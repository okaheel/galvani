import streamlit as st
import pandas as pd

from src.grid_definition import grid_def_page, GRID_DEF
from src.geospatial_processing import geospatial_processing_page, GEOSPATIAL_PROCESSING

pages = [GRID_DEF, GEOSPATIAL_PROCESSING]

selected_page = st.selectbox("Select Page", pages)

if selected_page == GRID_DEF:
    grid_def_page()
elif selected_page == GEOSPATIAL_PROCESSING:
    geospatial_processing_page()