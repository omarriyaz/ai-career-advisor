# Using the youtube_transcript_api library to get the transcript of a YouTube video.

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Clean and join transcript text
        cleaned_transcript = " ".join([entry['text'] for entry in transcript])

        # return the cleaned transcript
        return cleaned_transcript
    
    except Exception as e:
        return ""  # Return an empty string if transcript is not available
