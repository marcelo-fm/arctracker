import os
import re
folder = os.path.basename(os.path.dirname(inData))
folder = re.sub('[^0-9a-zA-Z]+', '_', folder)
if folder[0].isdigit():
    folder = "_" + folder