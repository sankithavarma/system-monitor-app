from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

# Welcome message
@app.route('/')
def home():
    return "Welcome to the System Monitor App! Visit /htop to view system info."

# System info route
@app.route('/htop')
def htop():
    # Debug print to check if this route is being accessed
    print("htop route triggered!")
    
    # Get full name (replace with your full name)
    full_name = "sample_name"  # Replace with your actual name

    # Get system username
    system_username = os.getlogin()

    # Get server time in IST
    ist_time = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S.%f")

    # Get 'top' output
    top_output = subprocess.getoutput("top -b -n 1")

    # Create the response with required details
    return f"""
    <pre>
    Name: {full_name}
    User: {system_username}
    Server Time (IST): {ist_time}

    TOP output:
    {top_output}
    </pre>
    """

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
