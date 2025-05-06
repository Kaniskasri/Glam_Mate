# GlamMate Setup Guide

This guide will help you set up the GlamMate application on your local machine.

## Prerequisites

- Python 3.7 or higher
- Git (optional, for cloning the repository)

## Setup Instructions

### Automatic Setup (Recommended)

#### For Linux/Mac:

1. Make the setup script executable:
   ```
   chmod +x setup.sh
   ```

2. Run the setup script:
   ```
   ./setup.sh
   ```

#### For Windows:

1. Run the setup script:
   ```
   setup.bat
   ```

### Manual Setup

If you prefer to set up the environment manually, follow these steps:

1. Create a virtual environment:
   ```
   # On Windows
   python -m venv venv
   
   # On Linux/Mac
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```
   # On Windows
   venv\Scripts\activate
   
   # On Linux/Mac
   source venv/bin/activate
   ```

3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

## Required Libraries

The application requires the following libraries, which are listed in `requirements.txt`:

- Flask==2.2.3
- flask-mongoengine==1.0.0
- boto3==1.26.84
- python-dotenv==1.0.0
- Werkzeug==2.2.3

## Environment Configuration

Before running the application, you need to set up your environment variables:

1. Create a `.env` file in the root directory of the project
2. Add the following variables to the file:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   MONGODB_URI=your_mongodb_connection_string
   AWS_REGION=your_aws_region
   AWS_ACCESS_KEY_ID=your_aws_access_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret_key
   ```

## Running the Application

After setting up the environment and installing the required libraries, you can run the application:

```
# Make sure the virtual environment is activated
python run.py
```

The application will be available at `http://localhost:5000`.

## Running Tests

To run the tests:

```
# Make sure the virtual environment is activated
python -m unittest test_app.py
```