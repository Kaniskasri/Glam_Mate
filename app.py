from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import Appointment, db
from email_service import send_booking_notification
import os

app = Flask(__name__, template_folder='.')
app.config.from_object(Config)

# Initialize database
db.init_app(app)

@app.route('/')
def home():
    """Render the home page"""
    return render_template('home.html')

@app.route('/services')
def services():
    """Render the services page with booking form"""
    return render_template('services.html')

@app.route('/book', methods=['POST'])
def book_appointment():
    """Handle appointment booking form submission"""
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        service = request.form.get('service')
        preferred_time = request.form.get('preferred_time')
        
        # Validate form data
        if not all([name, location, service, preferred_time]):
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('services'))
        
        try:
            # Save appointment to database
            appointment = Appointment(
                name=name,
                location=location,
                service=service,
                preferred_time=preferred_time
            )
            appointment.save()
            
            # Send email notification
            send_booking_notification(appointment)
            
            flash('Your appointment has been booked successfully!', 'success')
            return redirect(url_for('services'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('services'))

@app.route('/shop')
def shop():
    """Render the shopping page"""
    return render_template('shop.html')

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
         db.create_all()
    
    app.run(debug=True)

