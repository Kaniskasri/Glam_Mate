import boto3
from botocore.exceptions import ClientError
from flask import current_app
import logging

logger = logging.getLogger(__name__)

def send_booking_notification(appointment):
    """
    Send an email notification to the parlor when a new booking is made
    
    Args:
        appointment: The Appointment object containing booking details
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    # Get AWS SES configuration from app config
    aws_region = current_app.config['AWS_REGION']
    aws_access_key = current_app.config['AWS_ACCESS_KEY_ID']
    aws_secret_key = current_app.config['AWS_SECRET_ACCESS_KEY']
    sender_email = current_app.config['SENDER_EMAIL']
    recipient_email = current_app.config['RECIPIENT_EMAIL']
    
    # Create SES client
    ses_client = boto3.client(
        'ses',
        region_name=aws_region,
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    
    # Prepare email content
    subject = f"New Booking: {appointment.service} by {appointment.name}"
    
    # HTML body of the email
    html_body = f"""
    <html>
    <head></head>
    <body>
        <h1>New Appointment Booking</h1>
        <p>A new appointment has been booked with the following details:</p>
        <ul>
            <li><strong>Customer Name:</strong> {appointment.name}</li>
            <li><strong>Service:</strong> {appointment.service}</li>
            <li><strong>Location:</strong> {appointment.location}</li>
            <li><strong>Preferred Time:</strong> {appointment.preferred_time}</li>
            <li><strong>Booked On:</strong> {appointment.created_at.strftime('%Y-%m-%d %H:%M:%S')}</li>
        </ul>
        <p>Please confirm this appointment with the customer.</p>
        <p>Thank you,<br>GlamMate Booking System</p>
    </body>
    </html>
    """
    
    # Plain text version of the email
    text_body = f"""
    New Appointment Booking
    
    A new appointment has been booked with the following details:
    
    Customer Name: {appointment.name}
    Service: {appointment.service}
    Location: {appointment.location}
    Preferred Time: {appointment.preferred_time}
    Booked On: {appointment.created_at.strftime('%Y-%m-%d %H:%M:%S')}
    
    Please confirm this appointment with the customer.
    
    Thank you,
    GlamMate Booking System
    """
    
    # Try to send the email
    try:
        response = ses_client.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [recipient_email]
            },
            Message={
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': text_body,
                        'Charset': 'UTF-8'
                    },
                    'Html': {
                        'Data': html_body,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        logger.info(f"Email sent! Message ID: {response['MessageId']}")
        return True
    except ClientError as e:
        logger.error(f"Error sending email: {e.response['Error']['Message']}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error sending email: {str(e)}")
        return False