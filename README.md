# Byte Brigades Embedathon

Team Byte Brigades's submission for IEEE Embedathon 2025. </br>
Team members :-
|Idx|Name|Roll No.|Contact|
|---|---|---|---|
| 1 | Mukul  | 231EE134   |  mukul.231ee134@nitk.edu.in|
| 2 | Soham | 231EE159  |   |
| 3 | Ratan | 231EC146  | ratan.231ec146@nitk.edu.in  |
---
## Milestone 1: How we got the values from esp32's NVS

### Step 1. EXTRACTING NVS DATA USING HEX EDITOR
1. First install [esptool.py](https://docs.espressif.com/projects/esptool/en/latest/esp32/) 
```python 
pip install esptool
```
2. Get the whole firmware that was loaded onto the esp32-id ;)
```bash
python -m esptool --port com11 read_flash 0x0 0x400000 firmware_backup.bin
```
```bash
python -m esptool --port com11 write_flash 0x0 firmware_backup.bin
```

3. Reading the firmware:
Using a hex editor like [hxd](https://mh-nexus.de/en/hxd/), we could view the whole firmware and things written to it.

Here is what we found:

![hex editor image output](/final_task/photos/hex_editor_output.png)

### Step 2. Converting the bin data to a usable format

####  Using Preference Library

Using this [code](final_task\milestone1\scripts\read_data\read_data.ino) we could read the value from NVS.

```bash
 line0: �?=18141312131254144313133
 line1: �?=1711131213131415111313121312131
 line2: �?=16131211141314141312131213121
 line3: �?=16131225541413124313133
 line4: �?=1652111413141452111413161
 line5: �?=1613121213131414131212131312131
 line6: �?=521312131213141413121313343
```

##### Code
```cpp
#include <Preferences.h>
Preferences preferences;
void setup() {
  Serial.begin(115200);
  if (preferences.begin("Passwords", true)) { // 'true' is for read only mode
   
    for (int i = 0; i <= 6; i++) {
      String key = "line" + String(i); 
      String storedValue = preferences.getString(key.c_str(), "default_value"); 
      Serial.println(" " + key + ": " + storedValue);
    }
  } else {
    Serial.println("Failed to open preferences.");
  }
  preferences.end();
}
void loop() {
}
```

---
## Milestone 2: How we sent to and decrypted the message on another PC

### Step 1. (Sort of) Manual Decryption

From the Problem Statement Document:
```
A mysterious sequence of digits, such as 13125216175, has
been transmitted by the ESP32. It appears to encode a hidden
visual pattern.
The sequence alternates between two roles, guiding the
structure of the pattern.
Your task is to interpret these numbers and reconstruct the
encoded representation.
```

- `visual pattern` indicated that there was definitely use of plotting techniques 
- `The sequence alternates between two roles, guiding the
structure of the pattern.` This meant we needed to alternate between the two symbols here we took as `*` and ` `
- For the even index we used `*` and ` ` for odd index
- We used the pattern for each line and got the outut ***LAKHTARUS*** which is the reverse of **SURATHKAL**
- So now we know to expect LAKHTARUS on the receiving computer.

### Step 2. Actually sending the data to the second PC
#### a. ESP32
- On the ESP we have a websocket running which takes the Key values from NVS of the ESP and converts it to readable format using the Preferences library.
- It then sends the data to the computer which decrypts it.
- **[This](final_task/milestone2/transmit_password_websocket/transmit_password_websocket.ino)** is the code which does this.

#### b. Receiving PC
- On the Receiving PC we have a python script which has 2 main functionalities.
- First part of the script deals with receiving the data from the websocket. Once it's received it, it stores it in a string and prints out that string for verification purposes.
- Second part of the script deals with decrypting the data received from the websocket. Once we have stored the received data in a string, we parse through it and print `*` and ` ` according to the rules established in manual decryption part.
- Upon performing this action, this is the output received.

#### c. Running the code
**[This](/final_task/milestone2/receive.py)** is the code which performs all this. To run this code follow the following steps:

  1. Change the ssid and password in transmit_password_websocket to the ssid and password of your network.
  2. Upload the code in transmit_password_websocket onto your ESP32.
  3. Press the reset button on your ESP32
  4. Clone the repo to a location of your choice on the receiving pc and change directory to that location
  5. Run `/final_task/milestone2/receive.py`

#### d. Output
![receive output](/final_task/milestone2/photos/output.png)

Click on this link for a demonstration video:
https://github.com/user-attachments/assets/2d24559f-222d-41d2-809e-943fc90f1c7d


---
## Milestone 3: Displaying the output on the LED matrix display
### Step 1: Receiving and Deciphering the message on the PC
Same as whatever was done in milestone 2. The message is received over WiFi and deciphered. Upload the updated ESP32 code onto your ESP. Located in ./final_task/milestone3/transmit_password_websocket/transmit_password_websocket.ino

### Step 2: Resending decrypted data back to ESP32
The decrypted data is converted to a list of 20 matrices, each one representing a single letter. Since our word is "LAKHTARUS", only 9 of the 20 letters are used. Each letter is a matrix of 1s and 0s, 1s representing a star and 0s representing a space.</br>
This data is sent to the ESP32 server.

### Step 3: Converting this List to a usable format for LED Matrix
The data is received in a JSON format, and the data is reconstructed into a matrix of size 8x160 (8x8 per letter) consisting of 1s and 0s where 1s represent LED ON and 0s represent LED off.</br> We have a temporary matrix of 8x8 which iterates throught the columns of the first long matrix. At each iteration we send the output of the temp matrix to our LED matrix for display. When the temporary matrix is full of 0's, it resets back to the beginning.

### Step 4: Utilizing the LED Matrix
1. Connect according to pin diagram; 

![LED MATRIX diagram]![image copy](https://github.com/user-attachments/assets/dbb8e165-42bf-461e-ba61-3153b3837cc0)


2. Using this [test all led](learning/led_matrix/test_all_led/test_all_led.ino) we could run all leds one by one 
  
3. Now, we discover an issue with the LED Matrix. We cannot display the whole letter at once. We can demonstrate this using an example. Let's say you wanna turn on points((1,2),(1,6),(3,4)) </br>
To do this, we need to turn on column 2,4 and 6. We will also need to turn on row 1 and 3. However, when we do this, we turn on (1,4), (3,2) and (3,6). To prevent this we use 
[scaninng](learning/led_matrix/display_pattern/display_pattern.ino).

4. So, we turn on necessary LED's in only one row at once. First line is turned on, and after a tiny delay of 1ms, second line is turned on and so on. This effectively appears as a whole to our eyes because of our human image retention time of 16ms. So we effectively achieve a sliding text effect on our LED matrix.

5. Done!!!

### Outputs

https://github.com/user-attachments/assets/a5f1b01b-5be3-4cf1-89e2-d425c5ec568f

https://github.com/user-attachments/assets/a68d9a00-05ce-4b9f-b052-ba4f45678f21



---

## References

[esp-32 idf](https://github.com/espressif/esp-idf) </br>
[8x8 LED Matrix for Arduino](https://youtu.be/G4lIo-MRSiY?si=LezqKGx4KDTxJ4l9) </br>
[788BS pinout](https://www.electronics-lab.com/community/index.php?/topic/48060-788bs-led-matrix-pinout/)
---
