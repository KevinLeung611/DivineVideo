import subprocess


def extract_audio(video_file, output_file):
    try:
        print(f"Executing command: ffmpeg -i {video_file} -vn -acodec pcm_s16le -ar 44100 -ac 2 {output_file}")

        result = subprocess.run(
            ["ffmpeg", "-i", video_file, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "1", output_file, "-y"],
            check=True, capture_output=True, text=True)

        print(f"Executing args: {result.args}")
        print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

