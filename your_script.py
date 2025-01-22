from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import re
import os

def get_transcript(url):
    """Get transcript from YouTube video."""
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    if not video_id_match:
        return "Invalid YouTube URL"
    
    video_id = video_id_match.group(1)
    
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([d['text'] for d in transcript_list])
        
        # Create timestamp and filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if not os.path.exists('transcripts'):
            os.makedirs('transcripts')
        
        filename = f"transcripts/transcript_{timestamp}.txt"
        
        # Save to file with URL header
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")  # Separator line
            f.write(f"YouTube URL: {url}\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")  # Separator line
            f.write(transcript)
            
        return f"Transcript saved to {filename}"
    except Exception as e:
        return f"Error getting transcript: {str(e)}"

# Your YouTube URLs
urls = [
    "https://www.youtube.com/watch?v=GMG-ZEG_VU4",
    "https://www.youtube.com/watch?v=wjkPGhj2Odw"
]

# Process each URL
for url in urls:
    result = get_transcript(url)
    print(f"URL: {url} - {result}")


