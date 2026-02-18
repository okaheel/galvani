# Notes for Energy System Modelling Lectures

Class on youtube by Fabian Neumann: [here](https://www.youtube.com/watch?v=BqvbdtDrW7g&list=PL9_USGH2eQEOpSeN9kf-7Q8hfIC7MFa4J)

## Lecture 1

- Global wind atlas can be used for wind power density modeling
- Global solar atlas shows the solar potential
- Renewables ninja provides time series data for Solar PV, wind, heating and cooling, and weather
- Global Energy monitor provides fantastic data for research related work on all aspects of energy [here](https://globalenergymonitor.org/projects/private-equity-tracker/)

## Lecture 2

- Try running cases with https://model.energy/
- If you take a demand/load curve (hourly) across a year and reformat it/sort it by the scalar values you get a load duration curve (which shows the percentage of the year, the demand is above a certain value)
-We can use fourier analysis tp decompose a periodic signal into simpler sine waves
    - Every periodic signal can be broken down into a sum of sine waves with different frequencies and amplitudes
    -FFT is helpful for this
- Onshore wind is much more variable than offshore and solar, and there are some what seasonal patterns
- There are weekly or 'synoptic' weather patters that could appear in wind on shore patterns
- Offshore wind has higher and steadier capacity factors than onshore wind
- Open energy prices is a good source of information https://openenergytracker.org/en/
- We can look at time series correlation between two independent time series via the pearson correlation
![alt text](images/timeseries_correlation.png)

## Workshop #1,2,3

- Python, numpy and pandas intro

https://www.youtube.com/watch?v=c1HyDcuD2zM&list=PL9_USGH2eQEOpSeN9kf-7Q8hfIC7MFa4J&index=2

https://fneum.github.io/data-science-for-esm/dsesm/workshop-python/





## Open mod lecture to follow later
https://www.youtube.com/watch?v=Acl5gonFMx4
https://www.youtube.com/watch?v=igGdc3UTj-Q