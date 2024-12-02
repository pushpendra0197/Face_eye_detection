import cv2
import streamlit  as st
face_c=cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"haarcascade_eye.xml")

st.title("😃 and 👀 Detection")
button=st.button("Click For Camera")
Stop=st.button("Click for End")
frame_window=st.image([])
camera=cv2.VideoCapture(0)
if button:
    while True:
      _,frame=camera.read(0)
      frame=cv2.flip(frame,1)
      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces=face_c.detectMultiScale(gray,1.7)
      for x,y,w,h in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
         eye_gray=gray[x:x+w,y:y+h]
         eye_color=frame[x:x+w,y:y+h]
         eyes = eye_cascade.detectMultiScale(eye_gray,2)
         for ex,ey,ew,eh in eyes:
           cv2.rectangle(eye_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
      frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      frame_window.image(frame_rgb)
if Stop:
    camera.release()
         
