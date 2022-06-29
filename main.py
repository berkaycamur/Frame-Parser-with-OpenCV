import cv2
import os
import uuid

video_path = r"/home/berkay/Masaüstü/videoplayback.mp4"
parser = int(input("Assign a parser: "))
capture = cv2.VideoCapture(video_path)
image_name = "saved_image.jpg"

os.chdir(r"/home/berkay/Masaüstü/F1_VIDEO")

frame_counter = 0
while True:
    ret, frame = capture.read()
    frame_counter += 1

    if frame_counter % parser == 0:
        cv2.imwrite(str(frame_counter) + "__" + str(uuid.uuid1()) + ".jpg", frame)

    else:
        continue




