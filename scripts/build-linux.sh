#!/bin/bash

fyne-cross linux --tags=gui && cp fyne-cross/dist/linux-amd64/ArcTracker.tar.xz ./ArcTracker-gui.tar.xz
fyne-cross linux && cp fyne-cross/dist/linux-amd64/ArcTracker.tar.xz ./.
