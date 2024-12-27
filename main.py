import schedule
import time
import subprocess

#function to send designated message, replace'x-xxx-xxx-xxxx' to desired phone number
# replace the 'Message Example' to desired message
def send_message():
    subprocess.call("osascript sendMessage.applescript '%s' '%s'" % ('x-xxx-xxx-xxxx', f'{"Message Example"}'), shell=True)

if __name__ == '__main__':
   #uses schedule to call send message function at a given time in military format, change
    schedule.every().day.at('14:28').do(send_message)
    schedule.every().day.at('13:00').do(send_message)
    schedule.every().day.at('16:00').do(send_message)
    schedule.every().day.at('18:44').do(send_message)
    schedule.every().day.at('22:00').do(send_message)

    #sleep to rest the program
    while True:
        schedule.run_pending()
        time.sleep(1)
