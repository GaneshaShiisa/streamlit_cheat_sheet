import streamlit as st


from util.util import link

with st.sidebar:
    link("st.image", "#st-image")
    link("st.audio", "#st-audio")
    link("st.video", "#st-video")

# Display media
st.header("Display media", anchor="display-media")

# st.image
link("<h3>st.image</h3>",
     "https://docs.streamlit.io/develop/api-reference/media/st.image")

st.image("./media/Gq_I-T4aAAIrlGi.jpg",
         caption="Sample Image", use_container_width=True)

# st.audio
link("<h3>st.audio</h3>",
     "https://docs.streamlit.io/develop/api-reference/media/st.audio")

st.audio("./media/sample.wav")

# st.video
link("<h3>st.video</h3>",
     "https://docs.streamlit.io/develop/api-reference/media/st.video")

video_file = open("./media/star.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
