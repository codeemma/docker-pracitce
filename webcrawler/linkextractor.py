#!/usr/bin/env python

import os
import requests
import schedule
import time 

url = os.getenv('WEB_URL')

def run():
    res = requests.get(url) 
    print(res.text)  


schedule.every(5).seconds.do(run)  

while True:  
    schedule.run_pending()
    time.sleep(1)
