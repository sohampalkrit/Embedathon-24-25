import websocket

# Connect to WebSocket server
ws = websocket.WebSocket()
ws.connect("ws://192.168.201.200")
print("Connected to WebSocket server")

try:
    while True:
        # Prompt user for input
        user_input = input("Say something (type 'exit' to quit): ")
        
        # Exit condition
        if user_input.lower() == "exit":
            print("Exiting...")
            break

        # Send the input to the WebSocket server
        ws.send(user_input)

        # Receive and print the server response
        result = ws.recv()
        print("Received: " + result)
finally:
    # Gracefully close WebSocket connection
    ws.close()
    print("WebSocket connection closed")

# Lines to decode
lines = [
    "18141312131254144313133",
    "1711131213131415111313121312131",
    "16131211141314141312131213121",
    "16131225541413124313133",
    "1652111413141452111413161",
    "1613121213131414131212131312131",
    "521312131213141413121313343"
]

# Function to decode a single line
def decode_line(sequence):
    row = []  # Initialize an empty row
    i = 0     # Iterator for the sequence

    while i < len(sequence):
        # Number of asterisks to place
        count = int(sequence[i])
        # Spaces to leave
        spaces = int(sequence[i + 1]) if i + 1 < len(sequence) else 0
        # Add the asterisks and spaces to the row
        row.extend(['*'] * count)
        row.extend([' '] * spaces)
        # Move to the next pair
        i += 2

    return ''.join(row)  # Convert row list into a string

# Decode all lines
def decode_lines(lines):
    decoded_rows = [decode_line(line) for line in lines]
    return decoded_rows

# Decode the lines and print the pattern
decoded_pattern = decode_lines(lines)

print("\nDecoded Pattern:")
for i, row in enumerate(decoded_pattern):
    print(f"Row {i + 1:2d}: {row}")
