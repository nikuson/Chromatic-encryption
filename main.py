from PIL import Image
def text_to_pixels(text):
    # Converting text to bytes
    bytes_text = text.encode('utf-8')
    # Creating a 128x128 image
    image = Image.new('RGB', (128, 128))
    pixels = image.load()
    byte_index = 0

    for i in range(128):
        for j in range(128):
            # Getting the next byte of text
            if byte_index < len(bytes_text):
                byte_value = bytes_text[byte_index]
            else:
                byte_value = 0
            # Writing the byte value to the pixel color
            pixels[i, j] = (byte_value, byte_value, byte_value)
            # Move to the next byte
            byte_index += 1

    return image

def pixels_to_text(image):
    pixels = image.load()
    # String for storing bytes of text
    bytes_text = b''

    for i in range(128):
        for j in range(128):
            pixel_value = pixels[i, j][0]
            bytes_text += bytes([pixel_value])
    # Decoding bytes into text
    decoded_text = bytes_text.decode('utf-8').rstrip('\x00')

    return decoded_text


# Usage example
text_to_encrypt = "Hello world!"
encrypted_image = text_to_pixels(text_to_encrypt)
encrypted_image.save("encrypted_image.png")

# Decoding example
decoded_text = pixels_to_text(encrypted_image)
print("Decoded Text:", decoded_text)
