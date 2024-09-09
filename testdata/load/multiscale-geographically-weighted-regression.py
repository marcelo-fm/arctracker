# Run MGWR to predict house prices using "Number of Neighbors" and "Golden Search"
# Import modules
import arcpy

# Set the current workspace
arcpy.env.workspace = "C:/data"

# Run MGWR 
arcpy.stats.MGWR("r\data.gdb\house_price", "price", "CONTINUOUS", 
                 "review;beds;areas", r"data.gdb\house_price_fit_model", 
                 "DISTANCE_BAND", "GOLDEN_SEARCH", None, None, None, None, 
                 None, None, None, None, None, None, None, None, None, 
                 "review # #;beds # #; areas # #", None, None, 
                 r"data.gdb\house_price", "review review;beds beds; areas areas", 
                 r"data.gdb\house_price_prediction", "ROBUST", "BISQUARE")