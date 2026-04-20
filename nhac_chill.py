import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# 1. Cấu hình Hệ điều hành Teeta Neural
st.set_page_config(page_title="TEETA NEURAL OS", page_icon="🧠", layout="wide")

# 2. Nhúng bộ não AI Gemini (Đã dán mã của đại ca)
API_KEY = "AIzaSyDR5qfvuNz9m_agr53g1ZywlZHjZ697fdI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Giao diện Cyberpunk 2026 đẳng cấp
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    [data-testid="stSidebar"] { background-color: #111; border-right: 1px solid #333; }
    .stTextInput input, .stTextArea textarea { 
        border-radius: 20px; background: #111 !important; 
        color: #00ffcc !important; border: 1px solid #00ffcc !important; 
    }
    .ai-bubble { background: #161b22; padding: 25px; border-radius: 15px; border-left: 5px solid #00ffcc; line-height: 1.8; margin-bottom: 20px; }
    .stButton button { border-radius: 30px; width: 100%; background: #222; color: #00ffcc; border: 1px solid #00ffcc; transition: 0.3s; }
    .stButton button:hover { background: #00ffcc; color: black; box-shadow: 0 0 20px #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- HỆ THỐNG ĐĂNG NHẬP THÀNH VIÊN ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<h2 style='text-align: center; color: #ffd700;'>🔐 TRUY CẬP HỆ THỐNG VIP</h2>", unsafe_allow_html=True)
        user = st.text_input("Tên đăng nhập:")
        pwd = st.text_input("Mật khẩu:", type="password")
        if st.button("KÍCH HOẠT NEURAL OS"):
            if user == "thuba" and pwd == "123":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("Thông tin không chính xác, đại ca ơi!")
    st.stop()

# --- SIDEBAR ĐIỀU HƯỚNG ---
with st.sidebar:
    st.markdown("<h2 style='color: #00ffcc;'>🧠 TEETA OS V26</h2>", unsafe_allow_html=True)
    st.write(f"Chào đại ca! **{st.session_state.get('user', 'ADMIN')}**")
    menu = st.radio("TRUNG TÂM ĐIỀU KHIỂN:", ["🤖 TRỢ LÝ AI", "🎵 NHẠC & MOOD", "🎬 XEM PHIM VIP", "📰 TIN TỨC ZNEWS"])
    st.write("---")
    if st.button("ĐĂNG XUẤT"):
        st.session_state.logged_in = False
        st.rerun()

# --- MỤC 1: TRỢ LÝ AI (SỬ DỤNG BỘ NÃO GEMINI) ---
if menu == "🤖 TRỢ LÝ AI":
    st.header("🤖 Trợ Lý Trí Tuệ Nhân Tạo Teeta")
    st.write("Ra lệnh cho AI: *'Tóm tắt tin tức và tìm bản nhạc chill nhất'*")
    
    user_input = st.text_area("Nhập lệnh cho bộ não AI:", placeholder="Ví dụ: Hôm nay 20/04/2026 có gì hot?...", height=120)
    
    if st.button("KÍCH HOẠT TRÍ TUỆ NHÂN TẠO"):
        with st.spinner("🧠 AI đang phân tích dữ liệu..."):
            try:
                # 1. AI Trả lời văn bản
                prompt = f"Bạn là trợ lý ảo cao cấp của Teeta. Hãy trả lời bằng tiếng Việt cực kỳ thông minh: {user_input}"
                response = model.generate_content(prompt)
                st.markdown(f"<div class='ai-bubble'>{response.text}</div>", unsafe_allow_html=True)
                
                # 2. Tự động tìm nhạc liên quan
                st.subheader("🎵 Nhạc AI đề xuất cho cảm xúc của đại ca:")
                with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch1'}) as ydl:
                    res = ydl.extract_info(user_input, download=False)['entries'][0]
                    st.video(res['webpage_url'])
            except Exception as e:
                st.error("Lỗi bộ não AI. Đại ca kiểm tra lại API Key nhé!")

# --- MỤC 2: NHẠC & MOOD ---
elif menu == "🎵 NHẠC & MOOD":
    st.header("🎧 Kho Nhạc Membership")
    m_q = st.text_input("Tìm kiếm giai điệu:", placeholder="Sơn Tùng MTP, Lofi chill...")
    if m_q:
        with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch5'}) as ydl:
            res = ydl.extract_info(m_q, download=False)['entries']
            st.video(res[0]['webpage_url'])
            st.success(f"Đã nạp bản nhạc: {res[0]['title']}")

# --- MỤC 3: XEM PHIM VIP ---
elif menu == "🎬 XEM PHIM VIP":
    st.header("🎬 Cinema Review Đẳng Cấp")
    f_q = st.text_input("Tìm phim:", placeholder="Review phim hành động...")
    s_term = f_q if f_q else "Review phim mới nhất 2026"
    with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch6'}) as ydl:
        movies = ydl.extract_info(s_term, download=False)['entries']
    
    cols = st.columns(3)
    for i, m in enumerate(movies):
        with cols[i%3]:
            st.image(m['thumbnail'], use_container_width=True)
            with st.expander("📺 Xem Trailer/Review"):
                st.video(m['webpage_url'])

# --- MỤC 4: TIN TỨC ZNEWS (SCRAPING) ---
elif menu == "📰 TIN TỨC ZNEWS":
    st.header("📰 Trình Đọc Báo ZNews AI")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get("https://znews.vn", headers=headers, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        articles = soup.find_all('article', limit=8)
        for art in articles:
            title_tag = art.find('p', class_='article-title') or art.find('h3')
            if title_tag:
                st.markdown(f"<div class='ai-bubble'><b>🔥 {title_tag.get_text()}</b><br>Đã sẵn sàng cho AI tóm tắt nội dung...</div>", unsafe_allow_html=True)
    except: st.error("Mất kết nối với vệ tinh tin tức!")

st.caption("TEETA NEURAL OS V26.0 | POWERED BY GEMINI AI | 2026")
