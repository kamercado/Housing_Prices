# House Price Prediction Project

## Group Members
- Correen Xilin He
- Hanh Le
- Jasmin Hong
- Jeremy Elam
- Kat Mercado

## Purpose
To predict house sale prices based on various features given in the datasets.

## Data Source
- **Ames, Iowa Dataset**: [Kaggle - House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- **Southern California Dataset**: Orange County Multi-Listing Services (MLS)

## Tools/Languages/Packages Used
- AWS
- Jupyter Notebook
- Python
- HTML/CSS
- Javascript
- Flask
- Scikit-learn
- Seaborn
- Pandas
- Numpy
- Pickle
- Matplotlib


## Methods
**Feature Engineering:** Using Pandas, the categorical data was converted to numerical data based on average sale price per category.

**Model Selection:** Given our y, "Sale Price," we chose a linear regression model to predict a continuous value based on multiple features.

**Model Training:** We used Seaborn to determine the features that had higher correlations to sale price. Using scikit-learn, we trained our model on the following features: 
*'MSZoning', 'LotFrontage', 'Neighborhood', 'OverallQual', '1stFlrSF', '2ndFlrSF', 'FullBath', 'KitchenQual','TotRmsAbvGrd', 'Fireplaces', 'GarageType', 'GarageCars', 'GarageArea','WoodDeckSF', 'OpenPorchSF'*.
 Our train and test was split 80/20. **Our R-squared score resulted in 0.82, with a root mean square error (RMSE) of 37,130.49.** The model was saved using Pickle.

**App Building:** Using Flask, we created an app route that the HTML form would call to process the values into our pickled model. In the same app file, we created an ROI calculator for investors.
