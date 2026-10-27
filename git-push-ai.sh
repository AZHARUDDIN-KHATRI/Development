if [ -z "$(git status --porcelain)" ]; then
    echo "No changes detected. Nothing to push."
    exit 0
fi

# 2. Stage all changes
git add .

# 3. Get the raw diff of your changes
git_diff=$(git diff --cached)

# 4. Use an AI CLI tool (like LLM or a simple curl request) to generate the commit message.
# (Make sure you have your API key set up in your environment variables)
echo "Generating AI commit message..."
commit_message=$(curl -s https://openai.com \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -D- \
  -d "{
    \"model\": \"gpt-4o-mini\",
    \"messages\": [
      {\"role\": \"system\", \"content\": \"You are a precise git assistant. Write a short, descriptive, single-line git commit message based on the provided diff. Do not include markdown formatting or explanations.\"},
      {\"role\": \"user\", \"content\": \"$git_diff\"}
    ]
  }" | grep -o '"content": "[^"]*' | grep -o '[^"]*$')

# Fallback if the AI fails
if [ -z "$commit_message" ]; then
    commit_message="Automated AI updates: $(date +'%Y-%m-%d %H:%M:%S')"
fi

echo "AI Generated Message: '$commit_message'"

# 5. Commit and push
git commit -m "$commit_message"
git push origin $(git branch --show-current)

echo "Pushed successfully!"