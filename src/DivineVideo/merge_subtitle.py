import subprocess

def merge_subtitle(srt_file, input_video, output_video):
    cmd = ["ffmpeg", "-i", input_video, "-vf", f"subtitles={srt_file}:force_style='FontName=Yuanti SC,FontSize=12,PrimaryColour=&HFFFFFF,Outline=1,OutlineColour=&H000000'", "-c:a", "copy", output_video, "-y"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, text=True)
    for line in process.stdout:
        print(line)
