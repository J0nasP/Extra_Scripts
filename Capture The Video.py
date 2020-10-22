import numpy as np
import cv2


def VideoAndFaceCapture():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        #Capture frame-by-frame
        ret, frame = cap.read()

        # the operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        try:
            (x, y, w, h) = faces[0]
            cv2.imshow('img', frame[y:y+h, x:x+w])
        except:
            cv2.imshow('img', frame[y:y+h, x:x+w])
    cap.release()
    cv2.destroyAllWindows()



def VideoCaptureFromFile():
    cap = cv2.VideoCapture('output.avi')

    while cap.isOpened:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def VideoAndFaceAndRecord():
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame,0)
            
            # Write the flipped frame
            out.write(frame)        

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

VideoAndFaceCapture()
 