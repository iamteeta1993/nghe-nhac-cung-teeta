import streamlit as st
import yt_dlp
import random

# 1. Cấu hình giao diện rộng toàn màn hình
st.set_page_config(page_title="TEETA 4-COLUMN ENGINE", page_icon="🧠", layout="wide")

# 2. CSS Cyberpunk Đẳng cấp cho 4 cột
st.markdown("""
    <style>
    .stApp { background: #000; color: #00ffcc; }
    .column-box { 
        background: #0a0a0a; border: 1px solid #333; 
        padding: 15px; border-radius: 10px; height: 85vh; overflow-y: auto; 
    }
    .stTextInput input { border-radius: 20px !important; background: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; }
    .ai-tag { color: #ff00ff; font-family: monospace; font-size: 12px; }
    /* Ẩn bớt khoảng cách thừa của Streamlit */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #00ffcc;'>🧠 TEETA NEURAL MULTI-CONTROL V7.0</h2>", unsafe_allow_html=True)

# --- THANH TÌM KIẾM CHUNG ---
query = st.text_input("", placeholder="🔍 NHẬP TẦN SỐ ÂM NHẠC TẠI ĐÂY...", label_visibility="collapsed")

# --- CHIA 4 CỘT DỌC ---
col1, col2, col3, col4 = st.columns([1, 1.5, 1.5, 1])

# CỘT 1: ĐIỀU KHIỂN & AI INSIGHT
with col1:
    st.markdown("### 📡 CONTROL")
    if query:
        st.success(f"Target: {query}")
        st.markdown("---")
        st.markdown("**🤖 AI ANALYSIS:**")
        st.write(f"Mood: {random.choice(['Deep Synth', 'Cyber Chill', 'Vina-Neural'])}")
        st.markdown("<p class='ai-tag'>> GENERATING PROMPTS...</p>", unsafe_allow_html=True)
        st.code(f"/imagine prompt: {query} cinematic lighting, neon green, techwear style, 8k", language="text")
    else:
        st.info("Đợi lệnh...")

# CỘT 2: YOUTUBE CORE (STREAMING)
with col2:
    st.markdown("### 📺 YOUTUBE")
    if query:
        try:
            ydl_opts = {'quiet': True, 'default_search': 'ytsearch1', 'format': 'best'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)['entries'][0]
            st.video(info['webpage_url'])
            st.caption(info['title'])
        except:
            st.error("Lỗi kết nối YouTube")

# CỘT 3: MULTI-SOURCE (ZING / SOUNDCLOUD)
with col3:
    st.markdown("### 🎶 MULTI-SOURCE")
    if query:
        source = st.radio("Nguồn:", ["ZingMP3", "SoundCloud"], horizontal=True)
        q_url = query.replace(' ', '+')
        if source == "ZingMP3":
            url = f"https://zingmp3.vn{q_url}"
        else:
            url = f"https://soundcloud.com{q_url}"
        st.components.v1.iframe(url, height=500, scrolling=True)

# CỘT 4: COMMUNITY & PROMPT WRITING
with col4:
    st.markdown("### 💬 NEURAL LOG")
    st.write("Ghi chép Prompt:")
    user_p = st.text_area("", placeholder="Nhập suy nghĩ...", height=150, label_visibility="collapsed")
    if st.button("LƯU DỮ LIỆU"):
        st.toast("Đã nạp vào Core!")
    st.markdown("---")
    st.write("**Bình luận mới nhất:**")
    st.caption("AI_Bot: Giai điệu này đạt chuẩn Neural.")
    st.caption("User_99: App đỉnh quá đại ca!")

st.caption("TEETA NEURAL ENGINE - 4 COLUMN INTERFACE | 2026")
