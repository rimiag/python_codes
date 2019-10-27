# #Healthy Programmer
import playsound
import schedule
from datetime import datetime
import time

def getdate():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def eyes():
    playsound.playsound('eyes.mp3')
def workout():
    playsound.playsound('physical.mp3')
def drink_water():
 while True:
    playsound.playsound('water.mp3')
    n = input("Please confirm  'confirm' or 'Drank' :")
    if n.strip() == 'confirm' or 'Drank' or 'ok':
     break

# Generate a log files
f= open("Exe7_log.txt","w")
f.write(f"{getdate()} ")
f.close()

print("Welocme to Health concern ")
schedule.every(120).minutes.do(drink_water)
schedule.every(30).minutes.do(eyes)
schedule.every(200).minutes.do(workout)
while True:
 # Checks whether a scheduled task
 # is pending to run or not
 schedule.run_pending()
 time.sleep(1)

