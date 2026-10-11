import subprocess
import os

def push_to_github(commit_message, repo_url=None):
    try:
        # 1. Check agar .git folder already exist karta hai, nahi to initialize karega
        if not os.path.exists(".git"):
            print("🔄 Initializing local Git repository...")
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "branch", "-M", "main"], check=True)

        # 2. Files ko stage (add) karna
        print("📁 Staging all files...")
        subprocess.run(["git", "add", "."], check=True)

        # 3. Code commit karna
        print(f"💾 Committing changes with message: '{commit_message}'")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # 4. Remote repository add karna (agar URL diya hai aur setup nahi hai)
        if repo_url:
            # Puraane origin ko remove karke naya add karega taaki error na aaye
            subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
            print(f"🔗 Linking to remote repository: {repo_url}")
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)

        # 5. GitHub par push karna
        print("🚀 Pushing code to GitHub (main branch)...")
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        
        print("✅ Success! Tumhara code GitHub pe push ho gaya hai.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error occurred during Git execution: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# --- PROGRAM RUN KARNE KE LIYE CONFIGURATION ---
if __name__ == "__main__":
    # Apne GitHub repository ka actual URL yahan daalo
    GITHUB_REPO_URL = "https://github.com"
    
    # Aaj ka commit message
    COMMIT_MSG = "feat: add SHAP, LIME and push automation scripts"
    
    # Function ko call