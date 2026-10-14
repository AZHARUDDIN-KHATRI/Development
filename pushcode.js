const { execSync } = require('child_process');

function pushToGithub(commitMessage = "Automated code update") {
    try {
        console.log("Staging files...");
        execSync('git add .');

        console.log(`Committing changes: "${commitMessage}"...`);
        execSync(`git commit -m "${commitMessage}"`);

        console.log("Pushing to remote repository...");
        execSync('git push origin main');

        console.log("🚀 Success! Your code has been programmatically pushed to GitHub.");
    } catch (error) {
        console.error("❌ An error occurred during the Git automation process:", error.message);
    }
}

// Run the automation function
pushToGithub("Code updated via automated Node.js script");