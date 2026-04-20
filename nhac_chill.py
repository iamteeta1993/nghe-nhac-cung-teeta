import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# 1. Cấu hình hệ thống Neural Tiếng Việt
st.set_page_config(page_title="HỆ ĐIỀU HÀNH TEETA", page_icon="🧠", layout="wide")

# 2. Cấu hình Bộ não AI (Dán API Key của đại ca vào đây)
# Lấy Key tại: https://google.com
API_KEY = "AIzaSyDR5qfvuNz9m_agr53g1ZywlZHjZ697fdI"

if API_KEY != "AIzaSyDR5qfvuNz9m_agr53g1ZywlZHjZ697fdI":
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')

# 3. Giao diện Dark Mode chuẩn Quốc tế
st.markdown("""
    <style>
    .stApp { background: #000; color: #00ffcc; }
    .stTextInput input, .stTextArea textarea { 
        border-radius: 20px; background: #111 !important; 
        color: #00ffcc !important; border: 1px solid #00ffcc !important; 
    }
    .membership-card { background: #111; padding: 25px; border-radius: 15px; border: 1px solid #FFD700; text-align: center; }
    .ai-bubble { background: #161b22; padding: 20px; border-radius: 15px; border-left: 5px solid #00ffcc; line-height: 1.8; }
    .stButton button { border-radius: 20px; width: 100%; transition: 0.3s; }
    .stButton button:hover { background: #00ffcc; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- HỆ THỐNG THÀNH VIÊN ---
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

if st.session_state.current_user is None:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<div class='membership-card'>", unsafe_allow_html=True)
        st.subheader("🔐 HỆ THỐNG ĐĂNG NHẬP")
        user = st.text_input("Tên đăng nhập:")
        pwd = st.text_input("Mật khẩu:", type="password")
        if st.button("TRUY CẬP HỆ THỐNG"):
            if user == "admin" and pwd == "teeta2026":
                st.session_state.current_user = user
                st.rerun()
            else: st.error("Sai thông tin rồi đại ca!")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- GIAO DIỆN CHÍNH ---
with st.sidebar:
    st.title(f"🎖️ VIP: {st.session_state.current_user.upper()}")
    st.write("---")
    menu = st.radio("TRUNG TÂM ĐIỀU KHIỂN:", ["🤖 TRỢ LÝ AI", "🎧 NHẠC & CẢM XÚC", "🎬 XEM REVIEW PHIM", "📰 ĐỌC BÁO ZNEWS"])
    st.write("---")
    if st.button("ĐĂNG XUẤT"):
        st.session_state.current_user = None
        st.rerun()

# --- MỤC 1: TRỢ LÝ AI (BỘ NÃO THỰC THỤ) ---
if menu == "🤖 TRỢ LÝ AI":
    st.header("🤖 Trợ Lý Trí Tuệ Nhân Tạo Teeta")
    st.write("Đại ca có thể ra lệnh: *'Tóm tắt tin tức nóng hôm nay và tìm nhạc không lời cho tao đọc báo'*")

    user_command = st.text_area("Nhập lệnh cho AI:", placeholder="Ví dụ: Chào mày, hôm nay có tin gì mới không?...", height=150)

    if st.button("KÍCH HOẠT LỆNH"):
        if API_KEY == "DÁN_MÃ_AIza_CỦA_ĐẠI_CA_VÀO_ĐÂY":
            st.warning("⚠️ Đại ca chưa dán API Key vào dòng số 12 trong code nên AI chưa trả lời được!")
        else:
            with st.spinner("🧠 AI đang suy nghĩ..."):
                try:
                    # Gửi lệnh cho Gemini
                    prompt = f"Bạn là trợ lý ảo cao cấp của Teeta. Hôm nay là ngày 20/04/2026. Hãy trả lời yêu cầu này một cách thông minh và ngắn gọn bằng tiếng Việt: {user_command}"
                    response = model.generate_content(prompt)
                    
                    st.markdown("<div class='ai-bubble'>", unsafe_allow_html=True)
                    st.write(response.text)
                    st.markdown("</div>", unsafe_allow_html=True)

                    # AI tự động tìm nhạc liên quan đến tâm trạng của lệnh
                    st.subheader("🎵 Nhạc AI chọn riêng cho đại ca:")
                    with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
                        res = ydl.extract_info(user_command, download=False)['entries'][0]
                        st.video(res['webpage_url'])
                except Exception as e:
                    st.error(f"Lỗi kết nối bộ não AI: {e}")

# --- MỤC 2: NHẠC ---
elif menu == "🎧 NHẠC & CẢM XÚC":
    st.subheader("🎧 Kho Nhạc Thành Viên VIP")
    q = st.text_input("Tìm kiếm bài hát:")
    if q:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
            res = ydl.extract_info(q, download=False)['entries'][0]
            st.video(res['webpage_url'])

# --- MỤC 4: ZNEWS ---
elif menu == "📰 ĐỌC BÁO ZNEWS":
    st.header("📰 Trình Đọc Báo ZNews Đẳng Cấp")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get("https://znews.vn", headers=headers, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        articles = soup.find_all('article', limit=8)
        for art in articles:
            title_tag = art.find('p', class_='article-title') or art.find('h3')
            if title_tag:
                st.markdown(f"<div class='ai-bubble'><b>🔥 {title_tag.get_text()}</b><br>Nhấn vào Trợ lý AI để yêu cầu tóm tắt bài báo này!</div>", unsafe_allow_html=True)
    except: st.error("Lỗi kết nối vệ tinh ZNews!")

st.caption("HỆ ĐIỀU HÀNH TEETA V26.0 | AI POWERED | 20/04/2026")
