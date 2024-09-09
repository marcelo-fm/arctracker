import arcpy
import os

# Define variables
inPDF = r'C:\Project\OGC_DDP.pdf'
outTIFF = r'C:\Project\TIFFs'

# Create PDFDocument Object from inPDF
pdf = arcpy.mp.PDFDocumentOpen(inPDF)

# Loop through each page in the PDF and create a name based on the page number
for page in range(1, pdf.pageCount+1):
    name = str(page) + ".tif"
    outTIFFpath = os.path.join(outTIFF, name)

    # Export each page to TIFF using 96 DPI, RGB color mode, and JPEG compression
    arcpy.conversion.PDFToTIFF(inPDF, outTIFFpath, '#', str(page), '#', '#', 96, 
                               'RGB_TRUE_COLOR', 'JPEG')

    # Build pyramids and calculate statistics on each output TIFF
    arcpy.management.BuildPyramidsandStatistics(outTIFF)

    print("Exported " + outTIFFpath)