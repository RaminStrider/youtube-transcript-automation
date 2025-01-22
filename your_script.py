from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import re
import os

# Print absolute path at the start
print(f"Absolute working directory: {os.path.abspath(os.getcwd())}")

def get_transcript(url):
    try:
        video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
        if not video_id_match:
            return "Invalid YouTube URL"
        
        video_id = video_id_match.group(1)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([d['text'] for d in transcript_list])
        
        # Create transcripts directory in the repository root
        transcript_dir = os.path.join(os.getcwd(), 'transcripts')
        os.makedirs(transcript_dir, exist_ok=True)
        print(f"Created directory at: {transcript_dir}")
        
        # Save file in the transcripts directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(transcript_dir, f"transcript_{timestamp}.txt")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write(f"YouTube URL: {url}\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(transcript)
        
        print(f"Saved transcript to: {filepath}")
        return f"Success: Transcript saved to {filepath}"
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"

# Test URLs
urls = [
    "https://www.youtube.com/watch?v=GMG-ZEG_VU4"
]

print("Starting transcript extraction...")
for url in urls:
    result = get_transcript(url)
    print(f"URL {url}: {result}")

print("\nFinal directory contents:")
os.system('ls -la')
if os.path.exists('transcripts'):
    print("\nTranscripts directory contents:")
    os.system('ls -la transcripts')
