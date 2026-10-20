import subprocess
import sys

def run_git_push(commit_message="Update code"):
    print("🚀 Starting Git automation...")
    
    # List of commands to execute sequentially
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", commit_message],
        ["git", "push"]
    ]
    
    for cmd in commands:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Check if the command failed
        if result.returncode != 0:
            # git commit returns code 1 if there is nothing new to commit
            if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
                print("ℹ️ Nothing new to commit. Moving on...")
                continue
            
            print(f"❌ Error running command: {' '.join(cmd)}")
            print(result.stderr)
            sys.exit(1)
            
    print("🎉 Success! Your code has been pushed to GitHub.")

if __name__ == "__main__":
    # You can pass a custom commit message when running the script
    # Example: python git_push.py "fixed login bug"
    msg = sys.argv[1] if len(sys.argv) > 1 else "Automated update via script"
    run_git_push(msg)