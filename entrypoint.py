#!/bin/python3

import os
import subprocess

model_id = os.getenv('INPUT_MODEL')
language = os.getenv('INPUT_LANGUAGE')

print('Model', model_id)
print('Language', language)

cmd='git diff --name-only 27efb55d3576ec8844b274eec7527909758b2a6a 97d8f06cd2b35842fb90fea9e39a3cc734f6bda2'
result=subprocess.getoutput(cmd)
print("result::",result)