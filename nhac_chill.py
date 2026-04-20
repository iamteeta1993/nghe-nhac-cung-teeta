import streamlit as st
import yt_dlp

st.set_page_config(page_title="Teeta YouTube", page_icon="🎧", layout="wide")

# CSS "Độ" thanh tìm kiếm chuẩn YouTube: Bo góc, nút search riêng, Micro
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: white; }
    
    /* Căn giữa thanh search */
    .search-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
        gap: 10px;
    }

    /* Bo góc và style ô input */
    .stTextInput input {
        border-radius: 40px 0 0 40px !important;
        background-color: #121212 !important;
        color: white !important;
        border: 1px solid #333 !important;
        height: 40px !important;
        padding-left: 20px !important;
        width: 500px !important;
    }

    /* Nút kính lúp chuẩn YouTube */
    div.stButton > button {
        border-radius: 0 40px 40px 0 !important;
        background-color: #222 !important;
        border: 1px solid #333 !important;
        height: 40px !important;
        width: 60px !important;
        margin-left: -16px !important;
        color: white !important;
    }

    /* Nút Micro tròn bên cạnh */
    .mic-icon {
        background-color: #181818;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- GIAO DIỆN THANH SEARCH CHUẨN ---
col_logo, col_search, col_user = st.columns([1, 4, 1])

with col_logo:
    st.markdown("<h3 style='color: white; margin: 0;'>🔴 YouTube</h3>", unsafe_allow_html=True)

with col_search:
    # Chia nhỏ trong cột search để làm nút sát nhau
    c1, c2, c3 = st.columns([5, 1, 1])
    with c1:
        query = st.text_input("", placeholder="Tìm kiếm", label_visibility="collapsed")
    with c2:
        search_trigger = st.button("🔍")
    with c3:
        st.markdown('<div class="mic-icon">🎤</div>', unsafe_allow_html=True)

# --- XỬ LÝ LOAD NHẠC SIÊU TỐC ---
if query:
    try:
        ydl_opts = {'quiet': True, 'default_search': 'ytsearch10', 'extract_flat': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            results = ydl.extract_info(query, download=False)['entries']
        
        main_v = results[0]
        col_main, col_side = st.columns([2.8, 1.2])

        with col_main:
            # Video chính to rõ
            st.video(f"https://youtube.com{main_v['id']}")
            st.subheader(main_v['title'])
            st.write(f"👤 {main_v.get('uploader', 'N/A')}")
            
            # Phần AI Prompts và Bình luận lồng vào nhau cho gọn
            with st.expander("🤖 PHÂN TÍCH AI & BÌNH LUẬN"):
                st.code(f"/imagine prompt: {query}, cinematic style, 8k", language="text")
                st.text_area("Ghi chú/Prompt của bạn:", placeholder="Ghi tại đây...")

        with col_side:
            st.write("⏭️ **Tiếp theo**")
            for vid in results[1:7]:
                c_thumb, c_info = st.columns([1, 1.5])
                with c_thumb:
                    st.image(f"https://ytimg.com{vid['id']}/mqdefault.jpg", use_container_width=True)
                with c_info:
                    st.markdown(f"<p style='font-size:12px;'>{vid['title'][:45]}...</p>", unsafe_allow_html=True)
                    if st.button("Nghe", key=vid['id']):
                        st.rerun()
    except:
        st.error("⚠️ Không tìm thấy bài hát. Thử lại nhé đại ca!")
else:
    st.info("💡 Nhập tên bài hát vào thanh tìm kiếm bo góc phía trên!")

st.caption("Teeta YouTube UI v10.0 - Optimized Search Bar")
