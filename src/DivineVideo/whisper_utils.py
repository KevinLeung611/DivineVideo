import subprocess

from utils import check_language_support
from utils import yaml_reader

__model = yaml_reader.load_config()["whisper"]["model"]
__language = yaml_reader.load_config()["whisper"]["language"]

# 检查输入的语言是否支持
check_language_support.check_language(__language)

def generate_audio_srt(audio_file, output_dir):
    """
    根据音频文件生成 subtitle 字幕文件
    audio_file: 音频文件路径
    output_dir: 输出文件路径
    """
    __output_format = "srt"
    generate_audio_with_format(audio_file, output_dir, __output_format)

def generate_audio_text(audio_file, output_dir):
    """
    根据音频文件生成 text 文本文件
    audio_file: 音频文件路径
    output_dir: 输出文件路径
    """
    __output_format = "txt"
    generate_audio_with_format(audio_file, output_dir, __output_format)

def generate_audio_with_format(audio_file, output_dir, output_format):
    """
    指定输出文件格式，根据音频文件生成语音文本
    """
    print(f"Executing whisper command: whisper {audio_file} --language {__language} --model {__model} -f {output_format} -o {output_dir}")

    try:
        cmd = ["whisper", audio_file, "--language", __language, "--model", __model, "-f", output_format, "-o", f"{output_dir}"]
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=False)

        for line in process.stdout:
            print(line)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stdout}")


if __name__ == "__main__":
    pass