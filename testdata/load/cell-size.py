import arcpy

# Set the cell size environment using a keyword.
arcpy.env.cellSize = "MINOF"

# Set the cell size environment using a number.
arcpy.env.cellSize = 20

# Set the cell size environment using a raster dataset.
arcpy.env.cellSize = "C:/sapyexamples/data/myraster"