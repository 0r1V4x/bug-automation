import PyInstaller.__main__
import os
import sys

# Package as single executable
PyInstaller.__main__.run([
    'bountyhunter.py',
    '--name=BountyHunterPro',
    '--onefile',
    '--windowed',
    '--icon=icon.ico',
    '--add-data=assets;assets',
    '--hidden-import=customtkinter',
    '--hidden-import=PIL',
    '--hidden-import=requests',
    '--hidden-import=aiohttp',
    '--clean'
])
