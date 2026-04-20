import streamlit as st
import yt_dlp
import feedparser
import random

# 1. Cấu hình hệ thống Neural
st.set_page_config(page_title="TEETA ULTIMATE HUB", page_icon="🚀", layout="wide")

# 2. CSS Dark Mode chuẩn 2026
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    [data-testid="stSidebar"] { background-color: #111; border-right: 1px solid #333; }
    .card { background-color: #111; padding: 15px; border-radius: 15px; border: 1px solid #222; margin-bottom: 20px; transition: 0.3s; }
    .card:hover { border-color: #ff4b4b; background-color: #1a1a1a; }
    .news-title { color: #ffffff; font-weight: bold; text-decoration: none; font-size: 18px; }
    .news-title:hover { color: #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ĐIỀU HƯỚNG ---
with st.sidebar:
    st.title("🚀 TEETA HUB")
    st.write("---")
    menu = st.radio("CHỌN KHÔNG GIAN:", ["🎧 NGHE NHẠC", "🎬 XEM PHIM", "📰 TIN TỨC 24H"], index=0)
    st.write("---")
    st.info("Hệ thống Neural v15.0 - Sẵn sàng phục vụ đại ca!")

# --- XỬ LÝ LOGIC ---

# MỤC 1: NGHE NHẠC (YOUTUBE CORE)
if menu == "🎧 NGHE NHẠC":
    st.header("🎵 Không Gian Âm Nhạc")
    query = st.text_input("", placeholder="🔍 Nhập tên bài hát hoặc nghệ sĩ...", key="music_search")
    
    if query:
        with st.spinner('🚀 AI đang quét sóng âm...'):
            try:
                with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch8'}) as ydl:
                    results = ydl.extract_info(query, download=False)['entries']
                
                col_main, col_side = st.columns([2.5, 1])
                with col_main:
                    st.video(results[0]['webpage_url'])
                    st.subheader(results[0]['title'])
                    with st.expander("🤖 AI Music Insight"):
                        st.code(f"/imagine prompt: Futuristic visual of {query}, neon style, 8k", language="text")
                with col_side:
                    st.write("**Tiếp theo:**")
                    for vid in results[1:6]:
                        st.image(vid['thumbnail'], use_container_width=True)
                        if st.button("Phát bài này", key=vid['id']): st.rerun()
            except: st.error("Lỗi kết nối YouTube!")

# MỤC 2: XEM PHIM (REVIEW & TRAILER)
elif menu == "🎬 XEM PHIM":
    st.header("🎬 Rạp Phim Review")
    m_query = st.text_input("", placeholder="🔍 Tìm phim hoặc thể loại (Hành động, Kinh dị...)", key="movie_search")
    
    search_term = m_query if m_query else "Review phim mới nhất 2026"
    with st.spinner('🎬 Đang lùng sục kho phim...'):
        with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch12'}) as ydl:
            movies = ydl.extract_info(search_term, download=False)['entries']
        
        cols = st.columns(3)
        for i, movie in enumerate(movies):
            with cols[i % 3]:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.image(movie['thumbnail'], use_container_width=True)
                st.markdown(f"**{movie['title'][:50]}...**")
                with st.expander("📺 Xem ngay"): st.video(movie['webpage_url'])
                st.markdown("</div>", unsafe_allow_html=True)

# MỤC 3: TIN TỨC (RSS FEED TỪ VNEXPRESS/TUOITRE)
elif menu == "📰 TIN TỨC 24H":
    st.header("📰 Cập Nhật Tin Tức Toàn Cầu")
    source = st.selectbox("Chọn nguồn tin:", ["VnExpress - Tin mới nhất", "Tuổi Trẻ - Thời sự"])
    
    rss_url = "https://vnexpress.net" if "VnExpress" in source else "https://tuoitre.vn"
    
    with st.spinner('📡 Đang bắt sóng vệ tinh...'):
        feed = feedparser.parse(rss_url)
        for entry in feed.entries[:15]:
            with st.container():
                st.markdown(f"""
                    <div class='card'>
                        <a href='{entry.link}' target='_blank' class='news-title'>{entry.title}</a>
                        <p style='color: #888; font-size: 14px;'>📅 {entry.published}</p>
                        <p style='color: #ccc;'>{entry.summary.split('<br />')[-1][:200]}...</p>
                    </div>
                """, unsafe_allow_html=True)

st.caption("TEETA ULTIMATE HUB V15.0 | ÂM NHẠC • ĐIỆN ẢNH • THÔNG TIN | 2026")
