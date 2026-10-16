# 1. Initialize the local directory as a Git repository
git init -b main

# 2. Stage all your project files for the first commit
git add .

# 3. Commit the staged files with a message
git commit -m "First commit"

# 4. Link your local repository to your remote GitHub repository
# (Replace the URL with your actual GitHub repository URL)
git remote add origin https://github.com

# 5. Push the code to the main branch
git push -u origin main