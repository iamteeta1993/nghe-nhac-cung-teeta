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
    scale = [60, 62, 64, 65, 67, 69, 71, 72] # Đô Trưởng
    
    for i in range(32):
        pitch = random.choice(scale)
        MyMIDI.addNote(0, 0, pitch, i * 0.5, 0.5, 100)
    
    # Chuyển MIDI sang dữ liệu base64
    mem_file = io.BytesIO()
    MyMIDI.writeFile(mem_file)
    midi_data = mem_file.getvalue()
    b64_midi = base64.b64encode(midi_data).decode()

    st.success("✅ Đã sáng tác xong! Đợi 1 giây để loa hiện ra...")
    
    # 2. Nhúng trình phát nhạc MIDI xịn (Dùng bản ổn định hơn)
    midi_player_html = f"""
    <script src="https://jsdelivr.net"></script>
    <div style="background: #f0f2f6; padding: 20px; border-radius: 10px;">
        <midi-player 
            src="data:audio/midi;base64,{b64_midi}" 
            sound-font="https://googleapis.com" 
            visualizer="#myVisualizer">
        </midi-player>
        <div style="margin-top: 20px;">
            <midi-visualizer type="piano-roll" id="myVisualizer" src="data:audio/midi;base64,{b64_midi}"></midi-visualizer>
        </div>
    </div>
    """
    st.components.v1.html(midi_player_html, height=450)
    
    st.download_button("📥 Tải file .mid về máy", midi_data, "nhac_teeta.mid")

st.info("💡 Nếu không thấy loa, bạn hãy đợi vài giây để trình duyệt tải bộ tiếng Piano nhé!")
