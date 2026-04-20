import streamlit as st
import yt_dlp
import requests

st.set_page_config(page_title="Teeta Global Music", page_icon="🎧", layout="wide")

# CSS làm thanh tìm kiếm lung linh
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .stTextInput input { border-radius: 20px !important; background-color: #1a1a1a !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 TEETA GLOBAL MUSIC")

# Hàm lấy gợi ý từ YouTube
def get_suggestions(query):
    if not query: return []
    url = f"http://google.com{query}"
    response = requests.get(url)
    # Kết quả trả về dạng list lồng nhau, cần bóc tách
    import json
    import re
    search_results = re.findall(r'\

# 1. Ô tìm kiếm với gợi ý
query = st.text_input("Tìm kiếm bài hát:", placeholder="Gõ từ khóa để thấy gợi ý...", key="search_input")

# 2. Hiển thị danh sách gợi ý dưới dạng nút bấm nhanh
if query:
    suggestions = get_suggestions(query)
    if suggestions:
        st.write("🔍 **Gợi ý cho bạn:**")
        cols = st.columns(len(suggestions[:5])) # Hiện 5 gợi ý nhanh
        for i, tip in enumerate(suggestions[:5]):
            if cols[i].button(tip):
                # Khi bấm vào gợi ý, gán lại query bằng từ đó
                query = tip
                st.rerun()

# 3. Xử lý tìm kiếm chính
if query:
    st.divider()
    with st.spinner(f'🚀 Đang tìm danh sách cho: {query}...'):
        try:
            ydl_opts = {'format': 'best', 'noplaylist': True, 'quiet': True, 'default_search': 'ytsearch5'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                results = info['entries']

            for video in results:
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(video.get('thumbnail'), use_container_width=True)
                with col2:
                    st.markdown(f"### {video.get('title')}")
                    st.caption(f"👤 {video.get('uploader')} | ⏳ {video.get('duration_string')}")
                    st.video(video.get('webpage_url'))
                st.markdown("---")
        except:
            st.error("Lỗi rồi đại ca ơi!")

st.caption("© 2024 Teeta Studio - Search Suggestion Engine")
