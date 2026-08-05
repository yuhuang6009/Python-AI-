import streamlit as st

# streamlit run 当前文件/可用Tab来选择

#设置页面的配置项
st.set_page_config(
    page_title="Streamlit 入门",
    page_icon="🧊",
    #布局
    layout="wide",#layout ("centered", "wide", or None)
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    #可指定连接
    menu_items={
        'Get Help': 'https://www.deepseek.com/',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "#这是一个Streamlit 入门的页面"
    }
)

#大标题
st.title("Streamlit 入门演示")
st.header("一级标题")
st.subheader("二级标题")

#段落文字-# 1. 普通文本
st.write("你好呀！这是 Streamlit 的 `st.write` 方法。")

# 2. 支持 Markdown
st.write("## 这是 Markdown 标题")
st.write("**加粗文字** 和 *斜体文字*")

#3.显示变量
name="小暖"
age=18
st.write(f"我叫{name},今年{age}岁了,很高兴认识你")

# 4. 显示图片
st.write("下面是一张图片:")
st.image("./prompt_图3_5pro.png")

# 5. 引入音频
st.audio("./resources/music.mp3")

#6. 引入视频
st.video("./resources/video.mp4")

#7. 展示logo
st.logo("resources/logo.png")

#8. 放置表格 #
data={ 
    "姓名": ["夜雨", "小暖", "黑猫"],
    "年龄": [20, 20, 3],
    "身份": ["主角", "AI 看板娘", "神秘生物"]
}

# 方法1：用 st.write（自动渲染成表格）
st.write("## 方法1:st.write")
st.write(data)

# 方法2：用 st.table（静态表格）
st.write("## 方法2:st.table")
st.table(data)

# 方法3：用 st.dataframe（可交互表格）
st.write("## 方法3:st.dataframe")
st.dataframe(data)

#具体样貌
""""
姓名    年龄    身份
夜雨     20     主角
小暖     20     AI看板娘
黑猫     3      神秘生物
"""
# 9. 分隔线
st.divider()
st.write("✨ 学会啦！`st.write` 几乎是万能的输出函数。")

#10 .输入输出
name=st.text_input("对了,你的名字叫什么呢✨:")
if st.button("确认名字"):
    st.write(f"哦，原来你叫{name}呀,好好听的名字！")

#输入密码
password=st.text_input("可以告诉我你的幸运数字串吗:",type="password")
if password:
    st.write(f"哦哦,是{password}")

#11.单选按钮
gender=st.radio("告诉我你的性别吧",["男","女","保密"],index=2) #index=2表示默认是保密   
st.write(f"你的性别是:{gender}")



