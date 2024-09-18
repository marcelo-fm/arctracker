# Import necessary packages
import numpy as np
import h5py

spatialStatsModel = h5py.File(r'C:/MyData/MySSMFile.ssm', 'r')

# Get a list of keys of the variables:
ls = list(spatialStatsModel.keys())

# Get the attributes of the model:
attrs = list(spatialStatsModel.attrs)

# Print all the datasets and attributes
print("The variables in the model:")
for k in ls:
     print("{}---{}, --- {}".format(k, spatialStatsModel[k][()],
                             type(spatialStatsModel[k][()])))

print("The attributes in the model:")
for k in attrs:
     print("{}---{}, --- {}".format(k, spatialStatsModel.attrs.get(k),
                             type(spatialStatsModel.attrs.get(k))))

# Close the .ssm file
spatialStatsModel.close