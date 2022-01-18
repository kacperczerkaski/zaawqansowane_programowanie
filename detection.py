import cv2
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detection(image: str):
    img = cv2.imread(image)
    img = imutils.resize(img, width=min(800, img.shape[1]))
    (frame, _) = hog.detectMultiScale(img, winStride=(4, 4), padding=(8, 8), scale=1.05)
    person = 1
    for x, y, w, h in frame:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1
    print("Number of people in this image: " + str(len(frame)))
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
