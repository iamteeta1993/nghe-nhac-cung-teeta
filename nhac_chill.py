import streamlit as st
import random
from midiutil import MIDIFile
import io
import base64

st.set_page_config(page_title="Nghe Nhạc Cùng Teeta", page_icon="🎹", layout="wide")

st.title("🎹 Trình Sáng Tác Nhạc Trực Quan - Teeta")

# Cấu hình thanh bên
with st.sidebar:
    st.header("Cài đặt âm nhạc")
    tempo = st.slider("Tốc độ (BPM)", 60, 180, 120)
    notes_count = st.slider("Số lượng nốt", 16, 64, 32)
    st.info("Nhấn nút bên phải để bắt đầu!")

# Xử lý tạo nhạc
if st.button("🎼 SÁNG TÁC VÀ HIỆN BẢN NHẠC"):
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(0, 0, tempo)
    scale = [60, 62, 64, 65, 67, 69, 71, 72] # C Major
    
    time = 0
    for i in range(notes_count):
        pitch = random.choice(scale)
        duration = random.choice([0.5, 1])
        MyMIDI.addNote(0, 0, pitch, time, duration, 100)
        time += duration
    
    # Xuất dữ liệu ra Base64
    mem_file = io.BytesIO()
    MyMIDI.writeFile(mem_file)
    midi_b64 = base64.b64encode(mem_file.getvalue()).decode()

    # Nhúng thư viện Trực quan (Midi Player & Visualizer)
    player_html = f"""
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 15px; border: 2px solid #ff4b4b;">
        <script src="https://jsdelivr.net"></script>
        
        <midi-player 
            src="data:audio/midi;base64,{midi_b64}" 
            sound-font="https://googleapis.com" 
            visualizer="#myVisualizer">
        </midi-player>

        <div style="margin-top: 20px; background: white; border-radius: 10px;">
            <midi-visualizer type="piano-roll" id="myVisualizer" src="data:audio/midi;base64,{midi_b64}"></midi-visualizer>
        </div>
    </div>
    <style>
        midi-player {{ width: 100%; margin: 10px 0; }}
        midi-visualizer {{ width: 100%; height: 200px; }}
    </style>
    """
    
    st.components.v1.html(player_html, height=450)
    st.success("✅ Đã vẽ xong bản nhạc! Nhấn Play trên loa để nghe.")
    st.download_button("📥 Tải file .mid", mem_file.getvalue(), "teeta_music.mid")

st.markdown("---")
st.caption("Giao diện trực quan sử dụng thư viện HTML-MIDI-Player và Magenta.")
