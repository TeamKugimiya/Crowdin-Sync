# Crowdin-Sync

## 轉換 BetterQuests

```sh
# 1. BetterQuest 的 DefaultQuests.json 路徑 
# 2. 輸出路徑，將會輸出於該資料夾 en_us.lang
python scripts/Transform.py {1} {2}

# 範例
python scripts/Transform.py temp/overrides/config/betterquesting/DefaultQuests.json Divine-Journey-2/
```

## 轉換 Lang 檔案到 Json

```sh
# 1. 模式 1 Lang2Json
# 2. Lang 檔案路徑
# 3. Json 輸出路徑

python scripts/Conventer.py {1} {2} {3}

# 範例
python scripts/Conventer.py 1 Divine-Journey-2/en_US.lang en_us.json

# 1. 模式 2 Json2Lang
# 2. Json 檔案路徑
# 3. Lang 輸出路徑

python scripts/Conventer.py {1} {2} {3}

# 範例
python scripts/Conventer.py 2 Divine-Journey-2/zh_tw.json zh_tw.lang
```
