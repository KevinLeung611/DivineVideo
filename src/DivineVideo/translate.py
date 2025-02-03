import requests
import json
from common.json_encoder import JsonEncoder

from utils import sanitize_utils
from model.srt import SRT

def translate_srt(srts: [SRT]):
    translated_srts = []

    for srt in srts:
        url = "https://api.siliconflow.cn/v1/chat/completions"

        payload = {
            "model": "Qwen/Qwen2.5-7B-Instruct",
            "messages": [
                {
                    "role": "system",
                    "content": "将下文翻译成中文，尽量参考上下文。如果不好翻译，可以按照意思转译。单词如果出现拼写错误，可以纠正。不要额外添加无关的内容"
                },
                {
                    "role": "user",
                    "content": srt.text
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

        translated_srt = SRT(srt.index, srt.duration, f"{translated_text}\n{srt.text}")

        translated_srts.append(translated_srt)

    return translated_srts

if __name__ == "__main__":
    from common.path_constants import data_dir
    file_path = f"{data_dir}/audio/output/DeepSeek.srt"
    sanitized_result = sanitize_utils.sanitize_srt_file(file_path)
    translated_result = translate_srt(sanitized_result)
    print(json.dumps(translated_result, cls=JsonEncoder))
