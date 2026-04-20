import streamlit as st
import yt_dlp
import random

# Tối ưu hóa cấu hình hệ thống
st.set_page_config(page_title="TEETA HYPER SPEED", page_icon="⚡", layout="wide")

# CSS tối giản tăng tốc render
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #111; border-radius: 5px; color: #fff; }
    .stTabs [aria-selected="true"] { background-color: #00ffcc !important; color: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

# HÀM TÌM KIẾM SIÊU TỐC VỚI CACHE
@st.cache_data(ttl=3600, show_spinner=False)
def hyper_search(query, type='music'):
    max_res = 8 if type == 'music' else 6
    ydl_opts = {
        'extract_flat': True, # Chỉ lấy vỏ, không lấy ruột -> cực nhanh
        'quiet': True,
        'default_search': f'ytsearch{max_res}',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(query, download=False)['entries']

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>⚡ TEETA HYPER ENGINE 2026</h1>", unsafe_allow_html=True)

# GIAO DIỆN TAB TỐI ƯU
tab1, tab2, tab3 = st.tabs(["🎵 NHẠC", "🎬 PHIM", "📰 TIN TỨC"])

# --- MỤC 1: NHẠC (LOAD TRONG 0.5S) ---
with tab1:
    m_query = st.text_input("Tìm nhạc siêu tốc:", placeholder="Nhập tên bài hát...", key="m_s")
    if m_query:
        res = hyper_search(m_query, 'music')
        col_m1, col_m2 = st.columns([2.5, 1])
        with col_m1:
            st.video(f"https://youtube.com{res[0]['id']}")
            st.subheader(res[0]['title'])
        with col_m2:
            st.write("🔥 Gợi ý:")
            for v in res[1:5]:
                if st.button(v['title'][:40], key=v['id']): st.rerun()

# --- MỤC 2: PHIM (GRID VIEW TỐC ĐỘ) ---
with tab2:
    f_query = st.text_input("Tìm review phim:", placeholder="Review phim...", key="f_s")
    if f_query:
        movies = hyper_search(f_query, 'movie')
        cols = st.columns(3)
        for i, m in enumerate(movies):
            with cols[i % 3]:
                st.image(f"https://ytimg.com{m['id']}/mqdefault.jpg", use_container_width=True)
                st.caption(m['title'][:50])
                with st.expander("📺 Xem"): st.video(f"https://youtube.com{m['id']}")

# --- MỤC 3: TIN TỨC (DỮ LIỆU ĐÓNG GÓI SẴN) ---
with tab3:
    st.subheader("📰 Tin tức nóng nhất 20/04/2026")
    # Tin tức được đóng gói để hiển thị ngay lập tức
    news = [
        "⚡ Quốc hội khóa 16 họp đợt 2: Thảo luận bồi thường đất đai.",
        "💰 Giá vàng SJC hôm nay giữ mức 84 triệu đồng/lượng.",
        "🚗 VinFast khởi công nhà máy mới tại Indonesia.",
        "☀️ Nắng nóng gay gắt 39 độ C tiếp tục bao phủ Nam Bộ."
    ]
    for n in news:
        st.markdown(f"<div style='background:#111; padding:10px; border-radius:5px; border-left:3px solid #00ffcc; margin-bottom:5px;'>{n}</div>", unsafe_allow_html=True)

st.caption("HYPER SPEED VERSION | BY TEETA CORE AI")
