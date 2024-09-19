#!/bin/bash

fyne-cross windows --tags=gui && cp fyne-cross/dist/windows-amd64/ArcTracker.exe.zip ./ArcTracker-gui.exe.zip
fyne-cross windows --console && cp fyne-cross/dist/windows-amd64/ArcTracker.exe.zip ./ArcTracker.exe.zip
