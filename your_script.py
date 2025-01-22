from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import re

def get_transcript(url):
    """Get transcript from YouTube video."""
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    if not video_id_match:
        return "Invalid YouTube URL"
    
    video_id = video_id_match.group(1)
    
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([d['text'] for d in transcript_list])
        
        # Save to file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d")
        filename = f"transcripts/transcript_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Transcript for: {url}\n\n")
            f.write(transcript)
            
        return "Transcript saved successfully"
    except Exception as e:
        return f"Error getting transcript: {str(e)}"

# Your YouTube URL list
urls = [
    "https://www.youtube.com/watch?v=GMG-ZEG_VU4",
    "https://www.youtube.com/watch?v=wjkPGhj2Odw"
]

# Process each URL
for url in urls:
    result = get_transcript(url)
    print(f"URL: {url} - {result}")
