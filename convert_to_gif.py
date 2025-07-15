from moviepy import VideoFileClip
import os
from Tiktok.download_tiktok import delete_dir_if_old
import random
import string

def generate_random_filename(extension=".gif"):
    """Generate a random filename for the video."""
    return f"gif_{''.join(random.choices(string.ascii_letters + string.digits, k=10))}{extension}"

def video_to_gif(video_path, fps=10):
    CURRENT_PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    SAVE = os.path.join(CURRENT_PROJECT_PATH, "downloads")    # Update this path if necessary
    OUTPUT = os.path.join(CURRENT_PROJECT_PATH, "result")   # Update this path if necessary
    delete_dir_if_old(SAVE)  # Delete old files in the downloads folder
    delete_dir_if_old(OUTPUT)  # Delete old files in the result folder
    # Ensure output folder exists
    os.makedirs(SAVE, exist_ok=True)
    os.makedirs(OUTPUT, exist_ok=True)
    filename = generate_random_filename()
    output_path = os.path.join(OUTPUT, filename)
    try:
        with VideoFileClip(video_path) as clip:
            clip.write_gif(output_path, fps=fps)
            return output_path
            print(f"GIF saved at {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

