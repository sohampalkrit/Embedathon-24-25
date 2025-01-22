class SHA1:
  def __init__(self):
     # Initial constants as defined by SHA-1 standard
    self.h0 = 0x67452301
    self.h1 = 0xEFCDAB89
    self.h2 = 0x98BADCFE
    self.h3 = 0x10325476
    self.h4 = 0xC3D2E1F0

  def _left_rotate(self, n, b):
    """Left rotate a 32-bit integer n by b bits."""
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF
  
  def _process_chunk(self, chunk):
    """Process a 512-bit chunk and update hash values."""
    w = [0] * 40
    for i in range(16):
      w[i] = int.from_bytes(chunk[i * 4:(i + 1) * 4], 'big')
    for i in range(16, 40):
      w[i] = self._left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)

    a, b, c, d, e = self.h0, self.h1, self.h2, self.h3, self.h4

    for i in range(40):
      if 0 <= i <= 19:
        f = (b & c) | (b & d) | (c & d)
        k = 0x8F1BBCDC
      elif 20 <= i <= 39:
        f = b ^ c ^ d
        k = 0xCA62C1D6

      # elif 40 <= i <= 59:
      #   f = (b & c) | (b & d) | (c & d)
      #   k = 0x8F1BBCDC
      # elif 60 <= i <= 79:
      #   f = b ^ c ^ d
      #   k = 0xCA62C1D6

      temp = (self._left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
      e = d
      d = c
      c = self._left_rotate(b, 30)
      b = a
      a = temp

    self.h0 = (self.h0 + a) & 0xFFFFFFFF
    self.h1 = (self.h1 + b) & 0xFFFFFFFF
    self.h2 = (self.h2 + c) & 0xFFFFFFFF
    self.h3 = (self.h3 + d) & 0xFFFFFFFF
    self.h4 = (self.h4 + e) & 0xFFFFFFFF

  def sha1(self, data: bytes) -> str:
    """Compute SHA-1 hash of the given data."""
    # Pre-processing
    original_length = len(data) * 8
    data += b'\x80'
    while (len(data) * 8) % 512 != 448:
      data += b'\x00'
    data += original_length.to_bytes(8, 'big')

    # Process each 512-bit chunk
    for i in range(0, len(data), 64):
      self._process_chunk(data[i:i + 64])

    # Produce final hash value
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(self.h0, self.h1, self.h2, self.h3, self.h4)

# Example usage
if __name__ == "__main__":
  input_string = input("Enter a string to hash using SHA-1:")
  sha1_hasher = SHA1()
  result = sha1_hasher.sha1(input_string.encode())
  print(f"SHA-1 hash of '{input_string}' is: {result}")