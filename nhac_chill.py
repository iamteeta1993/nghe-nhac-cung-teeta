import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# 1. Cấu hình Neural OS
st.set_page_config(page_title="TEETA NEURAL OS", page_icon="🧠", layout="wide")

# 2. KHỞI TẠO BỘ NÃO AI (BẢN TỰ PHỤC HỒI)
API_KEY = "AIzaSyDR5qfvuNz9m_agr53g1ZywlZHjZ697fdI"
genai.configure(api_key=API_KEY)

# Thuật toán dò tìm model: Nếu cái này lỗi thì dùng cái kia
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Thử gọi một lệnh nhỏ để kiểm tra xem model có thực sự chạy được không
    model.generate_content("test")
except:
    try:
        model = genai.GenerativeModel('gemini-pro')
    except:
        st.error("⚠️ Chìa khóa API của bạn gặp vấn đề hoặc tài khoản chưa kích hoạt. Hãy kiểm tra lại Google AI Studio!")

# 3. Giao diện Cyberpunk đẳng cấp
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .ai-bubble { background: #161b22; padding: 25px; border-radius: 15px; border-left: 5px solid #00ffcc; line-height: 1.8; margin-bottom: 20px; }
    .stButton button { border-radius: 30px; width: 100%; background: #222; color: #00ffcc; border: 1px solid #00ffcc; }
    .stButton button:hover { background: #00ffcc !important; color: black !important; box-shadow: 0 0 20px #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- HỆ THỐNG ĐĂNG NHẬP ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    c1, c2, c3 = st.columns(3)
    with c2:
        st.markdown("<h2 style='text-align: center;'>🔐 TRUY CẬP VIP</h2>", unsafe_allow_html=True)
        user = st.text_input("Username:")
        pwd = st.text_input("Password:", type="password")
        if st.button("KÍCH HOẠT"):
            if user == "admin" and pwd == "teeta2026":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("Sai rồi!")
    st.stop()

# --- GIAO DIỆN CHÍNH ---
with st.sidebar:
    st.title("🧠 TEETA OS V26")
    menu = st.radio("CHỌN KHÔNG GIAN:", ["🤖 TRỢ LÝ AI", "🎵 NHẠC & MOOD", "🎬 XEM PHIM", "📰 TIN TỨC ZNEWS"])

if menu == "🤖 TRỢ LÝ AI":
    st.header("🤖 Trợ Lý Trí Tuệ Nhân Tạo Teeta")
    user_input = st.text_area("Ra lệnh cho AI:", placeholder="Chào mày, hôm nay có tin gì mới không?...")
    if st.button("KÍCH HOẠT LỆNH"):
        with st.spinner("🧠 AI đang phân tích..."):
            try:
                response = model.generate_content(f"Trả lời bằng tiếng Việt: {user_input}")
                st.markdown(f"<div class='ai-bubble'>{response.text}</div>", unsafe_allow_html=True)
                
                # Tự tìm nhạc theo lệnh
                with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch1'}) as ydl:
                    res = ydl.extract_info(user_input, download=False)['entries'][0]
                    st.video(res['webpage_url'])
            except Exception as e:
                st.error(f"Lỗi AI: {e}")

elif menu == "🎵 NHẠC & MOOD":
    q = st.text_input("Tìm nhạc:")
    if q:
        with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch1'}) as ydl:
            res = ydl.extract_info(q, download=False)['entries'][0]
            st.video(res['webpage_url'])

elif menu == "📰 TIN TỨC ZNEWS":
    st.header("📰 ZNews Reader")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get("https://znews.vn", headers=headers, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        for art in soup.find_all('article', limit=5):
            title = art.find('p', class_='article-title') or art.find('h3')
            if title: st.markdown(f"<div class='ai-bubble'><b>🔥 {title.get_text()}</b></div>", unsafe_allow_html=True)
    except: st.error("Lỗi kết nối!")

st.caption("TEETA OS V26.0 | 20/04/2026")
