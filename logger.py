import os
import json
from datetime import datetime
from typing import Literal

CONFIG_PATH = "editor/config.json"
LOG_PATH = "editor/logs"
GENERAL_LOG = LOG_PATH + "/app.log"
ERROR_LOG = LOG_PATH + "/error.log"
DEBUG_LOG = LOG_PATH + "/debug.log"

log_entries = []

def load_config():
    if not os.path.exists(CONFIG_PATH):
        print("Config file not found.")
        return None

    with open(CONFIG_PATH, 'r') as config_file:
        return json.load(config_file)

def log(message:str, level:Literal["INFO", "ERROR", "DEBUG"]) -> None:
    config = load_config()
    if not config:
        print("Unable to load config. Logging aborted.")
        return

    max_logs = config.get("max_logs", 1000)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    log_entries.append(log_entry)


    with open(GENERAL_LOG, 'a') as general_log:
        general_log.write(log_entry)

    if level == "ERROR":
        with open(ERROR_LOG, 'a') as error_log:
            error_log.write(log_entry)
    elif level == "DEBUG":
        with open(DEBUG_LOG, 'a') as debug_log:
            debug_log.write(log_entry)

    if len(log_entries) > max_logs:
        log_entries.pop(0)