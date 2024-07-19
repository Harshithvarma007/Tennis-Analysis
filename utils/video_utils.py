import cv2
import moviepy.editor as mp
import numpy as np

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

# def save_video(output_video_frames, output_video_path):
#     fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#     out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
#     for frame in output_video_frames:
#         out.write(frame)
#     out.release()


def save_video(output_video_frames, output_video_path):
    # Convert frames to RGB (from BGR)
    rgb_frames = [cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) for frame in output_video_frames]

    # Convert frames to moviepy ImageClip
    clips = [mp.ImageClip(np.asarray(frame)).set_duration(1/24) for frame in rgb_frames]
    video_clip = mp.concatenate_videoclips(clips, method="compose")

    # Write the video clip to file
    video_clip.write_videofile(output_video_path, codec='libx264', fps=24)