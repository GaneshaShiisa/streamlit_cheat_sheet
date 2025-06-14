import streamlit as st
import pandas as pd
import numpy as np
from millify import millify


from util.util import link

with st.sidebar:
    link("st.dataframe", "#st-dataframe")
    link("st.table", "#st-table")
    link("st.json", "#st-json")
    link("st.metric", "#st-metric")

# Display data
st.subheader("Display data", anchor="display-data")

df = pd.DataFrame(
    np.random.randn(4, 5), columns=("col %d" % i for i in range(5))
)

# st.markdown
link("<h3>st.dataframe</h3>",
     "https://docs.streamlit.io/develop/api-reference/data/st.dataframe")

st.dataframe(df.style.highlight_max(axis=1))

# st.table
link("<h3>st.table</h3>",
     "https://docs.streamlit.io/develop/api-reference/data/st.table")

st.table(df)

# st.json
link("<h3>st.json</h3>",
     "https://docs.streamlit.io/develop/api-reference/data/st.json")

st.json({"data": {
    'name': 'abc',
    'age': 123
}})

# st.metric
link("<h3>st.metric</h3>",
     "https://docs.streamlit.io/develop/api-reference/data/st.metric")

col1, col2, col3 = st.columns(3)
col1.metric(label="Temperature", value="70 °F", delta="1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("My metric", millify(1234, precision=2), 2)
