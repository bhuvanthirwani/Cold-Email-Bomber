# email_utils/follow_up.py

"""
Module for sending follow-up emails to recipients.

This module includes functionality to load email settings, read email templates,
read recipient data from an Excel file, and send follow-up emails.

"""

import logging
from email_utils.email_sender import send_email
from email_utils.email_manager import load_email_settings, read_email_template, read_excel_data, read_follow_up_template
from data_utils.generate_email_address import generate_email_address  # Import the generate_email_address function

logger = logging.getLogger(__name__)

def send_follow_up_email(scenario):
    """
    Sends follow-up emails to recipients.

    This function loads email settings, email templates, and recipient data,
    and then iterates through each recipient to send a follow-up email.

    """
    sender_email, sender_password = load_email_settings()
    email_template = read_email_template()
    follow_up_template = read_follow_up_template()
    data = read_excel_data()
    print("Data: ", data)
    for row in data:
        first_name, last_name, email, company_name, designation = row

        generated_email = generate_email_address(first_name, last_name, email, company_name)
        print('generated_emails: ', generated_email)
        # Iterate through generated email addresses and send follow-up emails
        email = generated_email
        if email:
            subject = f"[Follow Up]: Exploring {designation} Roles at {company_name}"
            message = follow_up_template.format(first_name=first_name, last_name=last_name, email=email,
                                                company_name=company_name, designation=designation if designation else "esteemed employee")
            # Add additional string after "original email"
            original_email_info = f"<html><head></head><body><p>--------------- ORIGINAL EMAIL ---------------</p></br> <p>From: {sender_email}\nTo: {email}\n</p></br><p><strong>Subject: [Bhuvan Thirwani]: Exploring {designation} Roles at {company_name}</strong></p></body></html>"
            message += original_email_info
            message += email_template.format(first_name=first_name, last_name=last_name, email=email,
                                                company_name=company_name, designation=designation if designation else "esteemed employee")
            print(f"Email: {email}")
            send_email(sender_email, sender_password, email, subject, message, company_name, scenario)
        