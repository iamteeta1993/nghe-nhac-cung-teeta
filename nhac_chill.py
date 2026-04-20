import streamlit as st
import random
from midiutil import MIDIFile
import io
import base64

st.set_page_config(page_title="Nghe Nhạc Cùng Teeta", page_icon="🎹", layout="wide")

st.title("🎹 Trình Sáng Tác Nhạc Trực Quan - Teeta")

# Thanh điều khiển bên trái
with st.sidebar:
    st.header("Cài đặt âm nhạc")
    tempo = st.slider("Tốc độ (BPM)", 60, 180, 120)
    notes_count = st.slider("Số lượng nốt", 16, 64, 32)

# Nút bấm chính
if st.button("🎼 SÁNG TÁC VÀ HIỆN BẢN NHẠC"):
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(0, 0, tempo)
    scale = [60, 62, 64, 65, 67, 69, 71, 72] # Đô Trưởng
    
    time = 0
    for i in range(notes_count):
        pitch = random.choice(scale)
        duration = random.choice([0.5, 1])
        MyMIDI.addNote(0, 0, pitch, time, duration, 100)
        time += duration
    
    # Xuất file ra định dạng Base64 để nhúng vào Web
    mem_file = io.BytesIO()
    MyMIDI.writeFile(mem_file)
    midi_b64 = base64.b64encode(mem_file.getvalue()).decode()

    # Giao diện hiển thị trực quan (SỬA LỖI KHOẢNG TRẮNG TẠI ĐÂY)
    player_html = f"""
    <div style="background-color: #000; padding: 20px; border-radius: 15px;">
        <script src="https://jsdelivr.net"></script>
        <midi-player 
            src="data:audio/midi;base64,{midi_b64}" 
            sound-font="https://googleapis.com" 
            visualizer="#myVisualizer">
        </midi-player>
        <midi-visualizer type="piano-roll" id="myVisualizer" src="data:audio/midi;base64,{midi_b64}"></midi-visualizer>
    </div>
    <style>
        midi-player {{ width: 100%; margin: 10px 0; background: #333; border-radius: 10px; }}
        midi-visualizer {{ width: 100%; height: 250px; background: #111; border-radius: 10px; }}
    </style>
    """
    
    st.components.v1.html(player_html, height=450)
    st.success("✅ Đã vẽ xong! Nhấn nút Play trên loa màu xám để nghe.")
    st.download_button("📥 Tải file .mid về máy", mem_file.getvalue(), "teeta_music.mid")

st.info("💡 Lưu ý: Đợi vài giây để trình duyệt tải bộ tiếng Piano lần đầu nhé.")
