# 1. Initialize Git (if not already initialized)
git init

# 2. Add all files
git add .

# 3. Commit your changes
git commit -m "Initial commit"

# 4. Rename the branch to main
git branch -M main

# 5. Connect your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

# 6. Push your code
git push -u origin main
If your project is already connected to GitHub
You usually only need these three commands:

bash
git add .
git commit -m "Updated project"
git push origin main
Example
Replace the URL with your own GitHub repository URL:

bash
git remote add origin https://github.com/john123/my-project.git
git push -u origin main
Note: If Git says remote origin already exists, run:

bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
If GitHub asks you to authenticate, sign in using the supported browser flow or configure a personal access token; your GitHub account password generally won't work for HTTPS Git operations.

