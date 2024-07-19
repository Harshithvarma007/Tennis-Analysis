import streamlit as st
import os
import main

# Set up the Streamlit app
st.set_page_config(page_title="Tennis Match Analysis", layout="wide")
    # Default video path
default_video_path = "input_video.mp4"
output_video_path = "output_video.mp4"
# Title and description
st.title("🏆 Tennis Match Analysis")
st.write(
    "Welcome to the Tennis Match Analysis app! Here you can upload a video of a tennis match, "
    "input player names, and analyze their performance. You can also try a default video to see how it works."
)

# Layout for video selection and player names input
col1, col2 = st.columns([2, 1])

with col1:

    # Default video button
    st.subheader("Try a Sample Video")
    if st.button("Play Sample Video"):
        st.video(default_video_path)

    # Video upload
    uploaded_video = st.file_uploader("Or, Upload Your Own Video", type=["mp4", "avi", "mov"])

with col2:
    # Player names input
    st.subheader("Player Information")
    name1 = st.text_input("Enter name for Player 1 (Player near the camera)", "Player 1")
    name2 = st.text_input("Enter name for Player 2 (Player facing the camera)", "Player 2")

# Analyze button
if st.button("Analyze"):

    input_video_path = default_video_path
    # Save the uploaded video to a file if it exists
    if uploaded_video:
        with open("uploaded_video.mp4", "wb") as f:
            f.write(uploaded_video.getbuffer())
        input_video_path = "uploaded_video.mp4"
    
    # Run the analysis function from main.py
    if uploaded_video or name1 != "Player 1" or name2 != "Player 2":
        main.main(input_video_path, name1, name2)
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
        
    st.subheader("Player Speed Comparison")
    if os.path.exists(player_speed_image_path):
        st.image(player_speed_image_path, caption="Player Speed Comparison")
    else:
        st.error(f"Player speed comparison image not found at {player_speed_image_path}")
        
    st.subheader("Shot Speed Comparison")
    if os.path.exists(shot_speed_image_path):
        st.image(shot_speed_image_path, caption="Shot Speed Comparison")
    else:
        st.error(f"Shot speed comparison image not found at {shot_speed_image_path}")

# Add a footer
st.write("---")
st.write("Developed by N Sai Harshith Varma")
