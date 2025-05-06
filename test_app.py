import unittest
from unittest.mock import patch, MagicMock
from app import app
from models import Appointment
import json

class GlamMateTestCase(unittest.TestCase):
    
    def setUp(self):
        """Set up test client and other test variables."""
        self.app = app
        self.client = self.app.test_client
        self.app.config['TESTING'] = True
        
        # Mock appointment data
        self.appointment_data = {
            'name': 'Test User',
            'location': 'Test Location',
            'service': 'Basic Facial',
            'preferred_time': '2023-12-01T10:00'
        }
    
    @patch('app.send_booking_notification')
    @patch('app.Appointment')
    def test_book_appointment(self, mock_appointment, mock_send_notification):
        """Test booking an appointment."""
        # Set up the mock
        mock_instance = MagicMock()
        mock_appointment.return_value = mock_instance
        mock_send_notification.return_value = True
        
        # Send a POST request to book an appointment
        res = self.client().post('/book', data=self.appointment_data, follow_redirects=True)
        
        # Assert that the appointment was created
        mock_appointment.assert_called_with(
            name=self.appointment_data['name'],
            location=self.appointment_data['location'],
            service=self.appointment_data['service'],
            preferred_time=self.appointment_data['preferred_time']
        )
        
        # Assert that save was called
        mock_instance.save.assert_called_once()
        
        # Assert that the email notification was sent
        mock_send_notification.assert_called_once()
        
        # Assert that the response contains success message
        self.assertIn(b'Your appointment has been booked successfully', res.data)
    
    def test_home_page(self):
        """Test that the home page loads correctly."""
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Welcome to GlamMate', res.data)
    
    def test_services_page(self):
        """Test that the services page loads correctly."""
        res = self.client().get('/services')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Book an Appointment', res.data)
    
    def test_shop_page(self):
        """Test that the shop page loads correctly."""
        res = self.client().get('/shop')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Beauty Products', res.data)
    
    @patch('email_service.boto3.client')
    def test_send_booking_notification(self, mock_boto_client):
        """Test sending email notification via AWS SES."""
        from email_service import send_booking_notification
        
        # Create a mock SES client
        mock_ses_client = MagicMock()
        mock_boto_client.return_value = mock_ses_client
        
        # Create a mock response
        mock_ses_client.send_email.return_value = {'MessageId': 'test-message-id'}
        
        # Create a mock appointment
        mock_appointment = MagicMock()
        mock_appointment.name = 'Test User'
        mock_appointment.service = 'Basic Facial'
        mock_appointment.location = 'Test Location'
        mock_appointment.preferred_time = '2023-12-01T10:00'
        mock_appointment.created_at.strftime.return_value = '2023-11-15 10:00:00'
        
        # Call the function with app context
        with app.app_context():
            result = send_booking_notification(mock_appointment)
        
        # Assert that the function returned True (success)
        self.assertTrue(result)
        
        # Assert that send_email was called
        mock_ses_client.send_email.assert_called_once()

if __name__ == '__main__':
    unittest.main()