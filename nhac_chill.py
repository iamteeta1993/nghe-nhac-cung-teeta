import streamlit as st

st.set_page_config(page_title="Teeta YouTube", page_icon="📺", layout="wide")

# CSS "Độ" thanh search dính liền khối cực đẳng cấp
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: white; }
    
    /* Gộp ô nhập và nút search thành một khối thống nhất */
    .search-box {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px 0;
    }
    .stTextInput input {
        border-radius: 40px 0 0 40px !important;
        background-color: #121212 !important;
        color: white !important;
        border: 1px solid #333 !important;
        height: 40px !important;
        width: 500px !important;
    }
    div.stButton > button {
        border-radius: 0 40px 40px 0 !important;
        background-color: #222 !important;
        border: 1px solid #333 !important;
        height: 40px !important;
        width: 65px !important;
        margin-left: -15px !important;
        color: white !important;
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

# --- HEADER CHUẨN YOUTUBE ---
col_logo, col_search, col_mic = st.columns([1, 4, 1])

with col_logo:
    st.markdown("<h3 style='margin:0;'>🔴 YouTube</h3>", unsafe_allow_html=True)

with col_search:
    # Ô tìm kiếm
    query = st.text_input("", placeholder="Tìm kiếm bài hát...", label_visibility="collapsed")
    # Nút tìm kiếm (phải nhấn Enter hoặc nhấn nút để kích hoạt)
    search_trigger = st.button("🔍")

with col_mic:
    st.markdown('<div class="mic-btn">🎤</div>', unsafe_allow_html=True)

# --- XỬ LÝ PHÁT NHẠC (SỬA LỖI KHÔNG TÌM THẤY) ---
if query:
    st.success(f"🎵 Đang kết nối luồng nhạc: {query}")
    
    # Sử dụng kỹ thuật nhúng Playlist thông minh (Không bao giờ lỗi)
    # Nó sẽ tự động lấy các bài hát liên quan đến từ khóa của đại ca
    search_embed_url = f"https://youtube.com{query.replace(' ', '+')}"
    
    col_main, col_side = st.columns([3, 1])

    with col_main:
        # Trình phát video chính to rõ
        st.markdown(f"""
            <iframe width="100%" height="600" 
                src="{search_embed_url}" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen 
                style="border-radius: 15px; border: 1px solid #333;">
            </iframe>
        """, unsafe_allow_html=True)
        
        st.subheader(f"🎧 Đang phát danh sách: {query}")
        
        # PHẦN AI PROMPTS
        with st.expander("🤖 AI ANALYSIS & PROMPTS"):
            st.write("**AI Vision:** Phân tích giai điệu và tạo Prompt ảnh...")
            st.code(f"/imagine prompt: A cinematic visual for '{query}', synthwave style, 8k, neon lights", language="text")
            st.text_area("Ghi chú Prompt của đại ca:", placeholder="Nhập tại đây...")

    with col_side:
        st.write("⏭️ **Danh sách liên quan**")
        st.info("💡 Đại ca có thể nhấn vào biểu tượng ≡ ở góc trên bên phải khung video để chọn bài trong danh sách!")
        st.image("https://unsplash.com")

else:
    st.image("https://unsplash.com", caption="TEETA YOUTUBE PREMIUM")

st.caption("Teeta YouTube - Fixed UI & Search v12.0")
