import json
import urllib.request
import smtplib
from time import sleep
from datetime import datetime

message = """From: Is Lasership here yet?
Subject: Laserhip is here.
"""
print("Enter tracking number:", end = " ", flush=True)
trackingNum = input()
pkgURL = "http://www.lasership.com/track/" + trackingNum + "/json"
print("Sender Gmail username:", end = " ", flush=True)
senderUser = input()
print("Sender Gmail password:", end = " ", flush=True)
senderPass = input()
print("Receiver Gmail username:", end = " ", flush=True)
receiverUser = input()

while True:
    try:
        lsurl = urllib.request.urlopen(pkgURL)
        data = json.loads(lsurl.read().decode("utf-8"))
        if (data["Events"][0]["EventLabel"] == "Delivered"):
            smtpObj = smtplib.SMTP('smtp.gmail.com:587')
            smtpObj.starttls()
            smtpObj.login(senderUser, senderPass)
            smtpObj.sendmail(senderUser + "@gmail.com",
                receiverUser + "@gmail.com", message)
            break
        else:
            print(datetime.now().strftime('%I:%M%p')
                + " - I checked. Lasership is not here yet.")
            sleep(60)
    except:
        print(datetime.now().strftime('%I:%M%p')
            + " - I can't check if Lasership is here right now.")
        sleep(60)
