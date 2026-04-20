    # Đoạn code mới cho phần hiển thị trực quan
    player_html = f"""
    <div style="background-color: #000; padding: 20px; border-radius: 15px; border: 1px solid #444;">
        <!-- Tải thư viện âm thanh tổng hợp -->
        <script src="https://jsdelivr.net"></script>
        
        <midi-player 
            src="data:audio/midi;base64,{midi_b64}" 
            sound-font="https://googleapis.com" 
            visualizer="#myVisualizer">
        </midi-player>

        <midi-visualizer type="piano-roll" id="myVisualizer" 
            src="data:audio/midi;base64,{midi_b64}">
        </midi-visualizer>
    </div>
    
    <style>
        midi-player {{
            display: block;
            width: 100%;
            margin: 10px 0;
            background: #222;
            border-radius: 8px;
        }}
        midi-visualizer {{
            display: block;
            width: 100%;
            height: 250px;
            background: #111;
            border-radius: 8px;
            margin-top: 10px;
        }}
        /* Chỉnh màu các nốt nhạc cho rực rỡ */
        midi-visualizer .note.active {{ fill: #00ff00 !important; }}
    </style>
    """
    st.components.v1.html(player_html, height=450)
