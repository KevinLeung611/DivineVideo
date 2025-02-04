from pathlib import Path

def get_videos(videos_path):
    video_files = []
    files = [f.name for f in Path(videos_path).iterdir() if f.is_file()]

    support_video_formats = ["mp4", "mkv", "avi", "wmv", "flv", "mov", "webm", "m4v", "m4a"]
    for f in files:
        video_suffix = f.split(".")[1]
        if len(video_suffix) == 0:
            continue

        if video_suffix not in support_video_formats:
            continue

        video_files.append(f)

    if len(video_files) == 0:
        raise FileNotFoundError("No video files found!")

    return video_files


if __name__ == "__main__":
    from common.path_constants import data_dir
    videos_path = f"{data_dir}/video/input"
    video_names = get_videos(videos_path)
    print(video_names)