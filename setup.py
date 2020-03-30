import sys
from cx_Freeze import setup, Executable



setup(
    name="Jongho",
    version="1.0",
    description="wormhole_update_tool",
    author="60sec",
    executables=[Executable("wormhole_update_tool.py",base="Win32GUI")])