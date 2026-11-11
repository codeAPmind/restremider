import subprocess
from datetime import datetime

def get_today_git_logs_for_user(author_name):
    today = datetime.now().strftime('%Y-%m-%d')
    git_command = [
        "git",
        "log",
        f"--since={today}T00:00:00",
        f"--until={today}T23:59:59",
        # f"--author={author_name}",
        # "--pretty=format:%h - %s (%ad)",
        # "--date=local"
    ]

    try:
        result = subprocess.run(git_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        logs = result.stdout.strip()
        return logs if logs else None
    except subprocess.CalledProcessError as e:
        return None

def generate_daily_report(logs):
    today = datetime.now().strftime('%Y-%m-%d')
    report_header = f"## Daily Report - {today}\n"
    if logs:
        report_body = "\n".join([f"- {log}" for log in logs.split("\n")])
    else:
        report_body = "No commits for today."
    return report_header + report_body

if __name__ == "__main__":
    author = "himilong@yeah.net"  # Replace with your Git name or email
    logs = get_today_git_logs_for_user(author)
    daily_report = generate_daily_report(logs)
    print(daily_report)  # This can be sent to DingTalk
