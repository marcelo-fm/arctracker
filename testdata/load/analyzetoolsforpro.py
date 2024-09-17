import arcpy

arcpy.ImportToolbox('c:/tools/scripts/mytools.tbx')
arcpy.management.AnalyzeToolsForPro('mytool_tools', 'c:/temp/analyze_report.txt')

print(arcpy.GetMessages(1))