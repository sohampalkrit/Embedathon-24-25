  int rows[] = {21, 22, 23, 25, 26, 27, 32, 33}; // Row pins
  int cols[] = {4, 5, 13, 14, 16, 17, 18, 19};   // Column pins

  // Pattern to display
  int data[][8] = {
    {0,0,1,1,1,1,0,0},
    {0,1,0,0,0,0,1,0},
    {0,1,0,0,0,0,1,0},
    {0,1,1,1,1,1,1,0},
    {0,1,0,0,0,0,1,0},
    {0,1,0,0,0,0,1,0},
    {0,1,0,0,0,0,1,0},
    {0,0,0,0,0,0,0,0}
  };

  void setup() {
    // Set all row pins as OUTPUT
    for (int i = 0; i < 8; i++) {
      pinMode(rows[i], OUTPUT);
      digitalWrite(rows[i], LOW); // Turn rows off initially
    }

    // Set all column pins as OUTPUT
    for (int i = 0; i < 8; i++) {
      pinMode(cols[i], OUTPUT);
      digitalWrite(cols[i], HIGH); // Turn columns off initially
    }
  }

  void loop() {
    displayPattern(); // Display the defined pattern
  }

  // Function to display the pattern
  void displayPattern() {
    for (int row = 0; row < 8; row++) {
      for (int col = 0; col < 8; col++) {
        if (data[row][col] == 1) {
          lightLED(row, col); // Light up the LED for a '1'
        }
      }
    }
  }

  // Function to light up a single LED at (rowIdx, colIdx)
  void lightLED(int rowIdx, int colIdx) {
    // Turn off all rows and columns first
    for (int i = 0; i < 8; i++) {
      digitalWrite(rows[i], LOW);  // Turn all rows LOW
      digitalWrite(cols[i], HIGH); // Turn all columns HIGH
    }

    // Activate the desired row and column
    digitalWrite(rows[rowIdx], HIGH); // Set the specific row HIGH
    digitalWrite(cols[colIdx], LOW);  // Set the specific column LOW
    delay(1); // Small delay for stability (adjust if needed)
  }