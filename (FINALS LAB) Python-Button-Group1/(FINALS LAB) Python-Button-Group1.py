import serial
import requests  # To send HTTP requests
import time
from threading import Thread

# Arduino setup
arduino_port = "COM#"  # Replace with your Arduino port
baud_rate = 9600       # Match the baud rate in Arduino code
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Allow Arduino to initialize

# API URL
api_url = "http://your_endpoint_to_the_other_arduino" # Replace with your API endpoint

# Function to handle serial data and API calls
def read_from_arduino():
    try:
        while True:
            if ser.in_waiting > 0:  # Check if data is available
                data = ser.readline().decode('utf-8').strip()  # Read and decode data

                if data == "group1_on":  # Button pressed
                    print("Button Pressed")
                    # Call the API with a GET request, passing the button state as a query parameter
                    response = requests.get(f"{api_url}?groupName=group1_on", verify=False)
                    if response.status_code == 200:
                        print("API called successfully!")
                    else:
                        print(f"API call failed with status code: {response.status_code}")

                elif data == "group1_off":  # Button released
                    print("Button Not Pressed")
                    # Call the API with a GET request, passing the button state as a query parameter
                    response = requests.get(f"{api_url}?groupName=group1_off", verify=False)
                    if response.status_code == 200:
                        print("API called successfully!")
                    else:
                        print(f"API call failed with status code: {response.status_code}")

    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        ser.close()  # Close the serial connection

# Start the serial reading thread
thread = Thread(target=read_from_arduino, daemon=True)
thread.start()

# Keep the main thread running
while True:
    time.sleep(2)
