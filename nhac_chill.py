import streamlit as st
import yt_dlp
import requests
import json

st.set_page_config(page_title="Teeta Global Music", page_icon="🎧", layout="wide")

# CSS Dark Mode đẳng cấp, làm thanh chọn (Selectbox) nhìn mượt hơn
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .stTextInput input { border-radius: 20px !important; background-color: #1a1a1a !important; color: white !important; }
    /* Tùy chỉnh màu cho Dropdown */
    div[data-baseweb="select"] > div { background-color: #1a1a1a !important; color: white !important; border-radius: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 TEETA GLOBAL MUSIC")

# --- HÀM LẤY GỢI Ý TỪ YOUTUBE ---
def get_suggestions(query):
    if not query or len(query) < 2: return []
    try:
        url = f"http://google.com{query}"
        response = requests.get(url, timeout=5)
        # Bóc tách dữ liệu JSON từ Google
        clean_text = response.text
        data = json.loads(clean_text)
        return [item[0] for item in data[1]]
    except:
        return []

# --- GIAO DIỆN TÌM KIẾM ---
search_input = st.text_input("Gõ tên bài hát để nhận gợi ý:", placeholder="Ví dụ: 'in', 'son tung'...", key="main_search")

suggestions = get_suggestions(search_input)

# Biến lưu từ khóa cuối cùng để tìm
final_query = ""

# Nếu có gợi ý thì hiện Dropdown ngay dưới thanh tìm kiếm
if suggestions:
    selected_option = st.selectbox(
        "✨ Gợi ý cho bạn (Chọn để tìm nhanh):",
        options=["-- Chọn một gợi ý bên dưới --"] + suggestions
    )
    if selected_option != "-- Chọn một gợi ý bên dưới --":
        final_query = selected_option
else:
    if search_input:
        final_query = search_input

# --- THỰC HIỆN TÌM KIẾM ---
if final_query:
    st.divider()
    with st.spinner(f'🚀 Đang lùng sục: {final_query}...'):
        try:
            ydl_opts = {'format': 'best', 'noplaylist': True, 'quiet': True, 'default_search': 'ytsearch5'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(final_query, download=False)
                results = info.get('entries', [])

            if results:
                st.subheader(f"🔍 Danh sách bài hát cho: {final_query}")
                for video in results:
                    with st.container():
                        c1, c2 = st.columns([1, 2])
                        with c1:
                            st.image(video.get('thumbnail'), use_container_width=True)
                        with c2:
                            st.markdown(f"#### {video.get('title')}")
                            st.caption(f"👤 {video.get('uploader')} | ⏳ {video.get('duration_string')}")
                            st.video(video.get('webpage_url'))
                        st.markdown("---")
        except Exception as e:
            st.error("Không tìm thấy nhạc, đại ca kiểm tra lại mạng nhé!")

st.caption("© 2026 Teeta Studio - Global Search Experience")
