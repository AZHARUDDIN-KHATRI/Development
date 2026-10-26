git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main


Replace YOUR_USERNAME with your GitHub username and YOUR_REPOSITORY with your repository name.
2. If GitHub is already connected
If you have already created the Git repository and connected it to GitHub, you only need:
git add .
git commit -m "Updated project"
git push origin main


3. Check your GitHub connection
git remote -v


Check your current branch:
git branch


Check the status of your files:
git status


4. If you get an error
If you see remote origin already exists, use:
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git


Then push:
git push -u origin main