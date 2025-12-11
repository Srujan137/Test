import requests
import json

SONAR_HOST = "http://localhost:9000"
PROJECT_KEY = "sample"

url = f"{SONAR_HOST}/api/issues/search?projects={PROJECT_KEY}&resolved=false"
response = requests.get(url, auth=(SONAR_TOKEN, ""))
data = response.json()

for issue in data.get("issues", []):
    print(f"File: {issue['component']}, Line: {issue['line']}, "
          f"Severity: {issue['severity']}, Rule: {issue['rule']}")
    print(f"Message: {issue['message']}\n")
