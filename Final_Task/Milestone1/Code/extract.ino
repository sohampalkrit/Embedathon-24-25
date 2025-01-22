
#include <Preferences.h>
Preferences preferences;
void setup() {
// Initialize Serial Monitor with 115200 baud rate
Serial.begin(115200);
// Wait for serial connection
delay(1000); // Give time for serial monitor to
connect
Serial.println("\n\n--- Starting Message Extraction ---");
// Open Preferences with namespace "Passwords" in
read-only mode
preferences.begin("Passwords"
, true); // true = read- only mode
Serial.println("\nExtracted messages:");
Serial.println("------------------");
// Read all lines (0-6)
String value;
bool foundMessage = false;
for (int i = 0; i <= 6; i++) {
char key[10];
snprintf(key, sizeof(key),"line%d", i);
// Get the stored string
value = preferences.getString(key,"");
if (value.length() > 0) {
foundMessage = true;
Serial.print("Line ");
Serial.print(i);
Serial.print(": ");
Serial.println(value);
delay(100); // Small delay between lines for
readability
}
}
if (!foundMessage) {
Serial.println("No messages found in memory!");
}
Serial.println("------------------");
// Close the Preferences
preferences.end();
}
void loop() {
// Keep the program running but do nothing
delay(1000);
}