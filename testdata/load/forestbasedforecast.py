import arcpy
arcpy.env.workspace = "C:/Analysis"

# Run time series clustering to cluster counties by population value.
arcpy.stpm.TimeSeriesClustering("USA_County_Population_1969_2019.nc", 
           "POPULATION_SUM_ZEROS",
           "Analysis.gdb/USA_County_Population_TimeSeriesClustering",
           "VALUE", None, None, None, "CREATE_POPUP")

# Run forest-based forecast models on each time series cluster
arcpy.stpm.ForestBasedForecast("USA_County_Population_1969_2019.nc",
          "POPULATION_SUM_ZEROS", 
          "Analysis.gdb/USA_County_Population_ForestBasedForecast", 
          "USA_County_Population_ForestBasedForecast_cube.nc", 20, 
          None, 3, 100, None, None, 100, "VALUE", "NONE", "90%", 1,
          None, 10, None, "TIME_SERIES_CLUSTER", "POPULATION_SUM_ZEROS")