from ultralytics import YOLO

model=YOLO('Models\yolov5_best.pt')

result=model.predict('input_videos\input_video.mp4',save= True)

# print(result)
# print("boxes:")
# for box in result[0].boxes:
#     print(box)
