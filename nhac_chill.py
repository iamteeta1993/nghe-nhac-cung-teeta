import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup

# 1. Cấu hình hệ thống Neural Đẳng cấp
st.set_page_config(page_title="TEETA ULTIMATE HUB", page_icon="🚀", layout="wide")

# 2. CSS Cyberpunk 2026 - Tối ưu giao diện sạch
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    [data-testid="stSidebar"] { background-color: #111; border-right: 1px solid #333; }
    .card { background-color: #111; padding: 15px; border-radius: 12px; border: 1px solid #222; margin-bottom: 15px; }
    .z-title { color: #00ffcc; font-size: 18px; font-weight: bold; text-decoration: none; }
    .stTextInput input { border-radius: 20px !important; background-color: #1a1a1a !important; color: #00ffcc !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ĐIỀU HƯỚNG ---
with st.sidebar:
    st.title("🚀 TEETA HUB")
    st.write("---")
    menu = st.radio("CHỌN KHÔNG GIAN:", ["📰 ZNEWS 24H", "🎧 NGHE NHẠC", "🎬 XEM PHIM"], index=0)
    st.write("---")
    st.success("Hệ thống Đã Kiểm Duyệt ✅")
    st.caption("Version 23.0 - Stable Edition")

# --- MỤC 1: ZNEWS 24H (QUÉT TIN TRỰC TIẾP) ---
if menu == "📰 ZNEWS 24H":
    st.header("📰 ZNews - Tin Tức Thế Giới 2026")
    with st.spinner('📡 Đang đồng bộ hóa ZNews...'):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get("https://znews.vn", headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Lấy các bài viết nổi bật
            articles = soup.find_all('article', limit=10)
            
            if not articles:
                st.warning("Hệ thống đang làm mới luồng tin. Đại ca đợi chút nhé!")
            else:
                for art in articles:
                    title_tag = art.find('p', class_='article-title') or art.find('h3')
                    link_tag = art.find('a')
                    img_tag = art.find('img')
                    
                    if title_tag and link_tag:
                        title = title_tag.get_text()
                        link = "https://znews.vn" + link_tag['href'] if not link_tag['href'].startswith('http') else link_tag['href']
                        img = img_tag.get('data-src') or img_tag.get('src') if img_tag else "https://placeholder.com"
                        
                        with st.container():
                            c1, c2 = st.columns([1, 2.5])
                            with c1: st.image(img, use_container_width=True)
                            with c2:
                                st.markdown(f"<a href='{link}' target='_blank' class='z-title'>{title}</a>", unsafe_allow_html=True)
                                with st.expander("📖 Xem tóm tắt & Link gốc"):
                                    st.write("Dữ liệu tin tức được bóc tách trực tiếp từ ZNews.vn")
                                    st.markdown(f"[🔗 Mở bài báo trên ZNews]({link})")
                            st.write("---")
        except:
            st.error("⚠️ Không thể kết nối ZNews trưa nay. Đại ca hãy thử lại sau!")

# --- MỤC 2: NGHE NHẠC (HYPER SPEED) ---
elif menu == "🎧 NGHE NHẠC":
    st.header("🎵 Không Gian Âm Nhạc")
    q = st.text_input("", placeholder="🔍 Nhập tên bài hát...", key="m_s")
    if q:
        with st.spinner('🚀 AI đang tìm nhạc...'):
            try:
                ydl_opts = {'quiet': True, 'default_search': 'ytsearch5', 'format': 'best'}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    res = ydl.extract_info(q, download=False)['entries']
                
                col_main, col_side = st.columns([2.5, 1])
                with col_main:
                    st.video(res[0]['webpage_url'])
                    st.subheader(res[0]['title'])
                with col_side:
                    st.write("**Gợi ý:**")
                    for vid in res[1:5]:
                        if st.button(vid['title'][:40], key=vid['id']):
                            st.rerun()
            except: st.error("Lỗi kết nối âm nhạc!")

# --- MỤC 3: XEM PHIM (REVIEW GRID) ---
elif menu == "🎬 XEM PHIM":
    st.header("🎬 Cinema Review")
    mq = st.text_input("", placeholder="🔍 Tìm phim...", key="f_s")
    s_term = mq if mq else "Review phim mới nhất"
    with st.spinner('🎬 Đang quét kho phim...'):
        try:
            with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch6'}) as ydl:
                movies = ydl.extract_info(s_term, download=False)['entries']
            cols = st.columns(3)
            for i, m in enumerate(movies):
                with cols[i % 3]:
                    st.image(m['thumbnail'], use_container_width=True)
                    st.caption(m['title'][:50])
                    with st.expander("📺 Xem"): st.video(m['webpage_url'])
        except: st.error("Lỗi kết nối phim!")

st.caption("TEETA ULTIMATE HUB v23.0 | STABLE VERSION | 20/04/2026")
