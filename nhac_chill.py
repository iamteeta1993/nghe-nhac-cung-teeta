import streamlit as st
import os

st.set_page_config(page_title="Teeta Music Player", page_icon="🎧", layout="centered")

st.title("🎧 Teeta Music Player")
st.markdown("---")

# 1. Chức năng tải nhạc lên
uploaded_files = st.file_uploader("Chọn các file nhạc (MP3, WAV) của bạn:", type=['mp3', 'wav'], accept_multiple_files=True)

if uploaded_files:
    st.subheader(f"Danh sách phát ({len(uploaded_files)} bài)")
    
    for i, file in enumerate(uploaded_files):
        with st.expander(f"🎵 {file.name}"):
            # Hiển thị trình phát nhạc của trình duyệt
            st.audio(file, format='audio/mp3')
            
            # Hiển thị thông tin file
            file_details = {"Tên file": file.name, "Dung lượng": f"{file.size / 1024 / 1024:.2f} MB"}
            st.write(file_details)

else:
    st.info("Hãy kéo thả hoặc chọn file nhạc từ máy tính của bạn để bắt đầu nghe!")

# 2. Giao diện trang trí thêm
st.markdown("---")
st.caption("Ứng dụng nghe nhạc cá nhân phát triển bởi Teeta")
