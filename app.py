import streamlit as st
import pandas as pd

from src.grid_definition import nonconvergent_sample_grid, convergent_grid_sample

st.title("First pypsa project")

model_list = ["convergent", "nonconvergent"]

result = st.selectbox("Select model to show and run", options=model_list)

st.info(f"Running model: {result}")

if result == "convergent":
    grid = convergent_grid_sample("Example")
else:
    grid = nonconvergent_sample_grid("Example")

with st.expander("Sim details"):
    st.write(grid)
    st.write(grid.buses)

    st.write(dir(grid))
    st.write(grid.lines)
    st.write(grid.transformers)
    st.write(grid.transformers['tap_ratio'])

    st.write(grid.generators)
    st.write(grid.loads)
    
st.info("running power flow sim")
st.info(grid.pf())
st.info("Power flow completed")

st.write(grid.lines)

st.write(grid.explore())