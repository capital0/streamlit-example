from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# I love Business Analytics. 
This page is dedicated to my answers to homework questions.
Enjoy the art! I used streamlit to make this work. All code is written by Sinan.
"""


with st.echo(code_location='below'):
    total_points = st.slider("Please select hour", 1, 24, 1)
    num_turns = st.slider("Please select year", 2016, 2023, 1)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))