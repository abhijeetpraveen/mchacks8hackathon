#define watpin A3
int watreading; //Variable to store WSR value
void setup() {
  Serial.begin(9600);
}
void loop() {
  watreading = analogRead(watpin);
  Serial.print("Analog reading = ");
  Serial.print(watreading);
  if(fsrreading < 200) {
    Serial.println(" - Unneccessary");
  } else if (fsrreading <800) {
    Serial.println(" - Please Check on Catheter for Patient123");
  } else {
    Serial.println(" - MANDATORY CHANGE");
  }
  delay(500); //Delay 500 ms.
}