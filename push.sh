#!/bin/zsh

# Stage all changes
git add .

# Ask for commit message
echo -n "Enter commit message: "
read commit_message

# Commit changes
git commit -m "$commit_message"

# Push to main
git push -u origin main

