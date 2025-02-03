import yaml
import os
import sys

from common.path_constants import root_dir

def load_config():
    config_path = f"{root_dir}/conf.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config

if __name__ == "__main__":
    config = load_config()
    print(config["video"]["input"])
