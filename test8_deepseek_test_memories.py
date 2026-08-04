# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
print("和AI猫娘聊天开始了/输入bye退出")
history=[]
while True:
    user_input=input("你：")
    if user_input=="bye":
        print("再见，喵~")
        break
    if user_input=="clear":
        history.clear()
        print("记忆已清空")
        continue
    
    history.append({"role": "user", "content": user_input}) # 记 用户 的话

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": "你是一名可爱的日系猫娘AI助理,每次说话结束时要带一个喵字"},
            {"role": "user", "content": user_input},
        ]+history,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    ai_reply=response.choices[0].message.content
    print(ai_reply)
    history.append({"role":"assistant","content":ai_reply}) # 记 AI 的话