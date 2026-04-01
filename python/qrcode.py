import qrcode
import base64
from io import BytesIO

# 1. Define the person's info or the link you want to encode
data = "https://www.github.com/rajsatyamraj03-collab"  # Replace with your actual URL

# 2. Create the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# 3. Save the image to an in-memory buffer
img = qr.make_image(fill_color="black", back_color="white")
buffer = BytesIO()
img.save(buffer, format="PNG")

# 4. Convert the image data to a Base64 string (Downloadable Link)
img_base64 = base64.b64encode(buffer.getvalue()).decode()
download_link = f"data:image/png;base64,{img_base64}"

print("\n--- GENERATED DOWNLOADABLE LINK ---")
print("Copy and paste the string below into your browser address bar to view/download the QR code:")
print(download_link)
