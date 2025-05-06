# GlamMate - Your Personal Beauty Booking Assistant

GlamMate is a modern web application for beauty parlors to showcase their services, manage customer appointments, and promote beauty products. It integrates AWS SES to notify the parlor when a booking is made.

## 🌟 Features

- **Responsive Design**: Beautiful and user-friendly interface that works on all devices
- **Service Booking**: Easy-to-use appointment booking system
- **Email Notifications**: Automatic email notifications via AWS SES when bookings are made
- **Product Showcase**: Display and sell beauty products online
- **MongoDB Integration**: Secure and scalable database for storing appointment data

## 📋 Pages Overview

1. **Home Page**
   - Parlor introduction
   - Best work photos
   - Testimonials & highlights
   - "Book Now" button

2. **Service Page**
   - List of services (Facial, Haircut, Bridal Makeup)
   - Appointment form with fields for:
     - Name
     - Location
     - Service
     - Preferred Time
   - On submit:
     - Save to database
     - Send email notification via AWS SES

3. **Shopping Page**
   - Showcase beauty products
   - Add to cart / Buy option

## 🔧 Tech Stack

- **Frontend:** HTML + CSS + JavaScript with Bootstrap
- **Backend:** Python (Flask)
- **Database:** MongoDB (via Flask-MongoEngine)
- **AWS Service:** AWS SES for sending email notifications

## 📦 Installation

### Quick Setup (Recommended)

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/glammate.git
   cd glammate
   ```

2. Run the setup script:
   ```
   # On Linux/Mac
   chmod +x setup.sh
   ./setup.sh
   
   # On Windows
   setup.bat
   ```

3. Create a `.env` file based on `.env.example` and add your configuration:
   ```
   cp .env.example .env
   # Edit .env with your settings
   ```

4. Run the application:
   ```
   python run.py
   ```

5. Visit `http://localhost:5000` in your browser

### Manual Setup

For detailed manual setup instructions, please refer to [SETUP.md](SETUP.md).

## 🔑 AWS SES Setup

1. Create an AWS account if you don't have one
2. Set up AWS SES:
   - Verify your email domain
   - Request production access if needed
   - Create IAM user with SES permissions
   - Generate access keys
3. Add AWS credentials to your `.env` file:
   ```
   AWS_REGION=your-region
   AWS_ACCESS_KEY_ID=your-access-key
   AWS_SECRET_ACCESS_KEY=your-secret-key
   ```

## 🧪 Testing

Run the application tests with:
```
python -m unittest test_app.py
```

Run the setup script tests with:
```
python -m unittest test_setup.py
```

Or run all tests with:
```
python -m unittest discover
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.



