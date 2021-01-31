#define fsrpin A0
int fsrreading; //Variable to store FSR value
void setup() {
  Serial.begin(9600);
}
void loop() {
  fsrreading = analogRead(fsrpin);
  Serial.print("Analog reading = ");
  Serial.print(fsrreading);
  if (fsrreading < 10) {
    Serial.println(" - No one on bed");
  } else if (fsrreading < 200) {
    Serial.println(" - Object on bed");
  } else if (fsrreading < 500) {
    Serial.println(" - Patient is on bed");
  } else {
    Serial.println(" - Patient is currently sleeping");
  }
  delay(500); //Delay 500 ms.
}