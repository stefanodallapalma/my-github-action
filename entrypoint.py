#!/bin/python3

import os
import subprocess

model_id = os.getenv('INPUT_MODEL')
language = os.getenv('INPUT_LANGUAGE')

print('Model', model_id)
print('Language', language)

string='echo CIAO && ls'
result=subprocess.getoutput(string)
print("result::: ",result)