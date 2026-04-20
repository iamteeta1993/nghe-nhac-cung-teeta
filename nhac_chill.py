import streamlit as st
import random
from midiutil import MIDIFile
import io
import base64

st.set_page_config(page_title="Nghe Nhạc Cùng Teeta", page_icon="🎵")
st.title("🎵 Nghe Nhạc Cùng Teeta")

# 1. Thuật toán tạo nhạc
tempo = st.slider("Tốc độ nhạc (BPM)", 60, 180, 120)

if st.button("🎼 SÁNG TÁC VÀ NGHE TRỰC TIẾP"):
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(0, 0, tempo)
    scale = [60, 62, 64, 65, 67, 69, 71, 72]
    
    for i in range(32):
        pitch = random.choice(scale)
        MyMIDI.addNote(0, 0, pitch, i * 0.5, 0.5, 100)
    
    # Chuyển MIDI sang dữ liệu base64 để trình phát Web đọc được
    mem_file = io.BytesIO()
    MyMIDI.writeFile(mem_file)
    midi_data = mem_file.getvalue()
    b64_midi = base64.b64encode(midi_data).decode()

    # 2. Nhúng trình phát nhạc MIDI bằng JavaScript (Nghe trực tiếp trên trình duyệt)
    st.success("✅ Đã sáng tác xong! Bạn nhấn Play ở dưới để nghe nhé:")
    
    # Sử dụng thư viện ngoài để phát nhạc trực tiếp
    midi_player_html = f"""
    <script src="https://jsdelivr.net"></script>
    <midi-player src="data:audio/midi;base64,{b64_midi}" sound-font visualizer="#myVisualizer"></midi-player>
    <midi-visualizer type="piano-roll" id="myVisualizer" src="data:audio/midi;base64,{b64_midi}"></midi-visualizer>
    """
    st.components.v1.html(midi_player_html, height=400)
    
    st.download_button("📥 Tải file .mid về máy", midi_data, "nhac_teeta.mid")

st.info("💡 Trình phát này sẽ giả lập tiếng Piano để bạn nghe trực tiếp trên Web!")
