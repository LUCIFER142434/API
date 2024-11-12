import os
import json
from django.conf import settings

FILE_PATH = os.path.join(os.path.dirname(__file__),'date.json')

def read_date():
    with open(FILE_PATH,'r') as file:
        return json.load(file)
    
def write_date(date):
    with open(FILE_PATH,'w') as file:
        json.dump(date,file,indent=4)