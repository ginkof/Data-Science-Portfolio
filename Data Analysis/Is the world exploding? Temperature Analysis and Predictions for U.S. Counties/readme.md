## Project Overview

Utilized Python and 'seasonal decompose'-approach on hourly meteorological data for years 1980-2019 for each county in the United States to analyze the change in time of temperature. Our analysis focuses on the TGW dataset (Jones, A. D., Rastogi, D., Vahmani, P., Stansfield, A., Reed, K., Thurber, T., Ullrich, P., & Rice, J. S. (2022) availale [here](https://www.osti.gov/biblio/1960548).

### Data
Data are organized as follows

* `FIPS`: FIPS code for the county 
* `T2`:  2-m temperature 
* `Q2`:  2-m water vapor mixing ra'o 
* `U10`: 10-m east-west wind speed 
* `V10`: 10-m north-south wind speed 
* `SWDOWN`: Downwelling shortwave radia've flux at the surface 
* `GLW`: Downwelling longwave radia've flux at the surface

We have 40 years (years 1980-2019). For every year, the above quantities are measured hourly. Therefore, we have 365*24 dataframes, each with 56045 rows.




## Notebooks

* In [data_preparation.ipynb](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Data%20Analysis/Is%20the%20world%20exploding%3F%20Temperature%20Analysis%20and%20Predictions%20for%20U.S.%20Counties/data_preparation.ipynb) we import the data and average over the location in order to reduce the dimensionality of the dataframe
* In [decompose.ipynb
](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Data%20Analysis/Is%20the%20world%20exploding%3F%20Temperature%20Analysis%20and%20Predictions%20for%20U.S.%20Counties/decompose.ipynb) we perform a seasonal decompose analysis to investigate potential patterns in the data


