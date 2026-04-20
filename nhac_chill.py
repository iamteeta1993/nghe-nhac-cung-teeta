import streamlit as st
import yt_dlp
import requests
import json

st.set_page_config(page_title="Teeta YouTube", page_icon="❤️", layout="wide")

# CSS "Nhái" giao diện YouTube đẳng cấp
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: white; }
    .stTextInput input { border-radius: 40px !important; background-color: #121212 !important; color: white !important; border: 1px solid #333 !important; padding-left: 20px !important; }
    /* Sidebar và Card bài hát bên phải */
    .side-card { background-color: #121212; border-radius: 10px; padding: 5px; margin-bottom: 10px; display: flex; gap: 10px; cursor: pointer; }
    .side-card:hover { background-color: #272727; }
    </style>
    """, unsafe_allow_html=True)

# --- THANH TÌM KIẾM TRÊN CÙNG ---
col_logo, col_search, col_user = st.columns([1, 4, 1])
with col_logo:
    st.markdown("### ❤️ **YouTube**")
with col_search:
    search_input = st.text_input("", placeholder="Tìm kiếm", key="yt_search")
with col_user:
    st.markdown("👤")

# --- HÀM LẤY GỢI Ý (DROPDOWN) ---
def get_suggestions(query):
    if not query: return []
    try:
        url = f"http://google.com{query}"
        response = requests.get(url, timeout=5)
        clean_text = response.text
        return json.loads(clean_text)
    except: return []

suggestions = get_suggestions(search_input)
final_query = ""

if suggestions:
    selected = st.selectbox("Gợi ý từ YouTube:", options=["-- Chọn từ khóa --"] + suggestions)
    if selected != "-- Chọn từ khóa --": final_query = selected
elif search_input:
    final_query = search_input

# --- LAYOUT YOUTUBE: VIDEO CHÍNH (TRÁI) & DANH SÁCH (PHẢI) ---
if final_query:
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch10'}) as ydl:
            results = ydl.extract_info(final_query, download=False)['entries']
        
        main_video = results[0] # Bài đầu tiên làm video chính
        side_videos = results[1:] # Các bài còn lại làm danh sách bên phải

        col_main, col_side = st.columns([3, 1.2])

        with col_main:
            # Video chính to đùng
            st.video(main_video['webpage_url'])
            st.subheader(main_video['title'])
            st.write(f"👤 {main_video['uploader']} | 👁️ {main_video.get('view_count', 0):,} lượt xem")
            st.markdown("---")
            st.write("📝 **Mô tả:**")
            st.caption(main_video.get('description', 'Không có mô tả')[:200] + "...")

        with col_side:
            st.write("**Video liên quan**")
            for vid in side_videos:
                # Hiển thị danh sách bên phải dạng card nhỏ
                with st.container():
                    c1, c2 = st.columns([1, 1.2])
                    with c1:
                        st.image(vid['thumbnail'], use_container_width=True)
                    with c2:
                        st.markdown(f"**{vid['title'][:40]}...**")
                        st.caption(f"{vid['uploader']}")
                    # Nút để chuyển bài chính (dùng tạm nút bấm)
                    if st.button("Xem bài này", key=vid['id']):
                        st.session_state['yt_search'] = vid['title']
                        st.rerun()

    except:
        st.error("Lỗi tải nhạc rồi đại ca!")
else:
    st.info("Nhập tên bài hát phía trên để trải nghiệm giao diện YouTube!")

st.caption("Design by Teeta Studio - YouTube Clone Project")
