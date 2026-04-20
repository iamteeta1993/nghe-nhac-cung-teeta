import streamlit as st
import yt_dlp

st.set_page_config(page_title="Teeta Global Music", page_icon="🎧", layout="wide")

# CSS giao diện Dark Mode cao cấp
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .stTextInput input { border-radius: 30px !important; background-color: #1a1a1a !important; color: white !important; border: 1px solid #333 !important; }
    .song-card { background-color: #111; padding: 15px; border-radius: 15px; border: 1px solid #222; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 TEETA GLOBAL MUSIC")
st.write("---")

query = st.text_input("", placeholder="🔍 Nhập tên bài hát hoặc nghệ sĩ bạn muốn tìm...")

if query:
    with st.spinner('🚀 Đang lùng sục danh sách nhạc...'):
        try:
            # Tìm kiếm 5 kết quả hàng đầu
            ydl_opts = {
                'format': 'best',
                'noplaylist': True,
                'quiet': True,
                'default_search': 'ytsearch5', # Lấy 5 bài
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                songs = info['entries']

            st.subheader(f"🔍 Danh sách tham khảo cho: '{query}'")
            
            # Hiển thị từng bài trong danh sách
            for song in songs:
                with st.container():
                    col1, col2 = st.columns([1, 2]) # Chia tỉ lệ 1:2
                    with col1:
                        st.image(song.get('thumbnail'), use_container_width=True)
                    with col2:
                        st.markdown(f"#### {song.get('title')}")
                        st.caption(f"👤 Kênh: {song.get('uploader')} | ⏳ Thời lượng: {song.get('duration_string')}")
                        # Trình phát ngay dưới mỗi bài
                        st.video(song.get('webpage_url'))
                    st.markdown("---")
                    
        except Exception as e:
            st.error("Không tìm thấy danh sách nhạc. Thử lại nhé đại ca!")
else:
    st.info("Hãy nhập tên bài hát để hiện danh sách gợi ý.")

st.caption("© 2024 Teeta Studio - Global Streaming Platform")
