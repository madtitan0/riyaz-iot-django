void setup() {
  Serial.begin(9600); // Set the baud rate to match the Django application
}

void loop() {
  // Read EMG sensor value
  int sensorValue = analogRead(A0); // Assuming the EMG sensor is connected to analog pin A0

  // Send the sensor value via serial communication
  Serial.println(sensorValue);

  delay(10); // Adjust the delay based on your requirements
}
