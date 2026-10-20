from github import Github

# 1. Authenticate with your GitHub Personal Access Token
# Create a token here: GitHub Settings -> Developer Settings -> Personal Access Tokens
GITHUB_TOKEN = "your_personal_access_token_here"
g = Github(GITHUB_TOKEN)

# 2. Specify your repository details
# Format: "username/repository-name"
REPO_NAME = "your_username/your_repo_name"
repo = g.get_repo(REPO_NAME)

# 3. Define the file you want to upload
file_path_on_github = "data/hello.txt"  # Where it will save on GitHub
commit_message = "Upload via Python API"
file_content = "Hello, this file was pushed using a Python program!"

try:
    # Try to create a new file
    repo.create_file(
        path=file_path_on_github,
        message=commit_message,
        content=file_content,
        branch="main"  # Change to "master" if your default branch is different
    )
    print("🎉 File successfully pushed to GitHub!")

except Exception as e:
    # If the file already exists, we must update it instead
    if "already exists" in str(e).lower() or "sha" in str(e).lower():
        contents = repo.get_contents(file_path_on_github, ref="main")
        repo.update_file(
            path=file_path_on_github,
            message=commit_message,
            content=file_content,
            sha=contents.sha,
            branch="main"
        )
        print("🔄 Existing file successfully updated on GitHub!")
    else:
        print(f"❌ Failed to push: {e}")