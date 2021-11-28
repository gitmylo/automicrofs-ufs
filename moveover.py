# move files from this directory over to micro:bit

import os.path as path
import os
import microfs as mfs

for root, dirs, files in os.walk("./"):
    for file in files:
        file = root+"\\"+file
        if path.basename(file) != path.basename(__file__) \
                and not root.startswith("./venv") \
                and not root.startswith("./.idea"):
            print("Uploading {directoryprint}...".format(directoryprint=file))
            mfs.put(file)
            print("Uploaded {directoryprint}!".format(directoryprint=file))
