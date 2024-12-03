# GitHub User Activity Tracker CLI

This project is a simple command-line interface (CLI) application that fetches and displays the recent activity of a GitHub user. It serves as an excellent way to practice working with APIs, handling JSON data, and building a basic CLI application.
https://roadmap.sh/projects/github-user-activity
## Features

- Fetch the recent activity of a GitHub user using the GitHub API.
- Display a summary of the activity in the terminal.
- Handle errors gracefully, including invalid usernames or API failures.

## Requirements

- Python 3.x installed on your system.
- No external libraries or frameworks are required.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Keriii/github-activity.git
   ```
2. Navigate to the project directory:
   ```bash
   cd github-activity
   ```
3. Ensure Python 3.9 is installed and available in your terminal.

## Usage

Run the script from the command line with the following format:
```bash
python3 GithubActivityCLI.py github-activity <username>
```
- Replace `<username>` with the GitHub username whose activity you want to fetch.

### Example
```bash
python3 GitHubActivityCLI.py github-activity keriii
```
#### Output:
```
Output:
- Made Keriii/task-manager-CLI public
- Starred comet-ml/opik
- Created Keriii/test_dvc
- Created Keriii/test_dvc
```

## How It Works

1. **Argument Parsing**:
   - The CLI accepts the GitHub username as an argument using the `argparse` library.
   - Example command: `github-activity <username>`.

2. **Fetching Data**:
   - The script makes an HTTP GET request to the GitHub API endpoint:
     ```
     https://api.github.com/users/<username>/events
     ```

3. **Displaying Activity**:
   - The CLI processes the returned JSON data to extract and display relevant events, such as commits, issues, pull requests, and stars.

4. **Error Handling**:
   - Handles invalid usernames or API failures by checking the HTTP response status code and providing informative error messages.
