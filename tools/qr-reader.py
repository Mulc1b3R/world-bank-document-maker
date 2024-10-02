from pyzbar.pyzbar import decode
from PIL import Image


# Provide the path to the QR code image you want to read
qr_code_image_path = "QR_External debt stocks.png"

def read_qr_code(image_path):
    # Open the QR code image
    img = Image.open(image_path)
    
    # Decode the QR code
    qr_code = decode(img)
    
    if qr_code:
        # Extract and return the data from the QR code
        return qr_code[0].data.decode('utf-8')
    else:
        return "No QR code detected."



# Call the read_qr_code function with the image path
result = read_qr_code(qr_code_image_path)



# Write the information to a file
with open('qr-code-info.txt', 'w') as file:
    file.write(str(result))

# Display the data from the QR code
print("Data from the QR code:", result)