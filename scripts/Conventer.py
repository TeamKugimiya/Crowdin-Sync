import json
import sys

# Made by ChatGPT

def parse_lang_file(lang_file):
    data = {}
    with open(lang_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('=')
            if len(parts) >= 2:
                key = parts[0].strip()
                value = '='.join(parts[1:]).strip()
                data[key] = value
            else:
                print(f"警告：跳過不符合格式的行：{line}")
    return data

def save_as_json(lang_data, json_file):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(lang_data, file, ensure_ascii=False, indent=2)

def parse_json_file(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_as_lang(lang_data, lang_file):
    with open(lang_file, 'w', encoding='utf-8') as file:
        for key, value in lang_data.items():
            file.write(f"{key}={value}\n")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("錯誤！")
        print("用法：")
        print("python Conventer.py 模式ID（Lang2Json:1｜Json2Lang:2） （1: Lang 檔案路徑｜2: Json 檔案路徑） （1: Json 檔案路徑｜2: Lang 檔案路徑）")
        sys.exit()

    mode = sys.argv[1]

    match mode:
        case "1":
            lang_file = sys.argv[2]
            json_file = sys.argv[3]
            lang_data = parse_lang_file(lang_file)
            save_as_json(lang_data, json_file)
            print(f"轉換完成，資料已儲存到 {json_file}")
        case "2":
            json_file = sys.argv[2]
            lang_file = sys.argv[3]
            lang_data = parse_json_file(json_file)
            save_as_lang(lang_data, lang_file)
            print(f"轉換完成，資料已儲存到 {lang_file}")
        case _:
            print("錯誤！")
