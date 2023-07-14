# myapp/views.py
from django.shortcuts import render
#from contourpy import SerialContourGenerator
import serial
def emg_data_view(request):
    # Handle the request and retrieve EMG data
    # You can use the Serial library or a third-party library like pySerial to read data from the serial port

    # Read the EMG data from the serial port
    #import serial
    ser = serial.Serial('/dev/cu.usbserial-10', 9600)  # Update with the correct serial port and baud rate

    emg_data = []
    for _ in range(10):
        data = ser.readline().decode().strip()
        emg_data.append(data)

    ser.close()

    # Pass the EMG data to the template
    context = {'emg_data': emg_data}
    return render(request, 'myapp/emg_data.html', context)
