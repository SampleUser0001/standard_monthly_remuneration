from PIL import Image
import pytesseract

# Load the image from file
image_path = 'image/center.png'
image = Image.open(image_path)

# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Remove commas and other non-digit characters from the extracted text
text_no_commas = ''.join([c for c in text if c.isdigit() or c == '\n'])

# Print the processed text
print(text_no_commas)
