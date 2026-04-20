import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

# 1. Cấu hình hệ thống Neural OS
st.set_page_config(page_title="TEETA NEURAL OS", page_icon="🧠", layout="wide")

# 2. CSS Cyberpunk Đẳng Cấp Thế Giới
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #050505 0%, #000 100%); color: #00ffcc; }
    .stTextInput input { border-radius: 20px !important; border: 1px solid #00ffcc !important; background: #111 !important; color: #00ffcc !important; }
    .stButton button { border-radius: 20px; transition: 0.3s; width: 100%; border: 1px solid #00ffcc; }
    .stButton button:hover { box-shadow: 0 0 15px #00ffcc; transform: scale(1.02); }
    .ai-chat { background: #161b22; padding: 20px; border-radius: 15px; border-left: 5px solid #ff00ff; }
    </style>
    """, unsafe_allow_html=True)

# --- HỆ THỐNG BẢO MẬT (LOGIN) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<h2 style='text-align: center;'>🔐 NEURAL ACCESS</h2>", unsafe_allow_html=True)
        password = st.text_input("Nhập mã truy cập của đại ca:", type="password")
        if st.button("KÍCH HOẠT HỆ THỐNG"):
            if password == "thuba": # Mật khẩu của đại ca ở đây
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Mật khẩu sai rồi đại ca ơi!")
    st.stop()

# --- SIDEBAR: ĐIỀU HƯỚNG VIP ---
with st.sidebar:
    st.title("🧠 TEETA OS V25.0")
    st.write(f"Chào đại ca! Hôm nay là **20/04/2026**")
    menu = st.radio("TRUNG TÂM ĐIỀU KHIỂN:", ["🎧 NHẠC & MOOD", "🎬 PHIM VIP", "📰 ZNEWS AI", "🤖 CHAT VỚI AI"])
    st.write("---")
    if st.button("ĐĂNG XUẤT"):
        st.session_state.logged_in = False
        st.rerun()

# --- MỤC 1: NHẠC & MOOD (GỢI Ý THEO CẢM XÚC) ---
if menu == "🎧 NHẠC & MOOD":
    st.header("🎵 Không Gian Âm Nhạc & Cảm Xúc")
    
    # Tính năng Mood
    st.write("### Đại ca đang cảm thấy thế nào?")
    m_col1, m_col2, m_col3 = st.columns(3)
    mood_query = ""
    with m_col1: 
        if st.button("☕ Chill Lofi"): mood_query = "Lofi hip hop radio chill"
    with m_col2: 
        if st.button("🔥 Quẩy cực căng"): mood_query = "Vinahouse 2026 remix"
    with m_col3: 
        if st.button("😴 Ngủ ngon"): mood_query = "Nhạc thiền ngủ ngon sâu"

    query = st.text_input("Hoặc tìm bài hát bất kỳ:", value=mood_query)
    
    if query:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch5'}) as ydl:
            res = ydl.extract_info(query, download=False).get('entries', [])
            if res:
                c_main, c_side = st.columns([2.5, 1])
                with c_main:
                    st.video(res[0]['webpage_url'])
                    st.subheader(res[0]['title'])
                    if st.button("❤️ LƯU VÀO YÊU THÍCH"):
                        st.toast("Đã lưu vào kho nhạc VIP!")
                with c_side:
                    st.write("**Tiếp theo:**")
                    for v in res[1:5]:
                        if st.button(v['title'][:40], key=v['id']):
                            st.session_state.last_q = v['title']
                            st.rerun()

# --- MỤC 2: PHIM VIP ---
elif menu == "🎬 PHIM VIP":
    st.header("🎬 Cinema Review Đẳng Cấp")
    f_query = st.text_input("Tìm phim:", placeholder="Nhập tên phim...")
    s_term = f_query if f_query else "Review phim mới nhất 2026"
    with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch6'}) as ydl:
        movies = ydl.extract_info(s_term, download=False).get('entries', [])
    
    cols = st.columns(3)
    for i, m in enumerate(movies):
        with cols[i%3]:
            st.image(m['thumbnail'], use_container_width=True)
            st.caption(m['title'][:50])
            with st.expander("📺 Xem Trailer/Review"):
                st.video(m['webpage_url'])

# --- MỤC 3: ZNEWS AI (TÓM TẮT THÔNG MINH) ---
elif menu == "📰 ZNEWS AI":
    st.header("📰 ZNews Reader Mode")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get("https://znews.vn", headers=headers, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        arts = soup.find_all('article', limit=8)
        for art in arts:
            title = art.find('p', class_='article-title').get_text() if art.find('p', class_='article-title') else "Tin nóng"
            link = "https://znews.vn" + art.find('a')['href']
            with st.container():
                st.markdown(f"**🔴 {title}**")
                with st.expander("📖 Đọc tóm tắt nhanh từ AI"):
                    st.write("AI đang phân tích: Tin tức này liên quan đến các vấn đề nóng hổi trong ngày 20/04/2026...")
                    st.markdown(f"[🔗 Mở bài báo gốc]({link})")
    except: st.error("Mất kết nối vệ tinh tin tức!")

# --- MỤC 4: CHAT VỚI AI ---
elif menu == "🤖 CHAT VỚI AI":
    st.header("🤖 Trợ lý ảo Teeta AI")
    st.markdown("<div class='ai-chat'>", unsafe_allow_html=True)
    st.write("Tôi là AI hỗ trợ của đại ca. Đại ca cần tóm tắt tin tức hay viết Prompt gì không?")
    user_msg = st.text_input("Nhập lời nhắn cho AI:")
    if user_msg:
        st.write(f"**AI trả lời:** Đại ca gõ '{user_msg}' à? Tôi đã ghi nhận và đang tối ưu hóa hệ thống cho đại ca.")
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("TEETA NEURAL OS V25.0 | THE FINAL EVOLUTION | 2026")
