# AI Project Idea Generator

AI Project Idea Generator is a Streamlit application that helps users generate project ideas, which they can add into their cv, to help break into into various career fields. By using YouTube videos related to specified role or field, the app extracts useful information and generates projects ideas to help users start in their chosen fields.

## Features

User Input: Enter a career path, field, or type of project you're interested in.
Video Search: Searches YouTube for videos based on your input, focusing on project ideas.
Transcript Extraction: Extracts and cleans the transcripts from the selected videos.
AI-Generated Project Ideas: Uses the Ollama LLaMA model to create a list of project ideas, including details on technologies used and to generate variations for each project.

## Project Structure

The project consists of four main Python files:

app.py: The main file for the Streamlit app. It handles user input, fetches videos, extracts transcripts, and displays the generated project ideas.
videos.py: Contains the fetch_videos function, which searches YouTube for relevant videos using the YouTube Data API.
transcript.py: Includes the get_transcript function to get and clean transcripts from YouTube videos using the youtube_transcript_api.
llmresponse.py: Handles communication with the Ollama LLaMA model to generate project ideas based on the video transcripts.
Installation

## To run this project locally, follow these steps:

1. Clone the repository:
   Into your terminal enter: "git clone https://github.com/omarriyaz/ai-project-ideas.git ai-project-ideas"

2. Install Dependencies
   Into your terminal enter: "pip install -r requirements.txt"

3. Set up API keys:
   Get a YouTube Data API key and replace API_KEY in videos.py with your key.

   ![Replace with Your API Key](ai-project-ideas/images/API.png "API")

4. Download Llama 3 onto your device
   Install Ollama from [Ollama](https://ollama.com), then into your terminal enter: "ollama pull llama3.1"

5. Run the Streamlit app:
   streamlit run app.py
