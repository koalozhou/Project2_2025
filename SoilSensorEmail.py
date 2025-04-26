#!/usr/bin/env python3

# Use Comments
# Program Title: SoilSensorEmail.py
# Program Description: Send email about the soil moisture status every three hours
# Name: Renjie Zhou
# Student ID: 202283890006  W20110010
# Course & Year: Project Semester 3 & Grade 3
# Date: 26/4/2025

import RPi.GPIO as GPIO
import smtplib
import time
from email.message import EmailMessage

# Sensor Configuration
SENSOR_PIN = 4         # GPIO4 (BCM numbering)
CHECK_INTERVAL = 3     # Check interval in hours
status_map = {
    1: ("Lack of water!", "[Alert] Please water you plant"),  # Dry soil status
    0: ("Plenty of water.", "[OK] Water not needed")  # Wet soil status
}

# Email Configuration (QQ example) 
SMTP_SERVER = 'smtp.qq.com'  # QQ SMTP server address
SMTP_PORT = 587              # QQ SMTP uses port 587 with TLS encryption
SENDER_EMAIL = "3502210237@qq.com"  # Sender's QQ email address
SENDER_PASSWORD = "gvrgbyvzmswccjdc"  # Authorization code for QQ email
RECEIVER_EMAIL = "1640379074@qq.com"   # Recipient's QQ email address

# GPIO Initialization Function
def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    print("GPIO initialization completed")

# Email Sending Function
def send_email(subject, body):
    try:
        # Create the email message
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

        # Connect to QQ's SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable TLS encryption
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
    finally:
        server.quit()

# Main Program
if __name__ == "__main__":
    try:
        # Initialize GPIO
        setup_gpio()
        
        # Convert CHECK_INTERVAL from hours to seconds
        check_interval = CHECK_INTERVAL * 3600  
        
        print(f"Plant monitoring system started, reporting every {CHECK_INTERVAL} hours...")
        
        while True:
            # Read the current status of the moisture sensor
            current_status = GPIO.input(SENSOR_PIN)
            
            # Generate email content based on sensor reading
            message, subject = status_map[current_status]
            email_body = f"""\
Detection time: {time.strftime('%Y-%m-%d %H:%M')}
Current status: {message}
Sensor reading: {'Dry' if current_status else 'Wet'}"""
            
            # Send the email report
            send_email(subject, email_body)
            
            # Wait for the next cycle
            time.sleep(check_interval)

    except KeyboardInterrupt:
        # Handle program termination gracefully
        print("\nProgram terminated")
    finally:
        # Clean up GPIO settings
        GPIO.cleanup()
