import random
import time
from deep_translator import GoogleTranslator

# 設定語言清單
languages = ['en', 'ja', 'zh-TW', 'fr', 'de', 'es', 'ko', 'it']

# 初始文本
text = "我數學會及格嗎"

print(f"原始文本: {text}\n")

for i in range(30):  # 你可以改成100次
    # 步驟 1: 隨機選擇一個源語言和一個目標語言
    source_lang = random.choice(languages)
    target_lang = random.choice(languages)

    # 確保源語言和目標語言不相同
    while source_lang == target_lang:
        target_lang = random.choice(languages)

    # 步驟 2: 執行接龍翻譯 (將結果丟給下一次循環)
    # 將當前文本從 source_lang 翻譯到 target_lang
    new_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)

    # === 關鍵修改：讓翻譯器自動偵測中文檢視的源語言 (source='auto') ===
    # 步驟 3: 將 "new_text" 額外翻譯回中文供查看 (結果不影響下一次循環)
    # 使用 'auto' 讓 deep_translator 自己判斷 new_text 的語言
    try:
        chinese_result = GoogleTranslator(source='auto', target='zh-TW').translate(new_text)
    except Exception as e:
        # 如果翻譯失敗，就直接顯示原始外語文本
        chinese_result = f"[翻譯失敗: {new_text}]"

    # 步驟 4: 打印信息
    # 打印接龍翻譯結果
    print(f"[{i}] {source_lang} -> {target_lang}: {new_text}")
    # 打印翻譯回中文的結果
    print(f"      (中文檢視): {chinese_result}\n")

    # 更新文本，用於下一次的接龍翻譯
    text = new_text

    time.sleep(0.5)  # 避免請求太快被擋

# 最後將接龍翻譯的最終結果轉回中文
final_text = GoogleTranslator(source='auto', target='zh-TW').translate(text)

print("="*40)
print(f"最終的接龍翻譯結果 (最後語言: {target_lang}): {text}")
print("最終結果翻譯回中文:", final_text)
print("="*40)
