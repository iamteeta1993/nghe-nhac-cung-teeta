import streamlit as st
import yt_dlp

st.set_page_config(page_title="Teeta YouTube", page_icon="📺", layout="wide")

# CSS "Độ" thanh search dính liền khối & Giao diện chuẩn YouTube
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: white; }
    
    /* Gộp ô nhập và nút search thành một khối */
    div[data-testid="stHorizontalBlock"] .stTextInput input {
        border-radius: 40px 0 0 40px !important;
        background-color: #121212 !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-right: none !important;
        height: 40px !important;
    }
    
    div[data-testid="stHorizontalBlock"] button {
        border-radius: 0 40px 40px 0 !important;
        background-color: #222 !important;
        border: 1px solid #333 !important;
        height: 40px !important;
        width: 65px !important;
        margin-left: -30px !important; /* Kéo nút dính vào ô input */
    }

    .mic-btn {
        background-color: #181818;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-left: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER CHUẨN ---
col_logo, col_search, col_mic, col_user = st.columns([1, 4, 0.5, 0.5])

with col_logo:
    st.markdown("<h3 style='margin:0;'>🔴 YouTube</h3>", unsafe_allow_html=True)

with col_search:
    # Ô tìm kiếm
    query = st.text_input("", placeholder="Tìm kiếm", label_visibility="collapsed")

with col_mic:
    # Nút tìm kiếm giả lập dính liền (dùng phím Enter để kích hoạt)
    st.button("🔍")

with col_mic:
    st.markdown('<div class="mic-btn">🎤</div>', unsafe_allow_html=True)

# --- XỬ LÝ DỮ LIỆU ---
if query:
    try:
        with st.spinner('🚀 Đang tìm nhạc...'):
            ydl_opts = {'quiet': True, 'default_search': 'ytsearch10', 'extract_flat': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                results = ydl.extract_info(query, download=False)['entries']
            
            main_v = results[0]
            col_main, col_side = st.columns([2.8, 1.2])

            with col_main:
                st.video(f"https://youtube.com{main_v['id']}")
                st.subheader(main_v['title'])
                st.write(f"👤 {main_v.get('uploader', 'YouTube Player')}")
                
                with st.expander("🤖 AI ANALYSIS & COMMENTS"):
                    st.code(f"/imagine prompt: Cinematic visual for {query}, 8k, neon style", language="text")
                    st.text_area("Ghi chú Prompt của đại ca:", placeholder="Nhập tại đây...")

            with col_side:
                st.write("⏭️ **Tiếp theo**")
                for vid in results[1:8]:
                    c_t, c_i = st.columns([1, 1.5])
                    with c_t:
                        st.image(f"https://ytimg.com{vid['id']}/mqdefault.jpg", use_container_width=True)
                    with c_i:
                        st.markdown(f"<p style='font-size:12px; font-weight:bold;'>{vid['title'][:40]}...</p>", unsafe_allow_html=True)
                        if st.button("Xem", key=vid['id']):
                            st.rerun()
    except Exception as e:
        st.error("⚠️ Không tìm thấy bài hát. Đại ca kiểm tra lại tên bài nhé!")
else:
    st.image("https://unsplash.com")

st.caption("Teeta YouTube - Fixed UI & Search Engine v11.0")
