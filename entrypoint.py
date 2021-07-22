#!/bin/python3

import os
import subprocess

from github import Github


model_id = os.getenv('INPUT_MODEL')
language = os.getenv('INPUT_LANGUAGE')

print('Model', model_id)
print('Language', language)


# using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
files = repo.get_commit(sha=os.getenv('GITHUB_SHA')).files
print(files)

# cmd='curl -s https://api.github.com/ENDPOINT | jq -r '.files | .[] | select(.status == "modified") | .filename''
# result=subprocess.getoutput(cmd)
# print("result::",result)