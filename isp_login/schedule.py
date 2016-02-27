#!/usr/bin/env python2.7
import os
import subprocess
import schedule
import time

def job():
    print("Wait, while I search if you're logged in or not! ...")
    subprocess.call(["python","login.py"])

schedule.every(15).minutes.do(job) # Schedule the login script to do its job every 15 minutes.

while True:
    schedule.run_pending()
    time.sleep(1)
