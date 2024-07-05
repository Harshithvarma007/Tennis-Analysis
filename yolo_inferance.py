from ultralytics import YOLO

model=YOLO('yolov10x')

model.predict('input_videos\input_video.mp4',save= True)

