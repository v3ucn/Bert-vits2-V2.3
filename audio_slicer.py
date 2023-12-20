import librosa  # Optional. Use any library you like to read audio files.
import soundfile  # Optional. Use any library you like to write audio files.

import shutil
import gradio as gr
import os
import webbrowser
import subprocess
import datetime
import json
import requests
import soundfile as sf
import numpy as np
import yaml
from config import config
import os

with open('config.yml', mode="r", encoding="utf-8") as f:
    configyml=yaml.load(f,Loader=yaml.FullLoader)


model_name = configyml["dataset_path"].replace("Data/","")



from slicer2 import Slicer

audio, sr = librosa.load(f'./Data/{model_name}/raw/{model_name}.wav', sr=None, mono=False)  # Load an audio file with librosa.
slicer = Slicer(
    sr=sr,
    threshold=-40,
    min_length=2000,
    min_interval=300,
    hop_size=10,
    max_sil_kept=500
)
chunks = slicer.slice(audio)
for i, chunk in enumerate(chunks):
    if len(chunk.shape) > 1:
        chunk = chunk.T  # Swap axes if the audio is stereo.
    soundfile.write(f'./Data/{model_name}/raw/{model_name}_{i}.wav', chunk, sr)  # Save sliced audio files with soundfile.

if os.path.exists(f'./Data/{model_name}/raw/{model_name}.wav'):  # 如果文件存在
    os.remove(f'./Data/{model_name}/raw/{model_name}.wav')  