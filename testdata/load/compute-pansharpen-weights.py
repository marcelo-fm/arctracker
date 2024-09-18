#Compute the pansharpening weights and use the results in the 
#create pansharpening tool.

try:
    import arcpy
    
    InRGBraster = "C:\\temp\\rgb.img"
    InPanraster = "C:\\temp\\pan.tif"
    
    #Compute Pan Sharpen Weights  
    out_pan_weight = arcpy.ComputePansharpenWeights_management(
        InRGBraster, InPanraster, "3 2 1 4")
    
    #Get results 
    pansharpen_weights = out_pan_weight.getOutput(0)
    
    #Split the results string for weights of each band
    pansplit = pansharpen_weights.split(";")
    
    #Run the Create pan sharpened raster dataset tool. 
    arcpy.CreatePansharpenedRasterDataset_management(
        InRGBraster, "3", "2", "1", "4", "C:\\temp\\pansharpened_raster.tif",
        InPanraster, "Gram-Schmidt", pansplit[0].split(" ")[1],  
        pansplit[1].split(" ")[1], pansplit[2].split(" ")[1],
        pansplit[3].split(" ")[1])
    
except arcpy.ExecuteError:
    print(arcpy.GetMessages())
except Exception as err:
    print(err[0])