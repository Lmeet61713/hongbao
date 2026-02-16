import streamlit as st
from PIL import Image
import os

# ------------------ 页面配置 ------------------
st.set_page_config(
    page_title="特别红包",
    page_icon="🧧",
    layout="wide",  # 宽屏布局
    initial_sidebar_state="collapsed"
)

# 自定义一些样式（让界面更温馨）
st.markdown("""
<style>
    .big-red {
        color: #e4393c;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
    }
    .section-title {
        color: #e4393c;
        font-size: 32px;
        border-bottom: 2px solid #f9e4b7;
        padding-bottom: 10px;
        margin: 30px 0 20px;
    }
    .blessing {
        background-color: #fff5e6;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        font-size: 24px;
        color: #e4393c;
        border: 2px solid #f9e4b7;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ------------------ 第一部分：红包封面 ------------------
st.markdown('<div class="big-red">🧨🧨🧧 特别红包 🧧🧨🧨</div>', unsafe_allow_html=True)

# 左右两列，左边放封面图片，右边放祝福语
col1, col2 = st.columns([1, 2])

with col1:
    # 封面图片（已改为相对路径，请将图片放入 images 文件夹）
    cover_image_path = "images/钟离.png"
    if os.path.exists(cover_image_path):
        cover_img = Image.open(cover_image_path)
        st.image(cover_img, width=250)
    else:
        st.warning("封面图片未找到，请检查 images/钟离.png 是否存在")

with col2:
    st.markdown('<div class="blessing">', unsafe_allow_html=True)
    st.markdown("### 新年快乐！")
    st.markdown("愿你马年行大运，天天开心，万事如意！")
    st.markdown("(上面的祝福语太lou了)")
    st.markdown("(我觉得你会喜欢下面这个)")
    st.markdown("🌠🌠🌠🌠🌠看到这一行10连3金🌠🌠🌠🌠🌠")
    st.markdown("✨✨✨<-三金")
    st.markdown("៷>ᴗ<៷ಣ")
    st.markdown("៷>ᴗ<៷ಣ")
    st.markdown("៷>ᴗ<៷ಣ")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ 第二部分：三个核心选项 ------------------
st.markdown('<div class="section-title">🎁 点开有惊喜 🎁</div>', unsafe_allow_html=True)

# 用三个按钮控制显示内容
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None

col_a, col_b, col_c = st.columns(3)
with col_a:
    if st.button("✨ 阳光彩虹小白马꒰ঌ(🌸>ワ<)໒꒱ ✨", use_container_width=True):
        st.session_state.selected_option = 1
with col_b:
    if st.button("🎬 十级社恐宅女ต ᳐ ᷇ᵕ  ᷆ ᳐ต੭ 🎬", use_container_width=True):
        st.session_state.selected_option = 2
with col_c:
    if st.button("📸 钟爱黄紫配衣裁缝女( *・ω・)✄ 📸", use_container_width=True):
        st.session_state.selected_option = 3

# 根据选中的选项显示内容
if st.session_state.selected_option == 1:
    st.subheader("选项一的内容")
    # 图片和视频（请放入对应文件夹）
    img_path1 = "images/风堇.jpg"
    video_path1 = "videos/风堇.mp4"

    col_img, col_vid = st.columns(2)
    with col_img:
        # 直接显示图片，不用 os.path.exists
        try:
            st.image(img_path1, caption="想我了吗？灰宝！🌈🌈🌈")
        except:
            st.info("图片显示失败，但文件应该存在")
    with col_vid:
        if os.path.exists(video_path1):
            st.video(video_path1)
        else:
            st.info("视频未找到，请检查 videos/风堇.mp4 是否存在")

elif st.session_state.selected_option == 2:
    st.subheader("选项二的内容")
    img_path2 = "images/遐蝶.jpg"
    video_path2 = "videos/遐蝶.mp4"

    col_img, col_vid = st.columns(2)
    with col_img:
        try:
            st.image(img_path2, caption="重新认识一下吧！我叫遐蝶(♡>𖥦<)/♥")
        except:
            st.info("图片显示失败，但文件应该存在")
    with col_vid:
        if os.path.exists(video_path2):
            st.video(video_path2)
        else:
            st.info("视频未找到，请检查 videos/遐蝶.mp4 是否存在")

elif st.session_state.selected_option == 3:
    st.subheader("选项三的内容")
    img_path3 = "images/阿格莱雅.png"
    video_path3 = "videos/阿格莱雅.mp4"

    col_img, col_vid = st.columns(2)
    with col_img:
        try:
            st.image(img_path3, caption="3000万世轮回救不了白厄的审美ᐡ•͈ ·̭ •͈ᐡ")
        except:
            st.info("图片显示失败，但文件应该存在")
    with col_vid:
        if os.path.exists(video_path3):
            st.video(video_path3)
        else:
            st.info("视频未找到，请检查 videos/阿格莱雅.mp4 是否存在")

# 可以加一个分隔线
st.markdown("---")

# ------------------ 第三部分：宝藏收藏家（结语） ------------------
st.markdown('<div class="section-title">💖 宝藏收藏家 💖</div>', unsafe_allow_html=True)

# 这里可以放多张图片，例如用三列显示
recall_images = [
    "images/fll.jpg",
    "images/fnn.jpg",
    "images/小卡.jpg",
    "images/白厄.jpg",
    "images/长夜月.png",
    "images/昔涟.png",
]
recall_captions = [
    "想喝糖福禄和coko可乐嘛？想？那你就等着吧，哼~",
    "你也觉得小蛋糕很好吃对吧！✨(☆▽☆)✨",
    "义人！请停止你这危险的想法！vo(≧口≦)o",
    "搭档！我们一起去训练吧~🔪🔪",
    "我才不是傻不啦叽的(￣﹃￣)",
    "嘘~˶ᵒ ᵕ ˂˶  ಣ"
]
# 每行显示3张图片
cols = st.columns(3)
for i, img_path in enumerate(recall_images):
    with cols[i % 3]:
        if os.path.exists(img_path):
            img = Image.open(img_path)
            caption = recall_captions[i] if i < len(recall_captions) else f"回忆{i + 1}"
            st.image(img, use_container_width=True, caption=caption)
        else:
            st.write(f"图片{i + 1}未找到，请检查路径：{img_path}")

# ------------------ 第四部分：拾碎回忆 ------------------
st.markdown('<div class="big-red"> 🔎拾碎梦的开始🔍 </div>', unsafe_allow_html=True)

img_menory = "images/menory.jpg"
st.image(img_menory, caption="画质越来越模糊，记忆越来越清晰~")

# 左右两列，左边放文字，右边放抖音头像
col3, col4 = st.columns([1, 2])

with col3:
    st.markdown("### 我的外表------>")
    st.markdown("### 我的智商------>")
    st.markdown("### 我的财力------>")
    st.markdown("### 我的运气------>")
with col4:
    st.image("images/大佬.jpg", width=200)

st.markdown("---")
# 结语文字
st.markdown("---")
st.markdown("### 啊哈！这就是欢愉~")
st.markdown("#### 咕咕嘎嘎！！！")
