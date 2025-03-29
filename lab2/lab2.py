import cv2
import numpy as np

# deschide videoclipul
video_path = "D:/Vedere_artificiala/lab2/input.mp4"
cap = cv2.VideoCapture(video_path)

# obtine caracteristicile video
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, fps, (frame_width, frame_height))

max_radius = 150
min_radius = 5
radius_step = (max_radius - min_radius) / total_frames
line_y = 0
line_step = frame_height / total_frames
text = "Laborator VA"
text_to_display = ""
text_step = fps
prev_top_right = None

frame_idx = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break


    radius = int(min_radius + frame_idx * radius_step)
    cv2.circle(frame, (130, 190), radius, (255, 0, 0), -1)


    cv2.line(frame, (0, int(line_y)), (frame_width, int(line_y)), (0, 255, 0), 2)
    line_y += line_step


    if frame_idx % 10 == 0 and len(text_to_display) < len(text):
        text_to_display += text[len(text_to_display)]
    cv2.putText(frame, text_to_display, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


    if prev_top_right is not None:
        frame[-100:, -100:] = prev_top_right


    prev_top_right = frame[:100, -100:].copy()


    out.write(frame)
    frame_idx += 1

cap.release()
out.release()
cv2.destroyAllWindows()
