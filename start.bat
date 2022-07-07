@echo off

call %~dp0bot\venv\Scripts\activate

cd %~dp0bot

set TOKEN=your token

python common.py

pause