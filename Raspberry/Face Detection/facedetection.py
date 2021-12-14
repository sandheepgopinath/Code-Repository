# Import OpenCV library
import cv2

# Load a cascade file for detecting faces
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# Load image
image = cv2.imread("sasha-malia-obama-thanksgiving-pic-shutterstock-ftr-1-1.jpg")

# Convert into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Look for faces in the image using the loaded cascade file
faces = faceCascade.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in faces:
        # Create rectangle around faces
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

# Create the resizeable window
cv2.namedWindow('Obama', cv2.WINDOW_NORMAL)

# Display the image
cv2.imshow('Obama', image)

# Wait until we get a key
k=cv2.waitKey(0)

# If pressed key is 's'
if k == ord('s'):
    # Save the image
    cv2.imwrite('convertedimage.jpg', image)
    # Destroy all windows
    cv2.destroyAllWindows()
# If pressed key is ESC
elif k == 27:
    # Destroy all windows
    cv2.destroyAllWindows()
