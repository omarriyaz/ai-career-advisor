# Main streamlit app code

import streamlit as st
from videos import fetch_videos
from transcript import get_transcript
from llmresponse import generate_ideas

def main():
    st.markdown("<h1 style='text-align: center; color: black;'>AI Project Generator</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: black;'>Get a project ideas and advice to break into the field of your choice!</h6>", unsafe_allow_html=True)

    # Create a form for input and button
    with st.form("idea_form"):
        # User input for career path or field of interest
        field = st.text_input("Enter a career path, field or type of project:")
        
        # Button to submit the form
        submit_button = st.form_submit_button(label="Generate Ideas")

    # Check if the form is submitted
    if submit_button:
        if field:
            with st.spinner("Fetching videos..."):
                video_ids = fetch_videos(field)
            
            with st.spinner("Extracting transcripts..."):
                transcripts = [get_transcript(video_id) for video_id in video_ids]
            
            with st.spinner("Generating Projects..."):
                roadmap = generate_ideas(transcripts)
            
            st.write("### Project Ideas:")
            st.write(roadmap)
        else:
            st.warning("Please enter a career path or field of interest to proceed.")

if __name__ == "__main__":
    main()
