# 1. Initialize git in your project folder
git init -b main

# 2. Stage all your project files
git add .

# 3. Commit the staged files
git commit -m "Initial commit"

# 4. Link your local project to your GitHub repository
# (Replace the URL with your actual GitHub repository URL)
git remote add origin https://github.com

# 5. Push the code and set the upstream default branch
git push -u origin main