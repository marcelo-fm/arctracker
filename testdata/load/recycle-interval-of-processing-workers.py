import arcpy

# Set the number of to be processed before stopping and starting new worker 
# processes to 5
arcpy.env.recycleProcessingWorkers = 5