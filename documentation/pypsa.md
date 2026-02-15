# Notes for Static Power Grid Simulation using PyPSA

Based on [youtube class by Dr. Bogdan Dobrica.](https://www.youtube.com/watch?v=fJBC-QfNSAM&t=1060s)

### Voltage in an AC Power

Here is your content in Markdown format:


## Power Grid

- Power grid is a network (can be represented as a graph)
    - A graph node = power grid bus
    - edges = power grid lines / transformers

- A bus is a node at which several components of the power system are connected, like generators, loads, transformers 

- Buses enforce energy and charge conservation laws

- A bus has 4 parameters: 
  - $|V|$ – the amplitude of the voltage;
  - $\phi$ – the phase angle of the voltage;
  - $P = \operatorname{Re}(\tilde{S})$ – the real power;
  - $Q = \operatorname{Im}(\tilde{S})$ – the reactive power.

- Generator bus has at least one generator connected to it
- Load bus has no generators connected to it
- Slack bus injects or absorbs power and is not real but is used in load flow studies to simulate losses that are not known in advance for the system, it is choses arbitrarily for buses that have no load and at least one generator

## Defining a power grid in PyPSA

- The object is called `pypsa.Network`

| argument            | type              | unit  | default | description                              |
|---------------------|-------------------|-------|---------|------------------------------------------|
| name                | string            | -     | -       | unique name                              |
| snapshots           | list / pd.Index   | -     | ['now'] | List of time "moments"                   |
| snapshot_weightings | pd.DataFrame      | hours | 1       | How long is a time "moment"              |
| now                 | any               | -     | 'now'   | Current time "moment"                    |
| srid                | integer           | -     | 4326    | Spatial Reference System Identifier      |

- can use `dir(grid)`

## Defining buses in PyPSA

- Use `pypsa.Network.add(class_name='Bus')`

| argument       | type            | unit  | default | description                                         |
|----------------|-----------------|-------|---------|-----------------------------------------------------|
| name           | string          | -     | -       | unique name                                         |
| v_nom          | float           | kV    | 1       | Nominal voltage                                     |
| x              | float           | -     | 0       | Position in the SRID system (longitude)             |
| y              | Float           | -     | 0       | Position in the SRID system (latitude)              |
| carrier        | string          | -     | AC      | The carrier (‘AC’, ‘DC’, ‘heat’, ‘gas’ etc)         |
| unit           | string          | -     | None    | Unit for the bus carrier (usually `MW`)             |
| v_mag_pu_set   | string / Series | /unit | 1       | Voltage magnitude set point.                        |

- `v_mag_pu_set` is the Voltage magnitude set point, per unit of v_nom
- set point means the target voltage level (typically per-unit or a defined nominal value)
- `v_mag_pu_min` is the min of that set and the`v_mag_pu_max` is the maximum allowed for this
- x and y values are the equivalent of lat and long

## Bus admittance matrix

- A N x N matrix that shows a mathematical representation of an electrical network, relating nodal current injections to node voltages. It is a square matrix, often used in power systems for steady-state analysis, derived from applying Kirchhoff's Current Law at each node. 


The relationships between bus currents and bus voltages are defined by the nodal admittance matrix ($Y_{bus}$) or the nodal impedance matrix ($Z_{bus}$). 
The fundamental relationship is: $\mathbf{I}_{bus} = \mathbf{Y}_{bus} \mathbf{V}_{bus}$ 
Where: 

• $\mathbf{I}_{bus}$: Vector of current injections at each bus ($n \times 1$). 
• $\mathbf{Y}_{bus}$: Bus admittance matrix ($n \times n$). 
• $\mathbf{V}_{bus}$: Vector of bus voltages with respect to ground ($n \times 1$). [3, 4]  

Diagonal elements contain the sum of admittances connected to each bus