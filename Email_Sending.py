# !/usr/bin/env python3

# Use Comments
# Program Title: Email_Sending.py
# Program Description: Send email from Raspberry Pi using script and smtp server
# Name: Renjie Zhou
# Student ID: 202283890006  W20110010
# Course & Year: Project Semester 3 & Grade 3
# Date: 21/4/2025

import smtplib
from email.message import EmailMessage


sender = "3502210237@qq.com"
password = "gvrgbyvzmswccjdc" 
recipient = "1640379074@qq.com"


msg = EmailMessage()
msg.set_content("Warning: Plant needs water！")
msg["Subject"] = "Warning"
msg["From"] = sender
msg["To"] = recipient


try:
    server = smtplib.SMTP("smtp.qq.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    print("email send successfully！")
except Exception as e:
    print(f"email send failed：{e}")
finally:
    server.quit()
