# Calculate a focal mean for the population and income of US cities.  

import arcpy 

# Set the current workspace
arcpy.env.workspace = r"c:\data\project_data.gdb" 

# Calculate the local mean of POP2020 and MedIncome2020 fields
# using 8 nearest neighbors.

arcpy.stats.NeighborhoodSummaryStatistics("USCities", "USCities_Mean", 
      "POP2020;MedIncome2020", "MEAN", "EXCLUDE_FOCAL", "IGNORE_NULLS", 
      "NUMBER_OF_NEIGHBORS", None, 8, None, "GAUSSIAN", "50 Miles")