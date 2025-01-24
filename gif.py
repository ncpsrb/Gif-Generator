from moviepy import VideoFileClip
import os
def video_to_gif(video_path, output_path, start_time=None, end_time=None):
    try:
        # Load the video file
        clip = VideoFileClip(video_path)
        clip.write_gif(output_path, fps=10)  # Adjust fps for desired quality
        print(f"GIF saved at {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_all_mp4_to_gif(input_folder, output_folder, start_time=None, end_time=None):
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.gif")
            video_to_gif(video_path, output_path, start_time, end_time)

# Example usage
input_folder = "source"  # Folder containing .mp4 files
output_folder = "output"  # Folder to save the GIFs

# Optional: Add start and end times (in seconds)
start_time = 5  # Start at 5 seconds
end_time = 50   # End at 10 seconds

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Convert all .mp4 files in the source folder to GIFs
convert_all_mp4_to_gif(input_folder, output_folder, start_time, end_time)