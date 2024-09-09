import arcpy
import ctypes
from arcpy import env

def enableDiagnostics(enable: bool = True):
  pro = arcpy.GetInstallInfo()['InstallDir']
  dll = ctypes.CDLL(f'{pro}/bin/DADFLib.dll')
  if enable:
    dll.EventLogEnable()
  else:
    dll.EventLogDisable()

def setLogLevel(level: int = 2):
  pro = arcpy.GetInstallInfo()['InstallDir']
  dll = ctypes.CDLL(f'{pro}/bin/DADFLib.dll')
  dll.EventLogSetLogLevel(level)

enableDiagnostics(True) #enable diagnostic logging
# Setting a log level (0 == error, 1 == warning, 2 == information, 3 == debug)
# will get that level and everything below it. 0 is only errors, 1 is warnings and errors etc.
setLogLevel(3) # Max diagnostic log level 

arcpy.CheckOutExtension("3D")
env.workspace = r"C:\data"
arcpy.ddd.FeaturesFromCityEngineRules(r"geometry.gdb\in_polygons", 
                                      "rules.rpk", 
                                      r"geometry.gdb\out_multipatches")