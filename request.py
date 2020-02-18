import requests

url = 'http://localhost:5000/results'

r = requests.post(url,json={'MSZoning':1, 'LotFrontage':1,
       'Neighborhood':1, 'OverallQual':1, '1stFlrSF':1, '2ndFlrSF':1,
       'FullBath':1, 'KitchenQual':1,
       'TotRmsAbvGrd':1, 'Fireplaces':1, 'GarageType':1, 'GarageCars':1, 'GarageArea':1,
       'WoodDeckSF':1, 'OpenPorchSF':1})

print(r.json())