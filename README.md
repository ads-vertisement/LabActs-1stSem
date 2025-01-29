# Arduino and Python Lab Activities

This repository contains multiple lab activities involving Arduino and Python. The activities cover topics such as LED control, sensor integration, button interactions, and API communication between Arduino and Python.

## Activities Overview

### Components Used:
- Arduino board
- Bread board
- Push button
- Resistor(s) (1kΩ) for LED(s)
- Resistor(s) (10kΩ) for Button, Photoresistor, Temperature resistor/sensor
- LED(s)
- Wires

### Arduino Codes

#### Lab Act 1: LED Sequence (12 to 8 and 8 to 12)
- Turns LEDs ON and OFF sequentially.
- Uses pins 12, 11, 10, 9, and 8.

#### **Lab Act 2: LED Fading (12 to 8 and 8 to 12)**
- Controls the brightness of LEDs using PWM.
- Uses analog pins 3, 5, 6, 9, and 10.

#### **Lab Act 3: Fire Sensor Simulation**
- Simulates fire detection using a thermistor and photoresistor.
- Triggers an LED when temperature and brightness thresholds are exceeded.

#### **Lab Act 4: Fire Sensor Simulation with Stop Command**
- Same as Lab Act 3 but includes a stop command via Serial Monitor.
- Allows stopping the LED blinking using the "stop" command.

#### **Lab Act 5: Button Input with Python**
- Sends button press state from Arduino to Python via Serial.
- Used to trigger an API call in Python.

#### **Lab Act 6: LED Control via Python**
- Uses FastAPI to turn an LED ON/OFF through HTTP requests.
- Arduino listens for commands ('1' for ON, '0' for OFF).

#### **Midterms Lab: Light Intensity to Environment Mapping**
- Reads a light sensor and maps intensity to environmental conditions.
- Controls Green, Yellow, and Red LEDs based on intensity thresholds.
- Supports Manual and Automatic modes.

#### **Finals Lab: Button Interaction with Python API**
- Sends button press states to Python.
- Python script calls an API endpoint when the button is pressed.

---

### Python Codes

#### **Lab Act 5: Button API Trigger**
- Reads button states from Arduino and sends API requests based on button state.

#### **Lab Act 6: FastAPI-based LED Control**
- Provides API endpoints (`/led/on`, `/led/off`) to control Arduino LEDs.
- Establishes a Serial connection with the Arduino.

#### **Finals Lab: Button-triggered API Communication**
- Reads button states from Arduino and triggers an HTTP GET request to a specified API endpoint when pressed.
- Uses threading to continuously read data from Arduino while allowing API calls.

---

## How to Run the Codes

### **Arduino Codes**
1. Open the `.ino` file in the Arduino IDE.
2. Select the correct board and COM port.
3. Upload the sketch to the Arduino.
4. Open the Serial Monitor (if required) to interact with the system.

### **Python Codes**
1. Install required dependencies:
   ```sh
   pip install pyserial
   ```
   ```sh
   pip install fastapi
   ```
   ```sh
   pip install fastapi[standard]
   ```
   ```sh
    pip install requests
   ```
 - for uvicorn:
   ```sh
    pip install uvicorn
   ```
3. Run the Python script:
   ```sh
    python script_name.py
   ```
5. If using FastAPI, start the server with:
   ```sh
    uvicorn script_name:app --host 0.0.0.0 --port 8000
   ```

## Notes
- Update the `COM#` port in Python scripts to match your Arduino connection.
- Ensure the Arduino baud rate matches the Python serial communication settings.
- Modify API URLs as needed based on your network setup.

