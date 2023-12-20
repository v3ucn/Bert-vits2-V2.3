@echo off
chcp 65001

call .\venv\python.exe short_audio_transcribe.py --languages "CJE" --whisper_size medium

@echo 采样完毕，请按任意键继续
call pause