import requests
import os
import subprocess

# Variables
API_TOKEN = "TEXT"
GITLAB_URL = "TEXT"

headers = {"PRIVATE-TOKEN": API_TOKEN}

def fetch_groups():
    """
    Fetch all top-level groups accessible by the user.
    """
    response = requests.get(f"{GITLAB_URL}/api/v4/groups", headers=headers)
    response.raise_for_status()
    groups = response.json()
    return [group for group in groups if '/' not in group['full_path']]

def display_groups(groups):
    """
    Display the list of groups to the user.
    """
    print("Available Groups:")
    for i, group in enumerate(groups):
        print(f"{i + 1}: {group['name']} ({group['full_path']})")
    print()

def get_group_id_by_selection(groups):
    """
    Prompt the user to select a group and return its ID.
    """
    display_groups(groups)
    selection = int(input("Enter the number of the group you want to clone projects from: ")) - 1
    if selection < 0 or selection >= len(groups):
        raise ValueError("Invalid selection. Please run the script again and select a valid group.")
    return groups[selection]['id'], groups[selection]['name']

def clone_project(project_name, repo_url, group_path):
    """
    Clone the project into the appropriate directory.
    """
    project_dir = os.path.join(group_path, project_name)
    if not os.path.exists(project_dir):
        os.makedirs(project_dir, exist_ok=True)
        print(f"Cloning {repo_url} into {project_dir}...")
        subprocess.run(['git', 'clone', repo_url, project_dir])
    else:
        print(f"Project {project_name} already exists in {project_dir}. Skipping clone.")

def get_projects_in_group(group_id, group_path):
    """
    Recursively get all projects under a group, including subgroups.
    """
    # Fetch all projects in the current group
    response = requests.get(f"{GITLAB_URL}/api/v4/groups/{group_id}/projects", headers=headers)
    response.raise_for_status()
    projects = response.json()

    for project in projects:
        clone_project(project['name'], project['ssh_url_to_repo'], group_path)

    # Fetch subgroups and recursively get their projects
    response = requests.get(f"{GITLAB_URL}/api/v4/groups/{group_id}/subgroups", headers=headers)
    response.raise_for_status()
    subgroups = response.json()

    for subgroup in subgroups:
        subgroup_path = os.path.join(group_path, subgroup['name'])
        os.makedirs(subgroup_path, exist_ok=True)
        get_projects_in_group(subgroup['id'], subgroup_path)

def main():
    try:
        # Fetch all top-level groups
        groups = fetch_groups()

        if not groups:
            print("No groups found.")
            return

        # Prompt user to select a group
        group_id, group_name = get_group_id_by_selection(groups)

        # Create a base directory named after the selected group
        base_path = os.path.join(os.getcwd(), group_name)
        os.makedirs(base_path, exist_ok=True)

        # Start cloning from the selected group
        print(f"Cloning all projects from Group ID {group_id} ({group_name})...")
        get_projects_in_group(group_id, base_path)

        print("All projects have been cloned successfully.")

    except KeyboardInterrupt:
        print("\nProcess was interrupted by the user. Exiting gracefully.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()



