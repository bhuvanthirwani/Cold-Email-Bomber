# main.py
"""
Entry point of Cold Email Bomber.
"""

import logging
import email_utils.follow_up as follow_up

from scheduler.schedule_now import send_emails_now
from scheduler.send_later import schedule_emails

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    choice = input("Is this the 1. first email or a 2. follow-up? (1/2): ").lower()

    if choice == '1':
        first_email_flow()
    elif choice == '2':
        follow_up_flow()
    else:
        print("Invalid choice. Please enter '1' or '2'.")

def first_email_flow():
    choice = input("Do you want to send the email 1. now or 2. schedule it for a specific time? (1/2): ").lower()

    if choice == '1':
        send_emails_now('first_email')
    elif choice == '2':
        schedule_emails('first_email')
    else:
        print("Invalid choice. Please enter '1' or '2'.")

def follow_up_flow():
    follow_up.send_follow_up_email('followup_email')

if __name__ == "__main__":
    main()
