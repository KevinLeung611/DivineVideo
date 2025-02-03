import subprocess
from common.path_constants import data_dir
from utils import yaml_reader


def extract_audio():
    yaml_config = yaml_reader.load_config()

    video_file = f"{data_dir}/video/input/{yaml_config['video']['input']}"
    output_file = f"{data_dir}/audio/output/{yaml_config['video']['input'].split('.')[0]}.wav"

    try:
        print(f"Executing command: ffmpeg -i {video_file} -vn -acodec pcm_s16le -ar 44100 -ac 2 {output_file}")

        result = subprocess.run(
            ["ffmpeg", "-i", video_file, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "1", output_file, "-y"],
            check=True, capture_output=True, text=True)

        print(f"Executing args: {result.args}")
        print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_audio()
