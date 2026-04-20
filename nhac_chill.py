import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# 1. Cấu hình hệ thống Neural OS
st.set_page_config(page_title="TEETA NEURAL OS", page_icon="🧠", layout="wide")

# 2. Nhúng bộ não AI Gemini (Mã của đại ca)
API_KEY = "AIzaSyDR5qfvuNz9m_agr53g1ZywlZHjZ697fdI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Giao diện Cyberpunk 2026 đẳng cấp
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .stTextInput input, .stTextArea textarea { border-radius: 20px; background: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; }
    .ai-bubble { background: #161b22; padding: 25px; border-radius: 15px; border-left: 5px solid #00ffcc; line-height: 1.8; margin-bottom: 20px; }
    .stButton button { border-radius: 30px; width: 100%; background: #222; color: #00ffcc; border: 1px solid #00ffcc; transition: 0.3s; }
    .stButton button:hover { background: #00ffcc; color: black; box-shadow: 0 0 20px #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- HỆ THỐNG ĐĂNG NHẬP ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    # Sửa lỗi dòng 35 tại đây: Thêm số 3 vào columns
    c1, c2, c3 = st.columns(3)
    with c2:
        st.markdown("<h2 style='text-align: center; color: #ffd700;'>🔐 TRUY CẬP VIP</h2>", unsafe_allow_html=True)
        user = st.text_input("Tên đăng nhập:")
        pwd = st.text_input("Mật khẩu:", type="password")
        if st.button("KÍCH HOẠT HỆ THỐNG"):
            if user == "admin" and pwd == "teeta2026":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("Sai thông tin rồi đại ca!")
    st.stop()

# --- SIDEBAR ĐIỀU HƯỚNG ---
with st.sidebar:
    st.title("🧠 TEETA OS V26")
    menu = st.radio("CHUYỂN KHÔNG GIAN:", ["🤖 TRỢ LÝ AI", "🎵 NGHE NHẠC", "🎬 XEM PHIM", "📰 TIN TỨC ZNEWS"])
    if st.button("ĐĂNG XUẤT"):
        st.session_state.logged_in = False
        st.rerun()

# --- MỤC 1: TRỢ LÝ AI (GEMINI) ---
if menu == "🤖 TRỢ LÝ AI":
    st.header("🤖 Trợ Lý Trí Tuệ Nhân Tạo Teeta")
    user_input = st.text_area("Ra lệnh cho AI:", placeholder="Chào mày, tóm tắt tin tức sáng nay cho tao...")
    if st.button("KÍCH HOẠT LỆNH"):
        with st.spinner("🧠 AI đang suy nghĩ..."):
            try:
                prompt = f"Bạn là trợ lý ảo cao cấp của Teeta. Hãy trả lời bằng tiếng Việt thông minh: {user_input}"
                response = model.generate_content(prompt)
                st.markdown(f"<div class='ai-bubble'>{response.text}</div>", unsafe_allow_html=True)
                with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch1'}) as ydl:
                    res = ydl.extract_info(user_input, download=False)['entries']
                    st.video(res[0]['webpage_url'])
            except Exception as e:
                st.error(f"Lỗi AI: {e}")

# --- MỤC 2: NHẠC ---
elif menu == "🎵 NGHE NHẠC":
    q = st.text_input("Tìm nhạc:")
    if q:
        with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch1'}) as ydl:
            res = ydl.extract_info(q, download=False)['entries']
            st.video(res[0]['webpage_url'])

# --- MỤC 4: ZNEWS ---
elif menu == "📰 TIN TỨC ZNEWS":
    st.header("📰 ZNews Reader")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get("https://znews.vn", headers=headers, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        for art in soup.find_all('article', limit=5):
            title = art.find('p', class_='article-title') or art.find('h3')
            if title:
                st.markdown(f"<div class='ai-bubble'><b>🔥 {title.get_text()}</b></div>", unsafe_allow_html=True)
    except: st.error("Lỗi kết nối tin tức!")

st.caption("TEETA OS V26.0 | POWERED BY GEMINI AI | 20/04/2026")
