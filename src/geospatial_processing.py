from urllib.request import urlretrieve
from pathlib import Path
from os.path import basename
from rasterio.plot import show
from atlite.gis import ExclusionContainer

import requests
import tempfile
import rasterio as rio
import numpy as np
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

GEOSPATIAL_PROCESSING = "Geospatial Processing"

PORTUGAL_FILE_URL = "https://tubcloud.tu-berlin.de/s/2oogpgBfM5n4ssZ/download/PORTUGAL-2013-01-era5.nc"
COUNTRY_SHAPES_URL = "https://tubcloud.tu-berlin.de/s/7bpHrAkjMT3ADSr/download/country_shapes.geojson"
CORINE_LAND_COVER_CLASSIFICATION_URL = "https://tubcloud.tu-berlin.de/s/Mw5dwbwdsDY8zfH/download/U2018_CLC2018_V2020_20u1-PT.tif"
GEBCO_URL = "https://tubcloud.tu-berlin.de/s/XoDpBcweJHmYKgF/download/GEBCO_2014_2D-PT.nc"

def temp_dir():
    stable_dir = Path(tempfile.gettempdir()) / "galvani_cache"
    stable_dir.mkdir(parents=True, exist_ok=True)
    return stable_dir

def get_and_store_file(file_url):
    file_name = basename(file_url)
    file_path = temp_dir() / "data" / file_name
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        data = requests.get(file_url)
        with open(file_path, 'wb') as f:
            f.write(data.content)
        st.info(f"{file_name} file saved to {file_path}")
        return
    st.info(f"{file_name} exists in {file_path}, not retrieving")
    

def show_map_projections(file_path):
    countries = gpd.read_file(file_path / basename(COUNTRY_SHAPES_URL)).set_index("name")
    fig1, ax = plt.subplots(1, 1, figsize=(10, 6))
    countries.plot(edgecolor="k", facecolor="lightgrey", ax=ax)
    
    crs = ccrs.Mollweide()
    fig2 = plt.figure()
    ax = plt.axes(projection=crs)
    countries.to_crs(crs).plot(edgecolor="k", facecolor="lightgrey", ax=ax)
    with st.expander(label="Map Projections"):
        st.pyplot(fig1)
        st.pyplot(fig2)
    

def show_land_cover_data(file_path):
    # land cover dataset
    clc = rio.open(file_path / basename(CORINE_LAND_COVER_CLASSIFICATION_URL))
    #this dataset has multiple bands
    band = clc.read(1)
    # st.write(band)
    # st.write(band.shape)
    # st.write(clc.crs)
    # st.write(clc.bounds)
    # st.write(clc.transform)
    fig, ax = plt.subplots()
    show(band, transform=clc.transform, cmap="tab20", ax=ax)
    with st.expander(label="Land Cover Dataset"):
        st.pyplot(fig)
        

def show_gebco(file_path):
    gebco = rio.open(file_path / basename(GEBCO_URL), driver="netcdf")
    countries = gpd.read_file(file_path / basename(COUNTRY_SHAPES_URL)).set_index("name")
    # read the GEBCO band (was incorrectly reading the CORINE dataset before)
    band = gebco.read(1)

    fig, ax = plt.subplots(figsize=(6, 8))

    # show raster first so we can draw country borders on top
    show(
        band,
        transform=gebco.transform,
        cmap="RdBu_r",
        ax=ax,
        vmin=-2000,
        vmax=2000,
        adjust=False,
    )

    # plot only Spain outline above the raster for visibility
    countries.loc[["ES"]].plot(ax=ax, facecolor="none", edgecolor="k", linewidth=0.8, zorder=2)

    plt.colorbar(ax.images[0], ax=ax, label="Elevation (m)")

    # limit view to the desired region (lon: -9.5 to -6, lat: 37 to 42)
    ax.set_xlim(-9.5, -6)
    ax.set_ylim(37, 42)

    with st.expander("GEBCO"):
        st.pyplot(fig)

def geospatial_processing_page():
    
    with st.expander("Data Status"):
        get_and_store_file(PORTUGAL_FILE_URL)
        get_and_store_file(COUNTRY_SHAPES_URL)
        get_and_store_file(CORINE_LAND_COVER_CLASSIFICATION_URL)
        get_and_store_file(GEBCO_URL)
    
    file_path = temp_dir() / "data"
    
    show_map_projections(file_path)
    show_land_cover_data(file_path)
    show_gebco(file_path)


