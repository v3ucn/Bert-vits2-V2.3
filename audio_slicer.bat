@echo off
chcp 65001

call .\venv\python.exe audio_slicer.py

@echo 切分完毕，请按任意键继续
call pause