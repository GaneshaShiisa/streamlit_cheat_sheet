import streamlit as st
import time

from util.util import link

with st.sidebar:
    link("st.write", "#st-write")
    link("st.write_stream", "#st-write-stream")
    link("st.title", "#st-title")
    link("st.header", "#st-header")
    link("st.subheader", "#st-subheader")
    link("st.markdown", "#st-markdown")
    link("st.latex", "#st-latex")
    link("st.code", "#st-code")
    link("st.badge", "#st-badge")
    link("st.html", "#st-html")

# Display text
st.header("Display text", anchor="display-text")

# st.write
link("<h3>st.write</h3>",
     "https://docs.streamlit.io/develop/api-reference/write-magic/st.write")

st.write("Hello, Streamlit!")
st.write(["st", "is <", 3])

# st.write_stream
link("<h3>st.write_stream</h3>",
     "https://docs.streamlit.io/develop/api-reference/write-magic/st.write")


def stream_data():
    SAMPLE_TEXT = """春はるは、あけぼの。やうやうしろくなりゆく山やまぎは、すこし明あかりて、紫むらさきだちたる雲くもの、細ほそくたなびきたる。"""

    for word in SAMPLE_TEXT:
        yield word
        time.sleep(0.01)


st.write_stream(stream_data)

# st.title
link("<h3>st.title</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.title")

st.title("My title", anchor="test")

# st.header
link("<h3>st.header</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.header")

st.header("My header")

# st.subheader
link("<h3>st.subheader</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.subheader")

st.subheader("My sub")

# st.text
link("<h3>st.text</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.text")

st.text("Fixed width text")

# st.caption
link("<h3>st.caption</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.caption")

st.caption("注釈")

# st.markdown
link("<h3>st.markdown</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.markdown")

st.markdown("_Markdown_")
st.markdown("**Markdown**")

# st.latex
link("<h3>st.latex</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.latex")

st.latex(R""" e^{i\pi} + 1 = 0 """)

# st.code
link("<h3>st.code</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.code")

st.code("for i in range(8): foo()")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

# st.badge
link("<h3>st.badge</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.badge")

st.badge("badge", color="green")

# st.html
link("<h3>st.html</h3>",
     "https://docs.streamlit.io/develop/api-reference/text/st.html")

st.html("<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>")
