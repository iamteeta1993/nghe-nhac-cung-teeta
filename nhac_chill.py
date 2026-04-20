import streamlit as st
from youtubesearchpython import VideosSearch

# Cấu hình giao diện đẳng cấp
st.set_page_config(page_title="Teeta Global Music", page_icon="🔥", layout="wide")

# CSS tùy chỉnh để làm giao diện đẹp hơn
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTextInput>div>div>input { background-color: #262730; color: white; border-radius: 20px; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #FF4B4B; color: white; }
    .song-card { background-color: #161b22; padding: 15px; border-radius: 15px; border: 1px solid #30363d; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Teeta Global Music Player")
st.subheader("Tìm kiếm và phát nhạc trực tuyến từ kho tàng thế giới")

# Thanh tìm kiếm
query = st.text_input("", placeholder="Nhập tên bài hát hoặc nghệ sĩ bạn muốn nghe...")

if query:
    with st.spinner('Đang lùng sục kho nhạc thế giới...'):
        search = VideosSearch(query, limit=5)
        results = search.result()['result']

    if not results:
        st.error("Không tìm thấy bài này, thử tên khác xem sao đại ca!")
    else:
        st.write(f"🔍 Kết quả tìm kiếm cho: **{query}**")
        
        # Hiển thị kết quả dạng lưới
        for video in results:
            with st.container():
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(video['thumbnails'][0]['url'], use_container_width=True)
                with col2:
                    st.markdown(f"### {video['title']}")
                    st.write(f"👤 Kênh: {video['channel']['name']} | ⏳ Thời lượng: {video['duration']}")
                    
                    # Phát nhạc trực tiếp bằng iframe Youtube (không cần tải lên)
                    video_id = video['id']
                    st.video(f"https://youtube.com{video_id}")
                st.markdown("---")
else:
    # Giao diện khi chưa tìm kiếm
    st.info("💡 Mẹo: Gõ 'Lofi hip hop' hoặc 'Sơn Tùng MTP' để bắt đầu chill.")
    
    # Gợi ý nhạc xu hướng
    st.write("### 🌍 Xu hướng hôm nay")
    cols = st.columns(3)
    trending = ["Em xinh - Mono", "Perfect - Ed Sheeran", "Chúng ta của tương lai"]
    for i, song in enumerate(trending):
        if cols[i].button(song):
            st.rerun()

st.caption("© 2024 Teeta Music Entertainment - World Class UI")
