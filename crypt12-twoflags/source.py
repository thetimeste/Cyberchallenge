
from PIL import Image
import numpy as np

# Load the encrypted images and the recovered key image
enc1 = Image.open("crypt12-twoflags/flag_enc.png")
key = Image.open("crypt12-twoflags/notflag_enc.png")

# Convert images to NumPy arrays
enc1_np = np.array(enc1) * 255
recovered_key_np = np.array(key) * 255

# Decrypt the images by XOR-ing with the recovered key
dec1 = np.bitwise_xor(enc1_np, recovered_key_np).astype(np.uint8)

# Create and save the decrypted images
Image.fromarray(dec1).save('crypt12-twoflags/decrypted_flag.png')

