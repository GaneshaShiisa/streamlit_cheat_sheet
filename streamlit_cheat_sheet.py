import streamlit as st

from util.util import load_custom_css


load_custom_css("./style.css")

st.logo("./media/streamlit_cheat_sheet.png",
        icon_image="./media/streamlit_cheat_sheet_min.png")

home = st.Page(
    page="pages/home.py", title="Home", icon=":material/home:", default=True
)
display_text = st.Page(
    page="pages/display_text.py", title="Display text", icon=":material/grading:"
)
display_data = st.Page(
    page="pages/display_data.py", title="Display data", icon=":material/table:"
)
display_media = st.Page(
    page="pages/display_media.py", title="Display media", icon=":material/photo:"
)
display_chart = st.Page(
    page="pages/display_chart.py", title="Display chart", icon=":material/monitoring:"
)
display_interactive_widget = st.Page(
    page="pages/display_interactive_widget.py", title="Display interactive widgets", icon=":material/edit:"
)
demo_in_progress = st.Page(page="pages/demo_in_progress.py", title="Demo in progress", icon=":material/autorenew:"
                           )

pg = st.navigation([home, display_text, display_data, display_media,
                   display_chart, display_interactive_widget, demo_in_progress])
pg.run()
