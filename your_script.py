from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import re
import os

def get_transcript(url):
    """Get transcript from YouTube video."""
    print(f"Processing URL: {url}")
    print(f"Current working directory: {os.getcwd()}")
    
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    if not video_id_match:
        print("Invalid YouTube URL")
        return "Invalid YouTube URL"
    
    video_id = video_id_match.group(1)
    print(f"Video ID: {video_id}")
    
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([d['text'] for d in transcript_list])
        
        # Create timestamp and filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        print(f"Creating transcripts directory if it doesn't exist")
        if not os.path.exists('transcripts'):
            os.makedirs('transcripts')
            print("Created transcripts directory")
        
        filename = f"transcripts/transcript_{timestamp}.txt"
        print(f"Saving to file: {filename}")
        
        # Save to file with URL header
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")  # Separator line
            f.write(f"YouTube URL: {url}\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")  # Separator line
            f.write(transcript)
            
        print(f"File saved successfully")
        print(f"Checking if file exists: {os.path.exists(filename)}")
        return f"Transcript saved to {filename}"
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return f"Error getting transcript: {str(e)}"

# Your YouTube URLs
urls = [
    "https://www.youtube.com/watch?v=GMG-ZEG_VU4",
    "https://www.youtube.com/watch?v=wjkPGhj2Odw"
]

print("=== Starting transcript extraction ===")
print(f"Current directory contents: {os.listdir('.')}")

# Process each URL
for url in urls:
    result = get_transcript(url)
    print(f"Result for {url}: {result}")

print("=== Finished transcript extraction ===")
print(f"Final directory contents: {os.listdir('.')}")
if os.path.exists('transcripts'):
    print(f"Transcripts directory contents: {os.listdir('transcripts')}")
else:
    print("No transcripts directory found at the end")
