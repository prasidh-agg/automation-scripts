import requests
import smtplib
import boto3
from datetime import datetime, timedelta

def lambda_function(event, context):
    
    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId="github-access-token")
    access_token = response["SecretString"]
    response = client.get_secret_value(SecretId='smtp-password')
    smtp_password = response['SecretString']
    
    # Github API endpoint
    url = "https://api.github.com/repos/{username}/{repo}/commits"

    # Your GitHub username and repository name
    username = "prasidh-agg"
    repo = "java-blind75"

    # Email details
    email_sender = "prasidh2904agg@gmail.com"
    email_receiver = "aprasidh@gmail.com"
    email_password = {smtp_password}

    # Get the list of commits for the repository
    response = requests.get(url.format(username=username, repo=repo),
                            headers={"Authorization": f"Bearer {access_token}"})

    # Sort the commits by date
    commits = sorted(response.json(), key=lambda x: x["commit"]["author"]["date"])

    # Get the timestamp of the most recent commit
    most_recent_commit_time = datetime.strptime(commits[-1]["commit"]["author"]["date"],
                                                "%Y-%m-%dT%H:%M:%SZ")

    # Calculate the time elapsed since the most recent commit
    time_elapsed = datetime.utcnow() - most_recent_commit_time

    # If the time elapsed is greater than 24 hours, send an email notification
    if time_elapsed > timedelta(minutes=20):
        subject = 'Grind 75'
        body = f'You need to get back to grinding leetCode.. been a while. Just one commit, let\'s go! )'
        message = f'To: {email_receiver}\nSubject: {subject}\n\n{body}'
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, message)
        server.quit()

lambda_function()