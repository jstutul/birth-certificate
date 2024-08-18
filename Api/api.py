import requests
from PIL import Image
from io import BytesIO
import pytesseract

# Fetch the CAPTCHA image
url = 'https://everify.bdris.gov.bd/DefaultCaptcha/Generate'
response = requests.get(url,verify=False)
img = Image.open(BytesIO(response.content))

# Optionally save the image to check it
img.save("captcha.png")

# Extract text from the image using pytesseract
captcha_text = pytesseract.image_to_string(img)

# Show the extracted text
print("Extracted CAPTCHA text:", captcha_text.strip())