# YouTube Transcript to Notes

This is a python-and-streamlit-based web application. This extracts the transcript of a YouTube video, and generates a summarized version of the video using Google's generative AI ( gemini ). It also displays the full transcript grouped by 10-minute intervals. It provides users with detailed notes and helpful insights from YouTube videos.

## Features Provided

- **Video Transcript Extraction**: The app fetches the transcript of the YouTube video in the selected language.
- **AI-Powered Summary Generation**: It uses Google's Gemini AI to generate a concise summary of the video, providing important points within 800 words.
- **Full Transcript with Time Intervals**: Displays the full transcript of the video grouped by 10-minute intervals for easier reading.
- **Multi-Language Support**: Supports multiple languages for transcript extraction, including English, Spanish, French, and more.

## How to Use

1. **Enter YouTube Video Link**: Paste the URL of a YouTube video in the input box.
2. **Select Transcript Language**: Choose the language you want the transcript to be fetched in.
3. **Click on "Get Detailed Notes"**: Once the video and language are selected, click the button to fetch the transcript and generate a summary.
4. **View Summary and Transcript**: The summary of the video will be displayed, followed by the full transcript grouped in 10-minute intervals. You can expand each section to view the transcript content.

## Installation

To run this app locally, follow these steps:

### Prerequisites
Ensure you have Python 3.7+ installed on your system.

### Steps
- **Install the necessary libraries**: Install youtube_transcript_api , streamlit , google-generativeai , python-dotenv , pathlib
- **Set Up API Keys**:
    Create a .env file in the root directory of the project
    "GOOGLE_API_KEY=your_api_key_here"
- **Run the App**: streamlit run app.py

## Future Scope
- **Support for More Languages**: Extend the language support for transcripts and summaries to include more languages and dialects.
- **Video Processing Improvements**: Improve the handling of longer videos and large transcripts by implementing more efficient processing methods.
- **User Authentication**: Add user login and history tracking, so users can save their transcripts and summaries for later reference.
- **Customization Options**: Allow users to customize the summary length or output format based on their preferences.
- **Integration with Other Video Platforms**: Expand the app to support other video platforms like Vimeo or Dailymotion, beyond just YouTube.
- **Mobile Support**: Make the app more mobile-friendly by optimizing the interface for smaller screens.

