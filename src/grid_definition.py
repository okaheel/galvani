import pypsa
import streamlit as st

GRID_DEF = "Grid Definition"

def nonconvergent_sample_grid(name: str):
    grid = pypsa.Network(name=name)
    grid.add(class_name="Bus", name="Bus #1")
    # nominal voltage is 220
    # v_mag_pu_set Voltage magnitude set point, per unit of v_nom
    # set point means the target voltage level (typically per-unit or a defined nominal value)
    # v_mag_pu_min is the min of that set and the v_mag_pu_max is the maximum allowed for this 
    grid.add(class_name="Bus",
             name="Household #2",
             v_nom=0.22,
             v_mag_pu_set=1,
             v_mag_pu_min = 0.95,
             v_mag_pu_max = 1.05,
            #  x=47.603161,
            #  y=-122.331493
            )
    
    grid.add(class_name="Line",
             name="Line #1",
             x = 0.01,
             r= 0.1,
             bus0='Bus #1',
             bus1='HouseHold #2')
    
    grid.remove(class_name='Line', name="Line #1")
    grid.add(class_name='Transformer',
             name='Transf. #1',
             bus0='Bus #1',
             bus1='HouseHold #2',
             tap_ratio=4.54,
             x=0.01,
             r=0.1)
    
    grid.add(class_name="Generator",
             name="Gen #1",
             bus='Bus #1',
             p_nom=0.01)
    
    grid.add(class_name='Load',
             name='Load #1',
             bus='HouseHold #2',
             p_set=0.095,
             q_set=0.005)
    return grid

def convergent_grid_sample(name: str):
    n_buses = 3
    grid_ok = pypsa.Network(name=name)

    for i in range(n_buses):
        grid_ok.add("Bus", "My bus {}".format(i),
                    v_nom=20)

    for i in range(n_buses):
        grid_ok.add("Line", "My line {}".format(i),
                    bus0="My bus {}".format(i),
                    bus1="My bus {}".format((i+1)%n_buses),
                    x=0.1,
                    r=0.01)

    grid_ok.add("Generator", "My gen",
                bus="My bus 0",
                p_set=100,
                control="PQ")

    grid_ok.add("Load", "My load",
                bus="My bus 1",
                p_set=100,
                q_set=100)
    return grid_ok

def grid_def_page():
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