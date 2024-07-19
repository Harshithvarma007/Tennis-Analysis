from utils import read_video, save_video
from trackers import PlayerTracker

def main():
    input_video_path = r"input_videos\input_video.mp4"
    output_video_path = r"output_videos\output_video.avi"

    # Read video frames
    video_frames = read_video(input_video_path)

    # Initialize player tracker with YOLOv10-Large model
    player_tracker = PlayerTracker(model_path=r"Models\yolov10l.pt")

    # Detect players in video frames
    player_detections = player_tracker.detect_frames(video_frames)

    # Draw bounding boxes around players
    output_video_frames = player_tracker.draw_bboxes(video_frames, player_detections)

    # Save processed video with bounding boxes
    save_video(output_video_frames, output_video_path)

if __name__ == "__main__":
    main()
