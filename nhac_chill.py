import streamlit as st
import yt_dlp

st.set_page_config(page_title="Teeta Global Music", page_icon="🎧", layout="wide")

# CSS Dark Mode đẳng cấp
st.markdown("<style>.stApp {background-color: #000; color: white;}</style>", unsafe_allow_html=True)

st.title("🎧 TEETA GLOBAL MUSIC")

query = st.text_input("", placeholder="🔍 Nhập tên bài hát hoặc nghệ sĩ...")

if query:
    with st.spinner('🚀 Đang tìm nhạc...'):
        try:
            # Tìm kiếm video trên Youtube
            ydl_opts = {'format': 'best', 'noplaylist': True, 'quiet': True, 'default_search': 'ytsearch1'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                video_url = info['entries'][0]['webpage_url']
                video_title = info['entries'][0]['title']

            st.success(f"🎵 Đang phát: {video_title}")
            
            # Sử dụng trình phát video chính chủ của Streamlit (Cực kỳ ổn định)
            st.video(video_url)
            
        except Exception as e:
            st.error("Không tìm thấy bài hát này. Đại ca thử nhập tên khác nhé!")
else:
    st.info("Nhập tên bài hát để bắt đầu phiêu!")

st.caption("© 2024 Teeta Studio - Global Streaming Platform")
