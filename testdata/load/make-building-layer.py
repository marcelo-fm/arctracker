# Name: makebuildinglayer.py
# Description: Create a feature dataset

# Import system modules
import arcpy

# Set overwrite option
arcpy.env.overwriteOutput = True

# Make a building layer from a Dataset
arcpy.MakeBuildingLayer_management("C:/data/facilities/University.gdb/BuildingA",
                                   "Bld_A")

# Create a building Scene layer package
arcpy.CreateBuildingSceneLayerPackage_management(BLD_A, output_BLD_A.slpk)