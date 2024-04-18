
import cv2
import pytesseract
import pyttsx3

#print(pytesseract)
# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set Tesseract path (Change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert the frame to grayscale for OCR
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(gray)

    # Speak the extracted text
    engine.say(text)
    engine.runAndWait()

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
