import streamlit as st
import os
import main


# Streamlit application
st.title("Player Stats Analysis")

# Default video path
default_video_path = "input_videos/input_video.mp4"
output_video_path = "output_videos/output_video.mp4"

# Default video button
use_default_video = st.button("Try this video")
st.video(default_video_path)
# Video upload
uploaded_video = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])

# Player names input
name1 = st.text_input("Enter name for Player 1 (Player near the camera)", "Player 1")
name2 = st.text_input("Enter name for Player 2 (player facing the camera)", "Player 2")

# Analyze button
if st.button("Analyze"):

    input_video_path = default_video_path
    if uploaded_video:
        # Save the uploaded video to a file
        with open("uploaded_video.mp4", "wb") as f:
            f.write(uploaded_video.getbuffer())
        input_video_path = "uploaded_video.mp4"
    # else:
    #     st.error("Please upload a video or use the default video.")
    #     st.stop()
    if not (input_video_path == default_video_path and name1=="Player 1" and name2=="Player 2"):
        # Run the analysis function from main.py
        main.main(input_video_path,name1, name2)

    st.success("Analysis completed!")

    # Display the analyzed video
    
    if os.path.exists(output_video_path):
        st.subheader("Analyzed Video")
        st.video(output_video_path)
    else:
        st.error(f"Output video not found at {output_video_path}")

    # Display the comparison images
    player_speed_image_path = "player_speed_comparison.png"
    shot_speed_image_path = "shot_speed_comparison.png"
    
    if os.path.exists(player_speed_image_path):
        st.subheader("Player Speed Comparison")
        st.image(player_speed_image_path)
    else:
        st.error(f"Player speed comparison image not found at {player_speed_image_path}")
    
    if os.path.exists(shot_speed_image_path):
        st.subheader("Shot Speed Comparison")
        st.image(shot_speed_image_path)
    else:
        st.error(f"Shot speed comparison image not found at {shot_speed_image_path}")
