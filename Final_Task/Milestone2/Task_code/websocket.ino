#include <WiFi.h>
#include <WebSocketsServer.h>

// Wi-Fi credentials
const char* ssid = "vivo"; // Replace with your Wi-Fi SSID
const char* password = "tnhg31i8"; // Replace with your Wi-Fi password

// WebSocket server instance
WebSocketsServer webSocket = WebSocketsServer(80);

// Array of text lines to send
const char* lines[] = {
    "Line 0: ?=18141312131254144313133",
    "Line 1: ?=171113121313141511313121312131",
    "Line 2: ?=16131211413144141312131213121",
    "Line 3: ?=16131225541413124313133",
    "Line 4: ?=16521114131415211413161",
    "Line 5: ?=161312131313141413121313121",
    "Line 6: ?=521312131213141413121313343"
};

// Handle incoming WebSocket messages
void handleWebSocketMessage(uint8_t clientNum, uint8_t* payload, size_t length) {
    // Add logic here if needed to handle incoming messages
}

// Handle WebSocket events
void onWebSocketEvent(uint8_t clientNum, WStype_t type, uint8_t* payload, size_t length) {
    switch (type) {
        case WStype_CONNECTED:
            Serial.printf("Client #%u connected\n", clientNum);
            // Send all lines to the client when it connects
            for (int i = 0; i < sizeof(lines) / sizeof(lines[0]); i++) {
                webSocket.sendTXT(clientNum, lines[i]);
            }
            break;

        case WStype_DISCONNECTED:
            Serial.printf("Client #%u disconnected\n", clientNum);
            break;

        case WStype_TEXT:
            handleWebSocketMessage(clientNum, payload, length);
            break;
    }
}

// Setup function
void setup() {
    Serial.begin(115200);

    // Connect to Wi-Fi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
    Serial.println(WiFi.localIP());

    // Start WebSocket server
    webSocket.begin();
    webSocket.onEvent(onWebSocketEvent);
}

// Main loop
void loop() {
    webSocket.loop();
}
