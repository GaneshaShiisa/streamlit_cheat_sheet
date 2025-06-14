import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import graphviz
import pydeck as pdk
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

from util.util import link


df = pd.DataFrame(
    np.random.randn(4, 5), columns=("col %d" % i for i in range(5))
)

with st.sidebar:
    link("st.line_chart", "#st-line-chart")
    link("st.scatter_chart", "#st-scatter-chart")
    link("st.area_chart", "#st-area-chart")
    link("st.bar_chart", "#st-bar-chart")
    link("st.map", "#st-map")
    link("st.altair_chart", "#st-altair-chart")
    link("st.graphviz_chart", "#st-graphviz-chart")
    link("st.plotly_chart", "#st-plotly-chart")
    link("st.pydeck_chart", "#st-pydeck-chart")
    link("st.pyplot", "#st-pyplot")

# Display charts
st.header("Display charts", anchor="display-charts")

# st.line_chart
link("<h3>st.line_chart</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.line_chart")

st.line_chart(df, x_label="x-label", y_label="y-label")

# st.scatter_chart
link("<h3>st.scatter_chart</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart")
st.scatter_chart(df)

# st.area_chart
link("<h3>st.area_chart</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.area_chart")

st.area_chart(df, x_label="x-label", y_label="y-label")

# st.bar_chart
link("<h3>st.bar_chart</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart")

st.bar_chart(df, x_label="x-label", y_label="y-label")
st.bar_chart(df, x_label="x-label", y_label="y-label", horizontal=True)

# st.map
link("<h3>st.map</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.map")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] +
    [36.7, 140],
    columns=["lat", "lon"],
)
st.map(df)

# st.altair_chart
link("<h3>st.altair_chart</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
chart = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.altair_chart(chart)

# st.graphviz_chart
link("<h3>st.graphviz_chart</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.graphviz_chart")

graph = graphviz.Digraph()
graph.edge("run", "intr")
graph.edge("intr", "runbl")
graph.edge("runbl", "run")
graph.edge("run", "kernel")
graph.edge("kernel", "zombie")
graph.edge("kernel", "sleep")
graph.edge("kernel", "runmem")
graph.edge("sleep", "swap")
graph.edge("swap", "runswap")
graph.edge("runswap", "new")
graph.edge("runswap", "runmem")
graph.edge("new", "runmem")
graph.edge("sleep", "runmem")

st.graphviz_chart(graph)

# st.plotly_chart
link("<h3>st.plotly_chart</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart")
link("plotly", "https://plotly.com/python/")

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

fig = ff.create_distplot(
    hist_data, group_labels, bin_size=[.1, .25, .5])

st.plotly_chart(fig)

# st.pydeck_chart
link("<h3>st.pydeck_chart</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart")
link("pydeck", "https://deckgl.readthedocs.io/en/latest/")

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

# st.pyplot
link("<h3>st.pyplot</h3>",
     "https://docs.streamlit.io/develop/api-reference/charts/st.pyplot")
link("matplotlib", "https://matplotlib.org/")
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)
