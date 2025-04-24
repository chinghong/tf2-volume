# TF2 Volume Setter

A simple utility that automatically sets Team Fortress 2's volume to 5% when the game launches.

## Features
- Automatically detects when TF2 launches
- Sets initial volume to 5%
- Allows manual volume control afterwards
- Closes automatically after setting the volume

## Installation
1. Download the latest release
2. Run the executable before launching TF2

## Building from source
```bash
pip install -r requirements.txt
pyinstaller --onefile --name tf2_volume_setter tf2_volume.py