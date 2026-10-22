import os
import subprocess


def push_to_github():
    # 1. Enter the path of your local project folder
    # Example: "C:/Users/Name/Projects/MyApp" or "." for current folder
    project_folder = "."

    # Change terminal directory to your project folder
    os.chdir(project_folder)

    try:
        print("📦 Adding files...")
        subprocess.run(["git", "add", "."], check=True)

        print("✍️ Committing changes...")
        commit_msg = "Code upload via Python script"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)

        print("🚀 Pushing to GitHub...")
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("🎉 Successfully pushed to GitHub!")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git error occurred: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    push_to_github()