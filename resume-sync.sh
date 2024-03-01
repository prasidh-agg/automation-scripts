#!/bin/bash

# Names of the resume files
local_resume="Resume_PrasidhAgg_fs.pdf"
github_resume="Prasidh-Aggarwal-Resume.pdf"

# Paths to the resume files
local_resume_path="/Users/titanium/Desktop/applications/current-resumes/$local_resume"
github_resume_path="/Users/titanium/Documents/portfolio/prasidh-agg.github.io/public/files/$github_resume"

# Function to perform git actions
perform_git_actions() {
    # Commit and push changes
    current_date=$(date +"%Y-%m-%d")

    cd /Users/titanium/Documents/portfolio/prasidh-agg.github.io
    git add "$github_resume_path"
    git commit -m "updated resume on $current_date"
    git push origin main
}

# Monitor changes to local_resume file
fswatch -0 "$local_resume_path" | while read -d "" event; do
    # Copy the local resume to the GitHub repository
    cp "$local_resume_path" "$github_resume_path"
    perform_git_actions
done