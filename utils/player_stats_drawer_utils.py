# import numpy as np
# import cv2

# def draw_player_stats(output_video_frames,player_stats,name1,name2):

#     for index, row in player_stats.iterrows():
#         player_1_shot_speed = row['player_1_last_shot_speed']
#         player_2_shot_speed = row['player_2_last_shot_speed']
#         player_1_speed = row['player_1_last_player_speed']
#         player_2_speed = row['player_2_last_player_speed']

#         avg_player_1_shot_speed = row['player_1_average_shot_speed']
#         avg_player_2_shot_speed = row['player_2_average_shot_speed']
#         avg_player_1_speed = row['player_1_average_player_speed']
#         avg_player_2_speed = row['player_2_average_player_speed']

#         frame = output_video_frames[index]
#         shapes = np.zeros_like(frame, np.uint8)

#         width=350
#         height=230

#         start_x = frame.shape[1]-400
#         start_y = frame.shape[0]-500
#         end_x = start_x+width
#         end_y = start_y+height

#         overlay = frame.copy()
#         cv2.rectangle(overlay, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
#         alpha = 0.5 
#         cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
#         output_video_frames[index] = frame

#         text = f"     {name1}     {name2}"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+80, start_y+30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
#         text = "Shot Speed"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+80), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
#         text = f"{player_1_shot_speed:.1f} km/h    {player_2_shot_speed:.1f} km/h"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+130, start_y+80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

#         text = "Player Speed"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
#         text = f"{player_1_speed:.1f} km/h    {player_2_speed:.1f} km/h"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+130, start_y+120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        
#         text = "avg. S. Speed"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+160), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
#         text = f"{avg_player_1_shot_speed:.1f} km/h    {avg_player_2_shot_speed:.1f} km/h"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+130, start_y+160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
#         text = "avg. P. Speed"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+200), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
#         text = f"{avg_player_1_speed:.1f} km/h    {avg_player_2_speed:.1f} km/h"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+130, start_y+200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
#     return output_video_frames


import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt

def draw_player_stats(output_video_frames, player_stats, name1, name2):
    data = []

    for index, row in player_stats.iterrows():
        player_1_shot_speed = row['player_1_last_shot_speed']
        player_2_shot_speed = row['player_2_last_shot_speed']
        player_1_speed = row['player_1_last_player_speed']
        player_2_speed = row['player_2_last_player_speed']

        avg_player_1_shot_speed = row['player_1_average_shot_speed']
        avg_player_2_shot_speed = row['player_2_average_shot_speed']
        avg_player_1_speed = row['player_1_average_player_speed']
        avg_player_2_speed = row['player_2_average_player_speed']

        # Append data for charts
        data.append([name1, player_1_shot_speed, player_1_speed])
        data.append([name2, player_2_shot_speed, player_2_speed])

        frame = output_video_frames[index]
        shapes = np.zeros_like(frame, np.uint8)

        width = 350
        height = 230

        start_x = frame.shape[1] - 400
        start_y = frame.shape[0] - 500
        end_x = start_x + width
        end_y = start_y + height

        overlay = frame.copy()
        cv2.rectangle(overlay, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
        alpha = 0.5 
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
        output_video_frames[index] = frame

        text = f"     {name1}     {name2}"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 80, start_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        text = "Shot Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        text = f"{player_1_shot_speed:.1f} km/h    {player_2_shot_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 130, start_y + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        text = "Player Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        text = f"{player_1_speed:.1f} km/h    {player_2_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 130, start_y + 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        text = "avg. S. Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 160), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        text = f"{avg_player_1_shot_speed:.1f} km/h    {avg_player_2_shot_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 130, start_y + 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        text = "avg. P. Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 200), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        text = f"{avg_player_1_speed:.1f} km/h    {avg_player_2_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 130, start_y + 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    # Create DataFrame and preprocess it
    analysis_df = pd.DataFrame(data, columns=['name', 'shot_speed', 'player_speed'])
    
    # Remove duplicates
    analysis_df.drop_duplicates(inplace=True)

    # Generate and save shot speed chart
    plt.figure(figsize=(10, 6))
    for name in analysis_df['name'].unique():
        subset = analysis_df[analysis_df['name'] == name]
        plt.plot(subset['shot_speed'].values, label=f'{name} Shot Speed')
    plt.xlabel('Index')
    plt.ylabel('Shot Speed (km/h)')
    plt.title('Shot Speed Comparison')
    plt.legend()
    plt.savefig('shot_speed_comparison.png')
    plt.close()

    # Generate and save player speed chart
    plt.figure(figsize=(10, 6))
    for name in analysis_df['name'].unique():
        subset = analysis_df[analysis_df['name'] == name]
        plt.plot(subset['player_speed'].values, label=f'{name} Player Speed')
    plt.xlabel('Index')
    plt.ylabel('Player Speed (km/h)')
    plt.title('Player Speed Comparison')
    plt.legend()
    plt.savefig('player_speed_comparison.png')
    plt.close()
    
    return output_video_frames

