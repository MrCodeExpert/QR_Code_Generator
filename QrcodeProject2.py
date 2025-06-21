import qrcode
from PIL import Image

# Get input from the user
data = input("Enter the URL or text for the QR code: ")
filename = input("Enter the name for the QR code image file (without extension): ")

# Set up the QR code parameters
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add user-provided data
qr.add_data(data)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill_color="green", back_color="white")

# Save the image using the user-provided filename
img.save(f"{filename}.png")
print(f"QR code saved as '{filename}.png'")
