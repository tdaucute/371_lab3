"""
image_client.py
Lab: Secure Image Transfer with RSA, DES, and Raspberry Pi GPIO
---------------------------------------------------------------

Your tasks:
- Use your RSA implementation to encrypt the DES key
- Use your DES implementation to encrypt the image
- Send the encrypted key and image to the server
- Buzz when the image is sent
"""

import socket
import time
import lgpio

from RSA import generate_keypair, encrypt
from des import des

# --- GPIO Setup (TODO: complete this section) ---
# TODO: Choose the correct BCM pin for the buzzer
# TODO: Open gpiochip and claim output for the buzzer
BUZZER_PIN = 27
h = lgpio.gpiochip_open(4)
lgpio.gpio_claim_output(h, BUZZER_PIN)

def buzz(duration=0.3):
    """TODO: Buzzer ON -> sleep -> OFF"""
    lgpio.gpio_write(h, BUZZER_PIN, 1)
    time.sleep(duration)
    lgpio.gpio_write(h, BUZZER_PIN, 0)

# --- RSA setup ---
p, q = 3557, 2579
public, private = generate_keypair(p, q)  # public=(e,n), private=(d,n)

# --- DES setup ---
cipher = des()
des_key = "8bytekey"  # must be 8 chars

# Load image as bytes, then map bytes→text losslessly via latin-1
with open("penguin.jpg", "rb") as f:
    image_bytes = f.read()

# TODO: Convert image_bytes to string (latin-1 safe)
# TODO: Encrypt with DES (use padding=True, cbc=True)
# TODO: Encrypt DES key with RSA
img_string = image_bytes.decode('latin-1')
img_estring = cipher.run_cbc(key=des_key, text=img_string, padding=True)
des_ekey = encrypt(private, des_key)

# --- Socket setup ---
HOST = "127.0.0.1"
PORT = 6000

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"[image_client] Connected to {HOST}:{PORT}")

    # Step 1: Send RSA public key
    # TODO
    e, n = public
    key_msg = f"KEY:{e},{n}"
    client.sendall(key_msg.encode("utf-8"))
    print(f"[image_client] Sent public key: ({e}, {n})")

    # Step 2: Send encrypted DES key
    # TODO
    des_ekey_str = ",".join(map(str, des_ekey))
    des_ekey_msg = "DESKEY:" + des_ekey_str
    client.sendall(des_ekey_msg.encode("utf-8"))
    print("[image_client] Sent encrypted DES key")

    # Step 3: Send encrypted image
    # TODO

    img_msg = "IMAGE:" + img_estring
    client.sendall(img_msg.encode("utf-8"))
    print("[image_client] Sent encrypted image")

    # Feedback
    buzz()

    client.close()
    lgpio.gpio_free(h, BUZZER_PIN)
    lgpio.gpiochip_close(h)
    print("[image_client] Closed connection and cleaned up GPIO.")

if __name__ == "__main__":
    main()
