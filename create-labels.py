# This script removes default github labels and adds custom ones using python requests and the github API
# To work it needs: 1) User token, 2) Target username / organization name and target repository name and the 
# By Pablo and Spearbit with <3
# License: MIT

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
        print(r)
    print("Done deleting default labels!\n")


def create_new_labels():
    new_labels = [
        "Severity: Critical Risk", 
        "Severity: High Risk",
        "Severity: Medium Risk", 
        "Severity: Low Risk", 
        "Severity: Informational",
        "Severity: Gas Optimization",
        "Status: Acknowledged",
        "Status: Fixed",
        "Status: ReadyForReport"
    ]

    colors = [
        "ff0000",
        "B60205",
        "D93F0B",
        "FBCA04",
        "1D76DB",
        "B4E197",
        "5319E7",
        "0E8A16",
        "bfdadc"
    ]
    i = 0
    if len(new_labels) == len(colors):
        for n in new_labels:
            data={
                "name":n,
                "color":colors[i]
            }
            print(data)
            r = requests.post(f"https://api.github.com/repos/{username}/{repo}/labels", headers=headers, json=data)
            print(r)
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
    "Authorization":f"token {token}",
    "Accept": "application/vnd.github.v3+json",
    'User-Agent': 'request'
}

url = f"https://api.github.com/repos/{username}/{repo}/labels"

print(f"Deleting default labels in: {url}...")

delete_default_labels()

create_new_labels()

print("Please confirm old labels have been deleted and new ones have been created.")







