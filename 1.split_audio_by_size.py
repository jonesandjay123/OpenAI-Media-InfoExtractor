import os
import sys
from pydub import AudioSegment

def split_audio_by_size(file_name, size_mb):
    # split mp3 file into smaller files, each smaller than the specified size in MB
    # each file is named as 1.mp3, 2.mp3, 3.mp3, etc.
    size_bytes = size_mb * 1024 * 1024
    sound = AudioSegment.from_mp3(file_name)
    length = len(sound)
    count = 1

    for i in range(0, length, size_bytes):
        output_file_name = str(count) + ".mp3"
        if i + size_bytes < length:
            sound[i:i + size_bytes].export(output_file_name, format="mp3")
        else:
            sound[i:].export(output_file_name, format="mp3")
        count += 1

# Example usage:
input_file_name = "audio/sample.mp3"  # Replace with your actual file path
max_file_size_mb = 22.5

split_audio_by_size(input_file_name, max_file_size_mb)
