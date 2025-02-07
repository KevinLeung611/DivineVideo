import json

import requests

from model.srt import SRT
from utils import sanitize_utils
from utils import yaml_reader
from utils.check_language_support import check_language

src_lang = yaml_reader.load_config()["language"]["src_lang"]
src_lang = 'en' if not src_lang else src_lang

check_language(src_lang)

target_lang = yaml_reader.load_config()["language"]["target_lang"]
target_lang = 'zh' if not target_lang else target_lang

check_language(target_lang)

def translate_srt(srts: [SRT]):
    translated_srts = []

    for srt in srts:
        translated_text = translate(srt.text)

        translated_srt = SRT(srt.index, srt.duration, f"{translated_text}\n{srt.text}")

        translated_srts.append(translated_srt)

    return translated_srts

def translate(text):
    print(f"Original sentence: {text}")

    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": f"You are a professional subtitle translator and language consultant. Translating the following text from {src_lang} to {target_lang} simply and only return the translation. if target language is chinese, use simplified Chinese."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    }
    headers = {
        "Authorization": "Bearer sk-pwnyrdnbibbzswbntetohoydlwbetknqzlrkigimzzrmyifi",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    translated_text = json.loads(response.text)["choices"][0]["message"]["content"]

    print(f"Tranlated sentence: {translated_text}")

    return translated_text


def generate_tranlated_srt(translated_srts: [SRT], file_path):
    sanitize_utils.desanitize_srt_file(translated_srts, file_path)

if __name__ == "__main__":
    from common.path_constants import data_dir
    file_path = f"{data_dir}/srt/output/DeepSeek R1 Explained to your grandma.srt"
    sanitized_result = sanitize_utils.sanitize_srt_file(file_path)
    translated_result = translate_srt(sanitized_result)
    # generate_tranlated_srt(translated_result, file_path)