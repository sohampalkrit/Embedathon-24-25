
#include <Preferences.h> 
Preferences preferences; 
void setup() {
Serial.begin(115200); 
Serial.println("String 'Embedathon' has beenwrittentoNVM in namespace 'IEEE_NITK'.");

String value = preferences.getString("key","default");
Serial.print("Read back value: ");
Serial.println(value);

preferences.end();
}
void loop() {
// No operation in the loop
}