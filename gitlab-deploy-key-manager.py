import requests

# Variables
API_TOKEN = "TEXT"
GITLAB_URL = "TEXT"

def enable_key(project_id, project_name):
    print(f"Attempting to enable key on project {project_id} ({project_name}) with Deploy Key ID: {DEPLOY_KEY_ID}...")
    response = requests.post(
        f"{GITLAB_URL}/api/v4/projects/{project_id}/deploy_keys/{DEPLOY_KEY_ID}/enable",
        headers={"PRIVATE-TOKEN": API_TOKEN}
    )
    http_status = response.status_code
    body = response.json()
    print(f"HTTP Status Code: {http_status}")
    print(f"Response Body: {body}")
    if http_status not in (200, 201):
        print(f"Failed to enable key on project {project_id} ({project_name}): {body}")
    else:
        print(f"Key enabled successfully on project {project_id} ({project_name})")

try:
    # Fetch and list all deploy keys
    print("Fetching deploy keys...")
    response = requests.get(f"{GITLAB_URL}/api/v4/deploy_keys", headers={"PRIVATE-TOKEN": API_TOKEN})
    deploy_keys = response.json()
    for key in deploy_keys:
        print(f"{key['id']} - {key['title']}")

    DEPLOY_KEY_ID = input("Enter the ID of the deploy key to check across all projects: ")

    # Fetch all projects and store names with IDs
    print("Fetching project IDs and Names...")
    response = requests.get(f"{GITLAB_URL}/api/v4/projects?membership=true&per_page=100", headers={"PRIVATE-TOKEN": API_TOKEN})
    projects = response.json()
    project_details = {project['id']: project['name'] for project in projects}

    # Check if the selected deploy key is enabled in each project
    print("Checking deploy key in all projects...")
    project_status = {}
    for project_id, project_name in project_details.items():
        response = requests.get(
            f"{GITLAB_URL}/api/v4/projects/{project_id}/deploy_keys",
            headers={"PRIVATE-TOKEN": API_TOKEN}
        )
        deploy_keys = response.json()
        if any(key['id'] == int(DEPLOY_KEY_ID) for key in deploy_keys):
            project_status[project_id] = "Key is enabled"
        else:
            project_status[project_id] = "Key is not enabled"
        print(f"Project {project_id} ({project_name}): {project_status[project_id]}")

    # User input for further actions
    user_input = input("Enter 'all' to enable the key on all projects where it is not enabled, or enter specific project IDs separated by spaces to enable the key: ")
    if user_input == "all":
        for project_id, status in project_status.items():
            if status == "Key is not enabled":
                enable_key(project_id, project_details[project_id])
    else:
        for project_id in user_input.split():
            if project_status.get(int(project_id)) == "Key is not enabled":
                enable_key(int(project_id), project_details[int(project_id)])
            else:
                print(f"Key is already enabled on Project {project_id} ({project_details[int(project_id)]})")

except KeyboardInterrupt:
    print("\nProcess was interrupted by the user. Exiting gracefully.")
except Exception as e:
    print(f"An error occurred: {e}")

