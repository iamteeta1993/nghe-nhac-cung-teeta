import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# 1. Cấu hình hệ thống Neural OS
st.set_page_config(page_title="TEETA NEURAL OS", page_icon="🧠", layout="wide")

# 2. KHỞI TẠO BỘ NÃO AI (ĐÃ DÁN KHÓA CỦA ĐẠI CA)
API_KEY = "AIzaSyDo4d5bIRhxlrPQgt-aiBF4YO5nPbuoe9s"
genai.configure(api_key=API_KEY)

def get_brain():
    # Thử các model từ mạnh nhất đến ổn định nhất
    models_to_try = ['gemini-pro', 'gemini-1.5-flash']
    for m in models_to_try:
        try:
            brain = genai.GenerativeModel(m)
            brain.generate_content("ping") # Kiểm tra tín hiệu
            return brain
        except: continue
    return None

model = get_brain()

# 3. Giao diện Cyberpunk 2026 đẳng cấp
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .stTextInput input, .stTextArea textarea { border-radius: 20px; background: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; }
    .ai-bubble { background: #161b22; padding: 25px; border-radius: 15px; border-left: 5px solid #00ffcc; line-height: 1.8; margin-bottom: 20px; }
    .stButton button { border-radius: 30px; width: 100%; background: #222; color: #00ffcc; border: 1px solid #00ffcc; transition: 0.3s; }
    .stButton button:hover { background: #00ffcc !important; color: black !important; box-shadow: 0 0 20px #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- HỆ THỐNG ĐĂNG NHẬP ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if not st.session_state.logged_in:
    c1, c2, c3 = st.columns(3)
    with c2:
        st.markdown("<h2 style='text-align: center;'>🔐 TRUY CẬP VIP</h2>", unsafe_allow_html=True)
        user = st.text_input("Tên đăng nhập:")
        pwd = st.text_input("Mật khẩu:", type="password")
        if st.button("KÍCH HOẠT HỆ THỐNG"):
            if user == "thang" and pwd == "123":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("Sai thông tin rồi đại ca!")
    st.stop()

# --- SIDEBAR ĐIỀU HƯỚNG ---
with st.sidebar:
    st.title("🧠 TEETA OS V26")
    menu = st.radio("CHỌN KHÔNG GIAN:", ["🤖 TRỢ LÝ AI", "🎵 NHẠC & MOOD", "🎬 XEM PHIM", "📰 TIN TỨC ZNEWS"])
    if st.button("ĐĂNG XUẤT"):
        st.session_state.logged_in = False
        st.rerun()

# --- MỤC 1: TRỢ LÝ AI ---
if menu == "🤖 TRỢ LÝ AI":
    st.header("🤖 Trợ Lý Trí Tuệ Nhân Tạo Teeta")
    user_input = st.text_area("Ra lệnh cho AI:", placeholder="Chào mày, tóm tắt tin tức sáng nay cho tao...")
    if st.button("KÍCH HOẠT LỆNH"):
        if model:
            with st.spinner("🧠 AI đang suy nghĩ..."):
                try:
                    response = model.generate_content(f"Bạn là trợ lý ảo của Teeta. Trả lời bằng tiếng Việt: {user_input}")
                    st.markdown(f"<div class='ai-bubble'>{response.text}</div>", unsafe_allow_html=True)
                    # Tìm nhạc liên quan
                    with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
                        res = ydl.extract_info(user_input, download=False)['entries']
                        if res: st.video(res['webpage_url'])
                except Exception as e: st.error(f"Lỗi phản hồi: {e}")
        else: st.error("⚠️ Lỗi API Key! Hãy kiểm tra lại chìa khóa.")

# --- MỤC 2: NHẠC ---
elif menu == "🎵 NHẠC & MOOD":
    st.header("🎧 Kho Nhạc Membership")
    q = st.text_input("Tìm nhạc:")
    if q:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
            res = ydl.extract_info(q, download=False)['entries']
            if res: st.video(res['webpage_url'])

# --- MỤC 4: TIN TỨC ZNEWS ---
elif menu == "📰 TIN TỨC ZNEWS":
    st.header("📰 ZNews Reader")
    try:
        resp = requests.get("https://znews.vn", headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        for art in soup.find_all('article', limit=5):
            title = art.find('p', class_='article-title') or art.find('h3')
            if title: st.markdown(f"<div class='ai-bubble'><b>🔥 {title.get_text()}</b></div>", unsafe_allow_html=True)
    except: st.error("Lỗi kết nối!")

st.caption("TEETA OS V26.0 | POWERED BY GEMINI AI | 20/04/2026")
