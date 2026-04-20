import streamlit as st

# Cấu hình giao diện chuẩn Dark Mode quốc tế
st.set_page_config(page_title="Teeta Global Music", page_icon="🔥", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .stTextInput input {
        background-color: #1a1a1a !important;
        color: white !important;
        border-radius: 50px !important;
        border: 2px solid #FF4B4B !important;
        padding: 15px 30px !important;
        font-size: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 TEETA GLOBAL MUSIC PLAYER")
st.write("### 🌍 Tìm là thấy - Nhấn là phiêu")

# Thanh tìm kiếm "độc bản"
query = st.text_input("", placeholder="🔍 Nhập tên bài hát hoặc nghệ sĩ (ví dụ: 'Skyline' hoặc 'Lofi chill')...")

if query:
    st.success(f"🎵 Đang tạo danh sách phát đẳng cấp cho: {query}")
    
    # Kỹ thuật nhúng Playlist thông minh từ từ khóa tìm kiếm
    search_url = f"https://youtube.com{query.replace(' ', '+')}"
    
    # Khung phát nhạc bo góc đẳng cấp
    st.markdown(f"""
        <div style="display: flex; justify-content: center; background: #111; padding: 10px; border-radius: 20px; border: 1px solid #333;">
            <iframe width="100%" height="600" 
                src="{search_url}" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen 
                style="border-radius: 15px;">
            </iframe>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Bạn có thể nhấn vào biểu tượng ≡ ở góc trên bên phải khung nhạc để chọn các bài khác trong danh sách!")
else:
    st.image("https://unsplash.com", use_container_width=True)
    st.write("---")
    st.write("### 🎤 Gợi ý cho bạn:")
    col1, col2, col3 = st.columns(3)
    with col1: st.code("Sơn Tùng MTP")
    with col2: st.code("Lofi hip hop radio")
    with col3: st.code("Global Top 50")

st.caption("© 2024 Teeta Studio | World Class Streaming System")
