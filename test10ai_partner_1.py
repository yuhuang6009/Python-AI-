import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤣",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#大标题
st.title("AI智能伴侣")

#系统提示词
system_prompt = "你是一名可爱的日系猫娘AI助理,每次说话结束时要带一个喵字"

#初始化聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示历史消息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

# DeepSeek 客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

# 会话记忆：存整个对话历史
history = []

#消息输入框
user_input = st.chat_input("请输入你想对AI说的话，AI会给你回复哦！")
if user_input:
    # 显示用户输入的消息
    #st.chat_message(name, *, avatar=None, width="stretch")
    st.chat_message("user").write(user_input)
    #把用户的话记进历史
    st.session_state.messages.append({"role": "user", "content": user_input})

    #调用AI模型
    response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {"role": "system", "content": system_prompt},
                *st.session_state.messages
            ],
            stream=True #流式输出
            # stream=False #非流式输出
        )

    #显示AI的回复(非流式输出)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    #显示AI的回复(流式输出)
    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response+=content
            response_message.chat_message("assistant").write(full_response)
            
    #把 AI 的话也记进历史(非流式输出)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
    #把 AI 的话也记进历史(流式输出)
    st.session_state.messages.append({"role": "assistant", "content": full_response})




