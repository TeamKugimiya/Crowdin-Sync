import json
import os
import sys

# Convent by ChatGPT
# Credit: Nomifactory

local_prefix = "divine_journey_2.quest."
data = {}

def flat(cur, pre):
    return pre + cur


def escape_string(origin):
    return origin.replace("\n", "%n")


def edit_key(db_name, key_name):
    r = []
    db = data[db_name]
    keys = list(db.keys())

    for key in keys:
        store_key_name = key.replace(":10", "")

        prefix = f"{local_prefix}{key_name}.{store_key_name}"
        props = db[key]["properties:10"]["betterquesting:10"]

        r.append(f"# {key_name} {store_key_name}")
        r.append(f"{prefix}.title={escape_string(props.get('name:8', props.get('name:8', '')))}")
        r.append(f"{prefix}.desc={escape_string(props.get('desc:8', ''))}")
        r.append("")

        props["name:8"] = f"{prefix}.title"
        props["desc:8"] = f"{prefix}.desc"

    return r


def mkdirp(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        pass
    except FileNotFoundError:
        mkdirp(os.path.join(dir, ".."))


def transform_file(file, lang_file):
    def transform():
        global data
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        lines = flat(edit_key("questDatabase:9", "db"), edit_key("questLines:9", "line"))
        text = "\n".join(lines)

        mkdirp(lang_file)

        with open(os.path.join(lang_file, "en_US.lang"), "w", encoding="utf-8") as f:
            f.write(text)

        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    return transform


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("錯誤！")
        print("用法：python Transform.py BetterQuest的路徑（DefaultQuests.json） 輸出路徑資料夾")
        sys.exit()
    quest_location = sys.argv[1]
    lang_file_location = sys.argv[2]

    transform = transform_file(quest_location, lang_file_location)
    transform()
