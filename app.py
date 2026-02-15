import streamlit as st
import pandas as pd

from src.grid_definition import sample_grid

st.title("First pypsa project")

grid = sample_grid("Example")

st.write(grid)
st.write(grid.buses)

st.write(dir(grid))