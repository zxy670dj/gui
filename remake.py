import os
import json

IMPORTANT = "editor/important"

def remake():
    conf_path = os.path.join(IMPORTANT, "conf.json")
    dconf_path = os.path.join(IMPORTANT, "dconf.json")

    if not os.path.exists(conf_path):
        print("Missing dconf.json. Cannot restore config.")
        return

    if not os.path.exists(dconf_path):
        with open(dconf_path, 'r') as dconf_file:
            default_conf = json.load(dconf_file)
        
        with open(conf_path, 'w') as conf_file:
            json.dump(default_conf, conf_file, indent=4)

    else:
        print("Config file already exists. No need to remake.")