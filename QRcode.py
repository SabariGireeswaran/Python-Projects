import qrcode

url = input("Enter the url or text to generate QR code: ").strip()
file_path = input("Enter the file path to save the QR code image(including filename and .png extension): ").strip()

qr=qrcode.QRCode()          # Create QR code instance
qr.add_data(url)            # Add data to the QR code

img = qr.make_image()       # Create an image from the QR code instance 
img.save(file_path)         # Save the image to the specified file path

print("QR Code generated successfully!")