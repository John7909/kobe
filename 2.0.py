import random
import time
import sys
import os

# ================= 配置区域 =================
DATA_FILE = "data.txt"  # 确保你的废话库文件名是这个

# 科比语录库（保留在代码里，保证随时能看鸡汤）
kobe_quotes = [
    "你见过凌晨四点的洛杉矶吗？",
    "总有人要赢的，为什么不能是我？",
    "Mamba Out.",
    "即使世界抛弃了你，可世界还是你的。",
    "第二名只能说明你是头号输家。",
    "爱我或者恨我，两者必有其一。"
]

# 表情库，让机器人回复更生动
emojis = ["🏀", "🐍", "🚁", "🤡", "🤔", "😎", "🔥", "👻", "🤖", "💬"]

# ================= 核心逻辑 =================
def load_data(filename):
    """正在加载废话库"""
    if not os.path.exists(filename):
        print(f"找不到 {filename} 文件！")
        return ["错误：未找到data.txt"]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # 读取所有行，去除空白，过滤掉空行
            lines = [line.strip() for line in f.readlines() if line.strip()]
            print(f"成功加载了 {len(lines)} 条废话/梗！")
            return lines
    except Exception as e:
        print(f"读取文件出错：{e}")
        return []

# 启动时加载数据
meme_list = load_data(DATA_FILE)

def main():
    print("=" * 30)
    print("科比机器人2.0已启动")
    print("=" * 30)
    
    while True:
        print("\n请输入指令(k/c/e)：")
        print("[K] - 听听老大的教诲")
        print("[C] - 聊聊那个梗 (现代抽象废话)")
        print("[E] - 退出程序")
        
        choice = input(">>> ").strip().upper()

        # 随机选一个表情
        random_emoji = random.choice(emojis)

        if choice == 'K':
            print(f"\n老大语录 {random_emoji}：")
            print(f"\"{random.choice(kobe_quotes)}\"")
            time.sleep(0.5)  # 假装思考

        elif choice == 'C':
            if meme_list:
                print(f"\n科比: {random_emoji}：")
                print(f">>> {random.choice(meme_list)}")
            else:
                print("快去写 data.txt！")

        elif choice == 'E':
            print("\nMan! Out!")
            break
        
        else:
            print(f"\n输入错误 {random_emoji}")

if __name__ == "__main__":
    main()
