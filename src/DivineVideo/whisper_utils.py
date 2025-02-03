import subprocess

from common.path_constants import data_dir
from utils import yaml_reader

audio_file_name = yaml_reader.load_config()['video']['input'].split('.')[0]

def generate_audio_srt(audio_file, output_dir):
    model = yaml_reader.load_config()["whisper"]["model"]
    language = yaml_reader.load_config()["whisper"]["language"]
    output_format = yaml_reader.load_config()["whisper"]["output_format"]

    print(f"Executing whisper command: whisper {audio_file} --language {language} --model {model} -f {output_format} -o {output_dir}")

    try:
        cmd = ["whisper", audio_file, "--language", language, "--model", model, "-f", output_format, "-o", f"{output_dir}"]
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=False)

        for line in process.stdout:
            print(line)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stdout}")


if __name__ == "__main__":
    audio_file = f"{data_dir}/audio/output/{audio_file_name}.wav"
    generate_audio_srt(audio_file)
