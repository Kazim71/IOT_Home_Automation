const int pulsePin = A0;  // A0 connected to JY-039 signal pin
int signal;
int threshold = 520;  // Adjust this based on your sensor readings
unsigned long lastBeat = 0;
int bpm = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pulsePin, INPUT);
}

void loop() {
  signal = analogRead(pulsePin);

  if (signal > threshold && (millis() - lastBeat) > 300) {
    unsigned long currentTime = millis();
    bpm = 60000 / (currentTime - lastBeat);
    lastBeat = currentTime;

    Serial.print("BPM: ");
    Serial.println(bpm);
  }

  delay(10);  // smooth read
}
