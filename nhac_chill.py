import streamlit as st
import random
from midiutil import MIDIFile
import io

# --- CẤU HÌNH GIAO DIỆN WEB ---
st.set_page_config(page_title="Nghe Nhạc Cùng Teeta", page_icon="🎵")
st.title("🎵 Nghe Nhạc Cùng Teeta")
st.subheader("Phần mềm sáng tác nhạc tự động bằng AI & Code")

st.markdown("""
Chào mừng bạn! Hệ thống sẽ sử dụng thuật toán để chọn các nốt nhạc trong thang âm **C Major (Đô Trưởng)** 
để tạo ra một bản nhạc độc bản không trùng lặp.
""")

# --- THANH ĐIỀU CHỈNH ---
col1, col2 = st.columns(2)
with col1:
    tempo = st.slider("Tốc độ nhạc (BPM)", 60, 180, 120)
with col2:
    notes_count = st.select_slider("Số lượng nốt nhạc", options=[16, 32, 64], value=32)

# --- XỬ LÝ TẠO NHẠC ---
if st.button("🎼 BẮT ĐẦU SÁNG TÁC"):
    with st.spinner('Đang tính toán giai điệu...'):
        # Khởi tạo đối tượng MIDI
        MyMIDI = MIDIFile(1)
        track = 0
        time = 0
        MyMIDI.addTempo(track, time, tempo)

        # Thang âm Đô Trưởng (C4 đến C5)
        scale = [60, 62, 64, 65, 67, 69, 71, 72]
        
        # Thuật toán chọn nốt
        for i in range(notes_count):
            pitch = random.choice(scale) # AI chọn nốt
            duration = random.choice([0.5, 1]) # Nhịp ngắn hoặc dài
            volume = random.randint(80, 110) # Độ to nhỏ ngẫu nhiên cho tự nhiên
            
            MyMIDI.addNote(track, 0, pitch, time, duration, volume)
            time += duration

        # Chuyển dữ liệu MIDI vào bộ nhớ (để tải về trên web)
        mem_file = io.BytesIO()
        MyMIDI.writeFile(mem_file)
        
        st.success("✅ Bản nhạc của bạn đã sẵn sàng!")
        
        # Nút tải file
        st.download_button(
            label="📥 Tải bản nhạc (.mid) về máy",
            data=mem_file.getvalue(),
            file_name="nhac_cua_teeta.mid",
            mime="audio/midi"
        )
        
        st.balloons() # Hiệu ứng chúc mừng

st.info("💡 Mẹo: Bạn có thể kéo file .mid vừa tải về vào trang 'onlinesequencer.net' để nghe trực tiếp trên trình duyệt!")
