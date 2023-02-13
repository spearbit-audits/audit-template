"""
This script removes default github labels and adds custom ones using python requests and the github API
To work it needs:
 1) User token 
 2) Target username / organization name
 3) Target repository name and the 
By Pablo and Spearbit with <3
License: MIT
"""
import requests

def delete_default_labels():
    default_labels = [
        "bug", 
        "duplicate",
        "enhancement", 
        "invalid", 
        "question", 
        "wontfix", 
        "question", 
        "good first issue", 
        "help wanted", 
        "documentation"
        ]
    for i in default_labels:
        r = requests.delete(f"https://api.github.com/repos/{username}/{repo}/labels/{i}", headers=headers)
        print(f"Deleting {i}... Github API  ", r)
    print("Done deleting default labels!\n")


def create_new_labels():
    labels = [
        { "name": "Severity: Critical Risk", "color": "ff0000"},
        { "name": "Severity: High Risk" , "color": "B60205"},
        { "name": "Severity: Medium Risk" , "color": "D93F0B"},
        { "name": "Severity: Low Risk", "color": "FBCA04"},
        { "name": "Severity: Informational" , "color": "1D76DB"},
        { "name": "Severity: Gas Optimization", "color": "B4E197"},
        { "name": "Status: Acknowledged", "color": "5319E7"},
        { "name": "Status: Fixed", "color": "0E8A16"},
        { "name": "Status: ReadyForReport", "color": "bfdadc"},
        { "name": "Status: ReadyForReport", "color": "bfdadc"},
        { "name": "Monitoring: ", "color": "FBCA04", "description": "Invariants and areas for monitoring"}
    ]

    i = 0
    for data in labels:
        r = requests.post(f"https://api.github.com/repos/{username}/{repo}/labels", headers=headers, json=data)
        print(f"Creating new label {data}... Github API {r}")
        i+=1
    print("Done creating new labels!\n")



# __ MAIN __
print("Hello! This script will first delete all labels from the target repository and create custom ones. Please enter the following details:\n")
while(True):
    token = input(str("1) Access token: "))
    username = input(str("2) User / Organization name: "))
    repo = input(str("3) Target repo name: "))
    if token != "" and repo != "" and username != "":
        break
    print("Please fill in the details.")
 

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "request"
}

url = f"https://api.github.com/repos/{username}/{repo}/labels"

print(f"Deleting default labels in: {url}...\n")

delete_default_labels()

create_new_labels()

print("Please confirm old labels have been deleted and new ones have been created.")