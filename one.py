import sys
import face_recognition
import cv2
import subprocess

# Load known face encodings and their names
hn_image = face_recognition.load_image_file("C:/Users/alber/project/Harinath_photo.jpg")
hn_encoding = face_recognition.face_encodings(hn_image)[0]

if 'C:\\Users\\alber\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages' not in sys.path:
    sys.path.append('C:\\Users\\alber\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages')

# Load images and create face encodings
hn_image = face_recognition.load_image_file("C:/Users/alber/project/Harinath_photo.jpg")
hn_encoding = face_recognition.face_encodings(hn_image)[0]

shiv_image = face_recognition.load_image_file("C:/Users/alber/project/shivansh.jpg")
shiv_encoding = face_recognition.face_encodings(shiv_image)[0]

anuj_image = face_recognition.load_image_file("C:/Users/alber/project/anuj.jpeg")
anuj_encoding = face_recognition.face_encodings(anuj_image)[0]

rcs_sir_image = face_recognition.load_image_file("C:/Users/alber/project/rcs_sir.jpg")
rcs_sir_encoding = face_recognition.face_encodings(rcs_sir_image)[0]

amit_sir_image = face_recognition.load_image_file("C:/Users/alber/project/amit_sir.jpeg")
amit_sir_encoding = face_recognition.face_encodings(amit_sir_image)[0]

divya_maam_image = face_recognition.load_image_file("C:/Users/alber/project/divya_maam.jpg")
divya_maam_encoding = face_recognition.face_encodings(divya_maam_image)[0]

wairya_sir_image = face_recognition.load_image_file("C:/Users/alber/project/wairya_sir.png")
wairya_sir_encoding = face_recognition.face_encodings(wairya_sir_image)[0]

neelam_maam_image = face_recognition.load_image_file("C:/Users/alber/project/neelam_maam.jpg")
neelam_maam_encoding = face_recognition.face_encodings(neelam_maam_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [hn_encoding, shiv_encoding, anuj_encoding, rcs_sir_encoding, amit_sir_encoding, divya_maam_encoding, wairya_sir_encoding, neelam_maam_encoding]
known_face_names = ["Harinath Chaurasiya", "Shivansh Pathak", "Anuj Kori", "Dr Ram Chandra Singh Chauhan", "Er Amit Kumar", "Dr Divya Sharma", "Dr Subodh Wairya", "Dr Neelam Srivastava"]


# Initialize video capture with DirectShow backend
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video.isOpened():
    print("Error: Could not open video source.")
    sys.exit()

while True:
    ret, frame = video.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Find face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Initialize an empty list to store names for each face
    names = []

    # Loop through each face found in the frame
    for face_encoding in face_encodings:
        # Check if the face matches any known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"  # Default name for unknown faces

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        names.append(name)

    # Speak the name using espeak with Hindi language only if a new face is recognized
    for name in names:
        if name != "Unknown":
            subprocess.run(["C:\\Program Files (x86)\\eSpeak\\command_line\\espeak.exe", name, "-vhi"])
        else:
            subprocess.run(["C:\\Program Files (x86)\\eSpeak\\command_line\\espeak.exe", "Unknown person", "-vhi"])

    # Draw rectangles and labels for each face
    for (top, right, bottom, left), name in zip(face_locations, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
