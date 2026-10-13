import subprocess
import os
import sys

def execute_cmd(cmd, error_message):
    """Run terminal commands and capture errors cleanly."""
    try:
        res = subprocess.run(cmd, check=True, text=True, capture_output=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing: {' '.join(cmd)}")
        print(f"💬 Technical Details: {e.stderr.strip() if e.stderr else e}")
        print(f"⚠️ Action Required: {error_message}")
        sys.exit(1)

def unique_git_pipeline(repo_url, commit_msg, force_push=False):
    print("🎬 Starting Unique Turbo Push Pipeline...\n")

    # 1. Git Initialization Check
    if not os.path.exists(".git"):
        print("📁 [NEW REPO] Initializing local Git repository...")
        execute_cmd(["git", "init"], "Failed to initialize Git repository.")
        execute_cmd(["git", "branch", "-M", "main"], "Failed to set default branch to 'main'.")
    else:
        print("✅ [EXISTING REPO] Git repository already initialized.")

    # 2. Dynamic Remote Configuration
    print("🔗 Configuring remote repository URL...")
    # Purane rules clean karne ke liye link update karte hain
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
    execute_cmd(["git", "remote", "add", "origin", repo_url], "Could not link to the provided GitHub URL.")

    # 3. Smart Staging & Status Tracking
    print("📦 Staging files (git add .)...")
    execute_cmd(["git", "add", "."], "Failed to stage files.")

    # Check tracking changes
    status_check = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
    if not status_check.strip():
        print("ℹ️ No new changes detected. Everything is already up-to-date locally.")
    else:
        print(f"💾 Committing changes: '{commit_msg}'")
        execute_cmd(["git", "commit", "-m", commit_msg], "Commit failed. Check file permissions.")

    # 4. Smart Branch Detection
    current_branch = execute_cmd(["git", "branch", "--show-current"], "Could not detect active branch.")
    if not current_branch:
        current_branch = "main" # Fallback to main

    # 5. Safe Pull & Push Operation
    if force_push:
        print(f"⚠️ [FORCE MODE] Overwriting remote '{current_branch}' branch directly...")
        execute_cmd(["git", "push", "-f", "origin", current_branch], "Force push failed. Check token/credentials.")
    else:
        print(f"🔄 Pulling latest updates from remote '{current_branch}' branch to prevent merge conflicts...")
        subprocess.run(["git", "pull", "origin", current_branch, "--rebase"], capture_output=True)
        
        print(f"📤 Uploading your unique code to GitHub branch: '{current_branch}'...")
        execute_cmd(["git", "push", "-u", "origin", current_branch], "GitHub Push failed. Verify your access rights.")

    print(f"\n🎉 SUCCESS! Your code has been uploaded beautifully to: {repo_url}")

if __name__ == "__main__":
    # ⚠️ REPLACEMENTS: Apne GitHub ke data ke sath ise change karein
    YOUR_GITHUB_URL = "https://github.com"
    YOUR_COMMIT_MESSAGE = "feat: deployment of unique program code structure"
    
    # False = Safe push (Recommended) | True = Force push (Use only if remote history needs overwrite)
    FORCE = False 

    unique_git_pipeline(YOUR_GITHUB_URL, YOUR_COMMIT_MESSAGE, force_push=FORCE)
