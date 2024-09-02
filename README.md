# GitLab Tools

This collection of Python scripts automates various tasks for managing GitLab instances, providing a streamlined way to interact with GitLab APIs for different purposes.

## Features

- **Deploy Key Manager (`gitlab-deploy-key-manager.py`)**: Automates the management of deploy keys across multiple projects on GitLab, enabling you to check and enable deploy keys efficiently.
- **Group Cloner (`gitlab-group-cloner.py`)**: Facilitates the cloning of all repositories within a specified GitLab group, simplifying the process of managing multiple repositories.

## Prerequisites

Before running these scripts, ensure you have the following:
- Python 3.x installed on your machine.
- The `requests` library installed, which can be added via pip if not already installed.

## Installation

To set up the GitLab Tools on your local machine, follow these steps:

1. Clone the repository:
   ```plaintext
   git clone https://github.com/yourusername/gitlab-tools.git
   ```
2. Navigate to the cloned directory:
   ```plaintext
   cd gitlab-tools
   ```
3. Ensure Python3 and pip3 are installed:
   ```plaintext
   python3 --version
   pip3 --version
   ```
4. Install the required Python3 packages:
   ```plaintext
   pip3 install requests
   ```

## Usage

### Deploy Key Manager
To use the `gitlab-deploy-key-manager.py` script:

1. Open your terminal.
2. Navigate to the script's directory.
3. Run the script using Python3:
   ```plaintext
   python3 gitlab-deploy-key-manager.py
   ```
4. Follow the on-screen prompts to manage deploy keys.

### Group Cloner
To use the `gitlab-group-cloner.py` script:

1. Open your terminal.
2. Navigate to the script's directory.
3. Run the script using Python3:
   ```plaintext
   python3 gitlab-group-cloner.py
   ```
4. Follow the on-screen prompts to clone repositories.

## Configuration

Configure your GitLab API token and GitLab URL within each script to connect to your GitLab instance:

- Open the script file.
- Find the lines containing `API_TOKEN` and `GITLAB_URL`.
- Replace `your_api_token` and `https://gitlab.yourdomain.com` with your actual API token and GitLab URL.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes. For more insights into my other projects and professional background, feel free to visit my portfolio at [nordbye.it](https://nordbye.it/). Additional scripts that enhance the management of GitLab instances can be added by following the structure of the existing scripts.

## License

This project is licensed under the MIT License. A copy of the license is available in the repository in the LICENSE file.
