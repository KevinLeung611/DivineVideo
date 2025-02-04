import os

import audio_extraction
import merge_subtitle
import translate
import whisper_utils
from common.path_constants import data_dir
from utils import check_video_file
from utils import sanitize_utils

video_input_name = check_video_file.get_videos(f"{data_dir}/video/input")[0]
file_base_name = video_input_name.split(".")[0]

video_input = os.path.join(data_dir, "video", "input", video_input_name)
video_output = os.path.join(data_dir, "video", "output", video_input_name)

audio_input = os.path.join(data_dir, "audio", "input", file_base_name + ".wav")
audio_output = os.path.join(data_dir, "audio", "output", file_base_name + ".wav")

srt_input = os.path.join(data_dir, "srt", "input", file_base_name + ".srt")
srt_output = os.path.join(data_dir, "srt", "output", file_base_name + ".srt")

audio_extraction.extract_audio(video_input, audio_input)

whisper_utils.generate_audio_srt(audio_input, os.path.join(data_dir, "srt", "input"))

sanitized_result = sanitize_utils.sanitize_srt_file(srt_input)

translated_srt = translate.translate_srt(sanitized_result)

translate.generate_tranlated_srt(translated_srt, srt_output)

merge_subtitle.merge_subtitle(srt_output, video_input, video_output)

print("All done!")