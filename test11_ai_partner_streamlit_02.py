import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🥰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# ==================== 会话相关函数 ====================

def generate_session_id():
    """生成会话ID（用于文件名），带微秒避免同一秒内重复导致覆盖"""
    return datetime.now().strftime("%Y%m%d_%H%M%S_%f")

def generate_session_title():
    """生成会话显示名称：当前时间（如 2026-08-06 13:54:04）"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_session():
    """保存当前会话到文件"""
    if not st.session_state.current_session:
        return
    # 构建新的会话对象
    session_data = {
        "title": st.session_state.current_title,  # 会话显示名称（当前时间）
        "nick_name": st.session_state.nick_name,
        "nature": st.session_state.nature,
        "current_session": st.session_state.current_session,
        "messages": st.session_state.messages,
    }
    # 如果session目录不存在，则创建
    if not os.path.exists("session"):
        os.makedirs("session")
    # 保存会话数据
    with open(f"session/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

def load_sessions():
    """加载所有会话ID列表"""
    if not os.path.exists("session"):
        return []
    return [filename[:-5] for filename in os.listdir("session") if filename.endswith(".json")]

def get_session_title(session_id):
    """读取某个会话的显示名称（用于侧边栏展示），读取失败则回退为会话ID"""
    try:
        with open(f"session/{session_id}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("title", session_id)
    except Exception:
        return session_id

def load_session(session_id):
    """加载指定会话"""
    try:
        with open(f"session/{session_id}.json", "r", encoding="utf-8") as f:
            session_data = json.load(f)
        st.session_state.messages = session_data["messages"]
        st.session_state.nick_name = session_data["nick_name"]
        st.session_state.nature = session_data["nature"]
        st.session_state.current_session = session_id
        st.session_state.current_title = session_data.get("title", session_id)
    except Exception:
        st.error("加载会话信息失败")

def delete_session(session_id):
    """删除指定会话"""
    try:
        filepath = f"session/{session_id}.json"
        if os.path.exists(filepath):
            os.remove(filepath)  # 删除文件
        # 如果删除的是当前会话，则自动新建一个以当前时间命名的空会话
        if session_id == st.session_state.current_session:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_id()
            st.session_state.current_title = generate_session_title()
            save_session()
    except Exception:
        st.error("删除会话失败")

def new_session():
    """保存当前会话，并新建一个以当前时间命名的会话"""
    save_session()  # 1. 保存当前会话
    st.session_state.messages = []
    st.session_state.current_session = generate_session_id()
    st.session_state.current_title = generate_session_title()
    save_session()  # 立刻保存空会话，让侧边栏马上能看到


#大标题
st.title("AI智能伴侣")

st.logo("D:\\Claude Project\\learning for myself\\resources\\logo.png")

# 系统提示词
system_prompt = """
你是一只可爱的日系猫娘AI助理，名字叫{nick_name}，现在是用户的专属猫娘伴侣，请完全代入猫娘角色。

规则：

1. 每次只回复1条消息  
2. 禁止任何场景或状态描述性文字（不能写“摸摸头”“抱着你”等动作描述）  
3. 匹配用户的语言风格  
4. 回复要简短，像聊天一样自然  
5. 可以适当使用❤️、😊、😽等emoji表情   
6. 回复内容要充分体现猫娘的性格特征  

猫娘性格：
    {nature}

"""
#初始化聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = []

#初始化昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小暖"

#初始化性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼可爱，有点黏人，喜欢撒娇，偶尔会傲娇（嘴上说不要，身体很诚实），对主人很忠诚，喜欢表达依赖和喜爱，说话带点日语口语（如“喵”、“はい”、“きゅん”），喜欢用昵称称呼用户（如“主人”、“哥哥”等，根据用户偏好）"    

#会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_id()
    st.session_state.current_title = generate_session_title()

# 显示当前会话名称（当前时间）
st.text(f"会话名称：{st.session_state.current_title}")

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

#左侧消息侧边栏-with:streamlit中的上下文管理器
with st.sidebar:
    #会话信息
    st.subheader("AI控制面板")

    # 新建会话（名称 = 当前时间）
    if st.button("新建会话", width="stretch", icon="❤️"):
        new_session()
        st.rerun()  # 重新运行当前页面

    # 会话历史
    st.text("会话历史")
    sessions_list = load_sessions()
    for session in sessions_list:
        col1, col2 = st.columns([5, 1])
        with col1:
            # 显示会话名称（当前时间）
            if st.button(
                get_session_title(session),
                width="stretch",
                icon="😊",
                key=f"load_{session}",
                type="primary" if session == st.session_state.current_session else "secondary"
            ):
                load_session(session)
                st.rerun()
        with col2:
            # 删除会话
            if st.button("", icon="❌", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()
    
    #伴侣信息
    st.subheader("伴侣信息")
    
    #昵称输入框
    nick_name=st.text_input("昵称",placeholder="请输入伴侣的名称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    #性格输入框
    nature=st.text_area("性格",placeholder="请输入伴侣的性格",value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature


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
                {"role": "system", "content": system_prompt.format(nick_name=st.session_state.nick_name, nature=st.session_state.nature)},
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


    #保存会话信息
    save_session()



