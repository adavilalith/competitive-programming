import os
import re
import glob
import subprocess
import requests
from datetime import datetime, timedelta

# ==============================================================================
# CONFIGURATION
# Paste your actual credentials gathered from browser DevTools -> Network panel
# ==============================================================================
LEETCODE_SESSION = "YOUR_LEETCODE_SESSION_COOKIE_HERE"
CSRF_TOKEN = "YOUR_CSRF_TOKEN_HERE"
LIMIT_SUBMISSIONS = 20  # Number of recent submissions to check at once

# Target output directory path relative to script execution context
TARGET_DIR = os.path.join(os.getcwd(), "leetcode", "problems")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Content-Type": "application/json",
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRF_TOKEN}",
    "X-CSRFToken": CSRF_TOKEN,
    "Referer": "https://leetcode.com/submissions/"
}

def fetch_recent_accepted_submissions():
    """Queries LeetCode GraphQL API for the latest user submissions."""
    url = "https://leetcode.com/graphql"
    
    query = """
    query submissionList($offset: Int!, $limit: Int!, $lastKey: String) {
      submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
        submissions {
          id
          title
          statusDisplay
          timestamp
        }
      }
    }
    """
    
    variables = {"offset": 0, "limit": LIMIT_SUBMISSIONS, "lastKey": None}
    
    try:
        response = requests.post(url, json={"query": query, "variables": variables}, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ Error talking to LeetCode API: Status Code {response.status_code}")
            return []
            
        data = response.json()
        submissions = data.get('data', {}).get('submissionList', {}).get('submissions', [])
        
        # Filter strictly for 'Accepted' answers
        return [s for s in submissions if s.get('statusDisplay') == 'Accepted']
    except Exception as e:
        print(f"❌ Network connection failure: {e}")
        return []

def fetch_submission_details(submission_id):
    """Retrieves source code and frontend problem ID for a given submission."""
    url = "https://leetcode.com/graphql"
    
    query = """
    query submissionDetails($submissionId: ID!) {
      submissionDetails(submissionId: $submissionId) {
        code
        question {
          frontendQuestionId
        }
      }
    }
    """
    
    variables = {"submissionId": submission_id}
    try:
        response = requests.post(url, json={"query": query, "variables": variables}, headers=HEADERS)
        if response.status_code != 200:
            return None, None
            
        detail = response.json().get('data', {}).get('submissionDetails', {})
        code = detail.get('code')
        frontend_id = detail.get('question', {}).get('frontendQuestionId')
        return code, frontend_id
    except Exception:
        return None, None

def execute_backdated_commit(file_name, problem_id, title, raw_epoch_time):
    """Executes atomic git commits using environment timestamp variables."""
    # Convert LeetCode epoch string to a date object, then pad +10 minutes
    submission_date = datetime.fromtimestamp(int(raw_epoch_time))
    backdated_time = submission_date + timedelta(minutes=10)
    iso_timestamp = backdated_time.isoformat()

    try:
        # Check if local Git tree exists, initialize if not
        if not os.path.exists(".git"):
            print("📦 Initializing local Git repository environment...")
            subprocess.run(["git", "init"], check=True)

        # Stage the targeted relative path file layout
        git_target_path = os.path.join("leetcode", "problems", file_name)
        subprocess.run(["git", "add", git_target_path], check=True)
        
        # Overlay the environment variables for authoring and committing metadata
        git_env = os.environ.copy()
        git_env["GIT_AUTHOR_DATE"] = iso_timestamp
        git_env["GIT_COMMITTER_DATE"] = iso_timestamp
        
        commit_message = f"Solves {problem_id}: {title}"
        subprocess.run(["git", "commit", "-m", commit_message], env=git_env, check=True)
        print(f"   🚀 Git commit synchronized and backdated to: {iso_timestamp}\n")
        
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Git system execution failed: {e}\n")

def main():
    # Make sure output tree directories exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    print("📡 Fetching your latest accepted submissions from LeetCode...")
    accepted_submissions = fetch_recent_accepted_submissions()
    
    if not accepted_submissions:
        print("Done. No recent accepted submissions found or session invalid.")
        return

    print(f"📊 Found {len(accepted_submissions)} accepted submissions. Verifying status...\n")

    for sub in accepted_submissions:
        title = sub['title']
        sub_id = sub['id']
        epoch_timestamp = sub['timestamp']

        # Query LeetCode depth metrics for source file code and exact problem ID
        code_text, problem_id = fetch_submission_details(sub_id)
        if not code_text or not problem_id:
            print(f"⚠️ Could not pull complete data payload for submission {sub_id}. Skipping.")
            continue

        # Check existing data tracking files mapping: '1234.*.py'
        search_pattern = os.path.join(TARGET_DIR, f"{problem_id}.*.py")
        if len(glob.glob(search_pattern)) > 0:
            print(f"⏭️  Skipping #{problem_id} ({title}): Already exists in your repository.")
            continue

        print(f"🌟 Processing New Entry -> #{problem_id}: {title}")

        # Standardize problem name to a file-safe lower-alphanumeric string
        cleaned_slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        file_name = f"{problem_id}.{cleaned_slug}.py"
        file_path = os.path.join(TARGET_DIR, file_name)

        # Write clean solution logic out to local disk file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code_text)
        print(f"   💾 Saved local copy to: ./leetcode/problems/{file_name}")

        # Package local change state to backdated Git engine
        execute_backdated_commit(file_name, problem_id, title, epoch_timestamp)

if __name__ == "__main__":
    main()