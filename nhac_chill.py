import streamlit as st
import yt_dlp

st.set_page_config(page_title="Teeta Speed Player", page_icon="⚡", layout="wide")

# CSS tối giản để tăng tốc độ render giao diện
st.markdown("<style>.stApp {background-color: #0f0f0f; color: white;} .stVideo {border-radius: 15px;}</style>", unsafe_allow_html=True)

# --- HÀM TÌM KIẾM SIÊU TỐC ---
@st.cache_data(ttl=3600) # Lưu kết quả trong 1 giờ để không phải load lại
def get_fast_music(search_query):
    ydl_opts = {
        'format': 'bestaudio/best', # Chỉ ưu tiên lấy luồng âm thanh/video nhẹ nhất
        'noplaylist': True,
        'quiet': True,
        'extract_flat': True, # Chiêu này giúp lấy danh sách cực nhanh mà không cần vào sâu từng video
        'default_search': 'ytsearch8',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(search_query, download=False)['entries']

st.markdown("<h2 style='color: red;'>⚡ TEETA SPEED PLAYER</h2>", unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Nhập tên bài hát... (Tìm nhanh gấp 3 lần)", label_visibility="collapsed")

if query:
    try:
        results = get_fast_music(query)
        main_v = results[0]
        
        col_left, col_right = st.columns([2.8, 1.2])

        with col_left:
            # Phát ngay bài đầu tiên - Sử dụng link trực tiếp để tránh load vòng
            st.video(f"https://youtube.com{main_v['id']}")
            st.subheader(main_v['title'])
            st.caption(f"👤 Nguồn: {main_v.get('uploader', 'YouTube')}")
            
            # Phần AI Prompts làm đơn giản để không tốn tài nguyên
            with st.expander("🤖 AI Prompt"):
                st.code(f"/imagine prompt: Visual of {query}, futuristic, 8k", language='text')

        with col_right:
            st.write("⏭️ **Tiếp theo**")
            for vid in results[1:]:
                # Dùng ảnh thumbnail chất lượng thấp (mqdefault) để load danh sách nhanh hơn
                thumb = f"https://ytimg.com{vid['id']}/mqdefault.jpg"
                c1, c2 = st.columns([1, 1.5])
                with c1:
                    st.image(thumb, use_container_width=True)
                with c2:
                    st.markdown(f"<p style='font-size:12px;'>{vid['title'][:40]}...</p>", unsafe_allow_html=True)
                    if st.button("Nghe", key=vid['id']):
                        st.rerun()
    except:
        st.error("⚠️ Server YouTube đang nghẽn, đại ca đợi 2 giây rồi gõ lại nhé!")
else:
    st.info("Nhập tên bài hát để thấy tốc độ bàn thờ!")

st.caption("TEETA SPEED ENGINE V9.0 | OPTIMIZED FOR 2026")
