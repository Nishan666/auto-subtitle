# Only Srt
# import os

# def extract_subtitles(video_folder, model="tiny"):
#     # Iterate over all files in the video folder
#     for filename in os.listdir(video_folder):
#         if filename.endswith(".mp4"):
#             # Construct input path
#             input_path = os.path.join(video_folder, filename)
            
#             # Construct the command to extract subtitles
#             command = f"auto_subtitle \"{input_path}\" --model {model} --srt_only True"
            
#             # Execute the command
#             os.system(command)

# if __name__ == "__main__":
#     # Specify the video folder
#     video_folder = "/home/nishan-7edge/auto-subtitle/test1"
    
#     # Extract subtitles for all video files in the folder
#     extract_subtitles(video_folder)
    
#     print("Subtitles extracted successfully.")


# srt and vtt
import os
import sys
import re
from pathlib import Path

def convertType(srtFile):
    # Get the directory of the script
    script_dir = os.path.dirname(__file__)
    srt_path = os.path.join(script_dir, srtFile)
    vtt_path = os.path.join(script_dir, Path(srtFile).stem + '.vtt')

    with open(srt_path, "r", encoding='utf8') as subtitlefile, open(vtt_path, "w", encoding='utf8') as convertedFile:
        lineArray = subtitlefile.read().splitlines()    
    
        convertedFile.write('WEBVTT\n\n')

        for line in lineArray:
            if not line.isdigit():
                convline = re.sub(',(?! )', '.', line)
                convertedFile.write(convline + '\n')

def extract_subtitles(video_folder, model="tiny"):
    # Iterate over all files in the video folder
    for filename in os.listdir(video_folder):
        if filename.endswith(".mp4"):
            # Construct input path
            input_path = os.path.join(video_folder, filename)
            
            # Construct the command to extract subtitles
            command = f"auto_subtitle \"{input_path}\" --model {model} --srt_only True"
            
            # Execute the command
            os.system(command)

            # Get the name of the SRT file
            srt_file = os.path.splitext(input_path)[0] + ".srt"
            
            # Convert SRT to VTT
            convertType(os.path.basename(srt_file))

if __name__ == "__main__":
    # Specify the video folder
    if len(sys.argv) != 2:
        print("Usage: python3 bulk.py <video_folder_path>")
        sys.exit(1)
    
    # Get the video folder path from the command line arguments
    video_folder = sys.argv[1]
    
    # Check if the provided path is a directory
    if not os.path.isdir(video_folder):
        print("Error: Provided path is not a directory.")
        sys.exit(1)
    
    # Extract subtitles for all video files in the folder
    extract_subtitles(video_folder)
    
    print("Subtitles extracted and converted successfully.")
