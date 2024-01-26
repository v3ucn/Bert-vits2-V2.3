import librosa
import soundfile as sf
import os
import yaml

# 假定Slicer类定义在slicer2.py文件中
from slicer2 import Slicer  

# 加载配置文件
with open('config.yml', mode="r", encoding="utf-8") as f:
    configyml = yaml.load(f, Loader=yaml.FullLoader)

model_name = configyml["dataset_path"].replace("Data/", "")

audio_folder = f'./Data/{model_name}/raw/'
index = 0  # 初始化全局索引

for filename in os.listdir(audio_folder):
    if filename.endswith('.wav'):
        # 加载音频文件
        audio_path = os.path.join(audio_folder, filename)
        audio, sr = librosa.load(audio_path, sr=None, mono=False)

        # 使用加载的音频文件的采样率初始化Slicer对象
        slicer = Slicer(sr=sr, threshold=-40, min_length=2000, min_interval=300, hop_size=10, max_sil_kept=500)

        # 切割音频文件
        chunks = slicer.slice(audio)
        for chunk in chunks:
            if len(chunk.shape) > 1:
                chunk = chunk.T  # 如果音频是立体声的，交换轴
            # 保存切割后的音频文件，使用全局索引
            output_filename = f'{model_name}_{index}.wav'
            sf.write(os.path.join(audio_folder, output_filename), chunk, sr)
            index += 1  # 更新索引

        # 删除原始音频文件
        os.remove(audio_path)
