
# Predicting Housing Prices

This repository contains code and associated files for creating an algoritm to for predicting housing prices via (un)supervised machine learning techiniques

### Project Overview

The project involves building a model to predict house prices based on their characteristics. It is divided into two phases: a **classification** task to determine if a house is expensive or not, and a **regression** task to predict the exact price. The project follows a typical machine learning workflow, including understanding the context, exploring and cleaning the data, pre-processing the data, training the models, and evaluating their performance. The goal is to provide clients with reliable and efficient predictions to assist in their decision-making process.

### Notebooks
This project notebooks can be found in the [classification](https://github.com/ginkof/Data-Science-Portfolio/tree/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/Classification) and [regression](https://github.com/ginkof/Data-Science-Portfolio/tree/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/Regression) folders. Here the tasks of feature engineering, model training and testing are performed.

#### Classification
* [1_Model_housing.ipynb](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/Classification/1_Model_housing.ipynb): we start with a "dummy" model to get an intuition. Later we use a decision tree classifier, which is later perfected by means of grid search method and pipeline.
* [2_Model_housing_Categorical.ipynb](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/Classification/2_Model_Housing_Categorical.ipynb): here we deal with categorical features using `OneHotEncoder`.
* [3_Model_Housing_complete.ipynb](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/Classification/3_Model_Housing_complete.ipynb): here we put all together in a pipeline able to deal with all kinds of features, namely numerical, (un)ordered categorical.

#### Regression
* [diamonds_intro_regression.ipynb](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/Regression/diamonds_intro_regression.ipynb): walkthrough solution on the Seaborn datased about diamond to get familiar with the regression techniques (linear regression)
* In [models_testing.ipynb](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/Regression/models_testing.ipynb) we apply decision tree and random forest regressors to our housing dataset
* In [Model testing and feature selection.ipynb](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/Regression/Model%20testing%20and%20feature%20selection.ipynb) we test the R^2 score and the RMSE for several model, applying various feature selections (Kbest, RFE, Variance Threshold)

### Data
The data can be found in [data](https://github.com/ginkof/Data-Science-Portfolio/tree/main/Machine%20Learning/Classification%20%26%20Regression/Predicting%20Housing%20Prices/data) and are organized according to the following features: 
* LotFrontage: Linear feet of street connected to property
* LotArea: Lot size in square feet
* TotalBsmtSF: Total square feet of basement area
* BedroomAbvGr: Bedrooms above grade (does NOT include basement bedrooms)
* Fireplaces: Number of fireplaces
* PoolArea: Pool area in square feet
* GarageCars: Size of garage in car capacity
* WoodDeckSF: Wood deck area in square feet
* ScreenPorch: Screen porch area in square feet
For the categorical dataset we have the following additional features:
* SZoning: Identifies the general zoning classification of the sale.
		
       A	Agriculture
       C	Commercial
       FV	Floating Village Residential
       I	Industrial
       RH	Residential High Density
       RL	Residential Low Density
       RP	Residential Low Density Park 
       RM	Residential Medium Density

* Condition1: Proximity to various conditions
	
       Artery	Adjacent to arterial street
       Feedr	Adjacent to feeder street	
       Norm	Normal	
       RRNn	Within 200' of North-South Railroad
       RRAn	Adjacent to North-South Railroad
       PosN	Near positive off-site feature--park, greenbelt, etc.
       PosA	Adjacent to postive off-site feature
       RRNe	Within 200' of East-West Railroad
       RRAe	Adjacent to East-West Railroad

* Heating: Type of heating
		
       Floor	Floor Furnace
       GasA	Gas forced warm air furnace
       GasW	Gas hot water or steam heat
       Grav	Gravity furnace	
       OthW	Hot water or steam heat other than gas
       Wall	Wall furnace

* Street: Type of road access to property

       Grvl	Gravel	
       Pave	Paved

* CentralAir: Central air conditioning

       N	No
       Y	Yes

* Foundation: Type of foundation
		
       BrkTil	Brick & Tile
       CBlock	Cinder Block
       PConc	Poured Contrete	
       Slab	Slab
       Stone	Stone
       Wood	Wood
