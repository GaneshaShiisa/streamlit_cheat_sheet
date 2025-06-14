import streamlit as st
import pandas as pd
import datetime

from util.util import link

with st.sidebar:
    link("st.button", "#st-button")
    link("st.download_button", "#st-download-button")
    link("st.st.link_button", "#st-link-button")
    link("st.page_link", "#st-page-link")
    link("st.data_editor", "#st-data-editor")
    link("st.checkbox", "#st-checkbox")
    link("st.feedback", "#st-feedback")
    link("st.pills", "#st-pills")
    link("st.segmented_control", "#st-segmented-control")
    link("st.radio", "#st-radio")
    link("st.toggle", "#st-toggle")
    link("st.selectbox", "#st-selectbox")
    link("st.multiselect", "#st-multiselect")
    link("st.slider", "#st-slider")
    link("st.select_slider", "#st-select-slider")
    link("st.text_input", "#st-text-input")
    link("st.number_input", "#st-number-input")
    link("st.text_area", "#st-text-area")
    link("st.date_input", "#st-date-input")
    link("st.time_input", "#st-time-input")
    link("st.file_uploader", "#st-file-uploader")
    link("st.audio_input", "#st-audio-input")
    link("st.camera_input", "#st-camera-input")
    link("st.color_picker", "#st-color-picker")

# Display interactive widgets
st.header("Display interactive widgets", anchor="display-interactive-widgets")

# st.button
link("<h3>st.button</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.button")
c1, c2, c3 = st.columns([1, 1, 1], border=True)
with c1:
    st.text('type="primary"')
    st.button("Reset", type="primary")
with c2:
    st.text('type="secondary"')
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")
with c3:
    st.text('type="tertiary"')
    if st.button("Aloha", type="tertiary"):
        st.write("Ciao")

# st.download_button
link("<h3>st.download_button</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.download_button")

st.download_button(
    label="Download Image",
    data=open("./media/Gq_I-T4aAAIrlGi.jpg", 'br'),
    file_name="sample.jpeg",
    mime="image/jpeg",
    icon=":material/download:",
)

# st.link_button
link("<h3>st.link_button</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.link_button")

st.link_button("link_button", "https://docs.streamlit.io/")

# st.page_link
link("<h3>st.page_link</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.page_link")

# st.page_link("app.py", label="Home")

# st.data_editor
link("<h3>st.data_editor</h3>",
     "https://docs.streamlit.io/develop/api-reference/data/st.data_editor")
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

# st.checkbox
link("<h3>st.checkbox</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox")

if st.checkbox("I agree"):
    st.write("Great!")

# st.feedback
link("<h3>st.feedback</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.feedback")
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

# st.pills
link("<h3>st.pills</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.pills")
options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

# st.segmented_control
link("<h3>st.segmented_control</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.segmented_control")
options = ["North", "East", "South", "West"]
selection = st.segmented_control(
    "Directions", options, selection_mode="single"
)
st.markdown(f"Your selected options: {selection}.")

# st.radio
link("<h3>st.radio</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.radio")
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)
if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write(f"You didn't select comedy. {genre}")

# st.toggle
link("<h3>st.toggle</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.toggle")
on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")

# st.selectbox
link("<h3>st.selectbox</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox")
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)
st.write("You selected:", option)

# st.multiselect
link("<h3>st.multiselect</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.multiselect")
options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)
st.write("You selected:", options)

# st.slider
link("<h3>st.slider</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.slider")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

# st.select_slider
link("<h3>st.select_slider</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.select_slider")
start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("red", "blue"),
)
st.write("You selected wavelengths between", start_color, "and", end_color)

# st.text_input
link("<h3>st.text_input</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.text_input")
title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

# st.number_input
link("<h3>st.number_input</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.number_input")
number = st.number_input("Insert a number")
st.write("The current number is ", number)

# st.text_area
link("<h3>st.text_area</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.text_area")
txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)
st.write(f"You wrote {len(txt)} characters.")

# st.date_input
link("<h3>st.date_input</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.date_input")
d = st.date_input("When's your birthday", datetime.date(2025, 6, 14))
st.write("Your birthday is:", d)

# st.time_input
link("<h3>st.time_input</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.time_input")
t = st.time_input("Set an alarm for", value=datetime.datetime.now())
st.write("Alarm is set for", t)

# st.file_uploader
link("<h3>st.file_uploader</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file.getvalue(),
             caption="Sample Image", use_container_width=True)

# st.audio_input
link("<h3>st.audio_input</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.audio_input")
audio_value = st.audio_input("Record a voice message")
if audio_value:
    st.audio(audio_value)

# st.camera_input
link("<h3>st.camera_input</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.camera_input")
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)
if picture:
    st.image(picture)

# st.color_picker
link("<h3>st.color_picker</h3>",
     "https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker")
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
