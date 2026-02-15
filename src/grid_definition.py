import pypsa

def sample_grid(name: str):
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
             x=47.603161,
             y=-122.331493)
    return grid