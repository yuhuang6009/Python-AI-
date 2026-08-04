import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

print("和 DeepSeek 聊天开始啦，输入 q 退出")

while True:
    user_input = input("\n你: ")
    if user_input == "q":
        print("再见！")
        break
    
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": "你是一个友好的助手"},
            {"role": "user", "content": user_input},
        ],
        stream=False
    )
    
    print("AI:", response.choices[0].message.content)
