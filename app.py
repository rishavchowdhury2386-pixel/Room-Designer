from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="One-Point Perspective Room Designer",
                   page_icon="🏠", layout="wide")

# The interactive designer is the index.html file that sits next to this script.
html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")

st.title("One-Point Perspective Virtual Room Designer")

tab_app, tab_theory, tab_about = st.tabs(["Designer", "How it works", "About"])

with tab_app:
    components.html(html, height=840, scrolling=True)

with tab_theory:
    st.subheader("Perspective projection")
    st.write("The camera looks straight at the back wall. Each 3D point (x, y, z) "
             "is drawn on screen with:")
    st.latex(r"x' = c_x + f\,\frac{x}{z} \qquad y' = c_y - f\,\frac{y}{z}")
    st.write("As z grows, every point moves toward the vanishing point, so all depth "
             "lines meet at one point. An object of width w appears with width:")
    st.latex(r"\text{apparent width} = \frac{f\,w}{z}")
    st.write("Moving the vanishing point to (vp_x, vp_y) while keeping the front opening fixed:")
    st.latex(r"k = 1 - \frac{Z_{front}}{z},\quad x' = c_x + f\frac{x}{z} + (vp_x - c_x)\,k")

with tab_about:
    st.write("Mini project: One-Point Perspective Virtual Room Designer.")
    st.write("Name: Rishav Chowdhury  |  Reg No.: 2411021060342")
