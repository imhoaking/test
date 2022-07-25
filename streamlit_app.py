from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.set_page_config(
    page_title="This is Hoaii_Zone",
    page_icon="👋",
)

st.write('# Welcome to Hoaii_Zone 👋👋')

st.sidebar.success("选择一个demo😊")

st.markdown(
    """
    
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    
    ### Want to learn more?
    -  ###### Check out [streamlit.io](https://streamlit.io)
    -  ###### Jump into our [documentation](https://docs.streamlit.io)
    
    ### About ME 
    - ###### work | TNU
    - ###### study | python 
"""
)
