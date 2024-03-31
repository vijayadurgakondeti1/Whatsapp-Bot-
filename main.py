import pywhatkit
from datetime import datetime

def send_whatsapp_message():
    """Send a WhatsApp message at a scheduled time or instantly."""

    PHONE_NUMBER = input("Enter Phone Number: ")  # Must include region code and '+'
    MESSAGE = input("Enter Message: ")
    HR = int(input("Enter Hour (24-hour format): "))     
    MIN = int(input("Enter Minutes: "))

    # Send message at scheduled time
    pywhatkit.sendwhatmsg(PHONE_NUMBER, MESSAGE, HR, MIN)

    # Send message instantly
    pywhatkit.sendwhatmsg_instantly(PHONE_NUMBER, MESSAGE, tab_close=True)

def convert_image_to_ascii():
    """Convert an image to ASCII art and display."""

    image_path = input("Enter the path to the image file: ")
    output_mode = "ascii"

    # Convert image to ASCII art
    pywhatkit.image_to_ascii_art(image_path, output_mode)

if __name__ == "__main__":
    send_whatsapp_message()
    convert_image_to_ascii()
