@echo off
chcp 65001

@echo 首次训练开始

call .\venv\python.exe train_ms.py

@echo 训练完毕，请按任意键关闭
call pause