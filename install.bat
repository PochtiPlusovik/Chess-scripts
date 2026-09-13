@echo off

python -m venv PythonChess

call PythonChess\Scripts\activate.bat

python -m pip install -r requirements.txt

pause
