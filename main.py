import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

st.set_page_config(page_title="YouTube Transcript to Notes", layout="centered")

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 800 words. And you can add a little friendly message with emojis.
Please provide the summary of the text given here:  """

st.markdown(
    """
    <style>
    .main {
        background-color: #BB9AB1;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def extract_transcript_details(youtube_video_url, language):
    try:
        video_id = youtube_video_url.split("=")[1]

        # Fetch the transcript in the selected language
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

        transcript = []
        for i in transcript_text:
            transcript.append({"start": i["start"], "text": i["text"]})

        return transcript

    except TranscriptsDisabled:
        st.error("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        st.error(f"No transcript available in the '{language}' language.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Function for generating the summary based on the prompt
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    transcript_combined = " ".join([item["text"] for item in transcript_text])
    response = model.generate_content(prompt + transcript_combined)
    return response.text

# Streamlit App
st.title("YouTube Transcript to Notes")


# User inputs
youtube_link = st.text_input("Enter YouTube Video Link:")

# Language selection dropdown
language_options = {
    "English": "en",
    "Automatic": "auto",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-Hans"
}
language = st.selectbox("Select Transcript Language:", options=language_options.keys())
selected_language = language_options[language]

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.markdown(
        f"""
            <iframe width="100%" height="400" src="https://www.youtube.com/embed/{video_id}" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
            </iframe>
            """,
        unsafe_allow_html=True,
    )

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link, selected_language)

    if transcript_text:
        # Generate summary
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)

        # Display Transcript in Sections
        st.markdown("## Full Transcript (Grouped by 10-Minute Intervals):")

        # Group transcript sections by 10-minute intervals
        interval = 10 * 60  # 10 minutes in seconds
        grouped_transcript = {}
        for section in transcript_text:
            start_time = section["start"]
            interval_key = int(start_time // interval) * interval
            if interval_key not in grouped_transcript:
                grouped_transcript[interval_key] = []
            grouped_transcript[interval_key].append(section)

        # Display transcript grouped by intervals
        for interval_start in sorted(grouped_transcript.keys()):
            interval_end = interval_start + interval
            start_time_str = f"{int(interval_start // 60)}:{int(interval_start % 60):02}"
            end_time_str = f"{int(interval_end // 60)}:{int(interval_end % 60):02}"

            with st.expander(f"🕒 {start_time_str} - {end_time_str}"):
                # Joining text within each interval
                section_texts = " ".join([section["text"] for section in grouped_transcript[interval_start]])
                st.write(section_texts)
