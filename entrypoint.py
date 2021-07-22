#!/bin/python3

import os
import requests
import subprocess

from github import Github
from repominer import filters  

from ansiblemetrics.metrics_extractor import extract_all as extract_ansible_metrics 
from toscametrics.metrics_extractor import extract_all as extract_tosca_metrics 

model_id = os.getenv('INPUT_MODEL')
language = os.getenv('INPUT_LANGUAGE')

print('Model', model_id)
print('Language', language)


# using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
files = repo.get_commit(sha=os.getenv('GITHUB_SHA')).files

for file in files:
    
    content = repo.get_contents(file.filename).decoded_content
    print(content)
    print('-------------')
    print(decoded_content)

    if language == 'ansible' and filters.is_ansible_file(file.filename):
        metrics = extract_ansible_metrics(content)
    elif language == 'tosca' and filters.is_tosca_file(file.filename, content):
        metrics = extract_tosca_metrics(content)
    else:
        continue

    print(metrics)