import json

from model.srt import SRT
from common.json_encoder import JsonEncoder

def sanitize_srt_file(src_file_path) -> []:
    input_data = []
    with open(src_file_path, encoding="utf-8", mode="r") as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue
            input_data.append(line.strip())

    if len(input_data) == 0:
        return []

    srt_infos = []

    for i in range(0, len(input_data), 3):
        srt_info = SRT()

        srt_info.index = input_data[i]
        srt_info.duration = input_data[i + 1]
        srt_info.text = input_data[i + 2]

        srt_infos.append(srt_info)

    print(f"Sanitize srt file result: {json.dumps(srt_infos, cls=JsonEncoder)}")

    return srt_infos

def desanitize_srt_file(srt_data: [SRT], file_path):
    if len(srt_data) == 0:
        return

    with open(file_path, encoding="utf-8", mode="w") as f:
        for srt in srt_data:
            f.write(f"{srt.index}\n{srt.duration}\n{srt.text}\n\n")

if __name__ == "__main__":
    from common.path_constants import data_dir
    srt_path = f"{data_dir}/audio/output/DeepSeek.srt"
    sanitized_result = sanitize_srt_file(srt_path)

    srt_path = f"{data_dir}/audio/output/DeepSeek-d.srt"
    desanitize_srt_file(sanitized_result, srt_path)
