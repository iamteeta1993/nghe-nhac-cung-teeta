import streamlit as st

st.set_page_config(page_title="Teeta Music Global", page_icon="🎧", layout="wide")

# CSS cho giao diện sang chảnh
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .stTextInput input {
        border-radius: 30px !important;
        background-color: #1a1a1a !important;
        color: white !important;
        border: 2px solid #FF4B4B !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 TEETA GLOBAL MUSIC")

query = st.text_input("", placeholder="🔍 Nhập tên bài hát...")

if query:
    # Fix lỗi link bằng cách format lại từ khóa chuẩn URL
    clean_query = query.replace(" ", "+")
    
    st.success(f"Đã tìm thấy bài hát: {query}")
    
    # Sử dụng link nhúng YouTube chuẩn (embed)
    video_url = f"https://youtube.com{clean_query}"
    
    # Hiển thị trình phát
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <iframe width="100%" height="500" 
                src="{video_url}" 
                frameborder="0" 
                allow="autoplay; encrypted-media" 
                allowfullscreen 
                style="border-radius: 20px; border: 2px solid #333;">
            </iframe>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Lưu ý: Nếu khung nhạc hiện 'YouTube từ chối kết nối', hãy nhấn vào nút Tải lại trang nhé.")
else:
    st.write("Nhập tên bài hát để bắt đầu bữa tiệc âm nhạc!")

st.caption("© 2024 Teeta Studio")
