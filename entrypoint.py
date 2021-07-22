#!/bin/python3

import os
import subprocess

model_id = os.getenv('INPUT_MODEL')
language = os.getenv('INPUT_LANGUAGE')

print('Model', model_id)
print('Language', language)

cmd='git diff-tree --no-commit-id --name-only -r ${{ github.sha }} | xargs'
result=subprocess.getoutput(cmd)
print("result::",result)