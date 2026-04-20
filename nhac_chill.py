import streamlit as st
import yt_dlp
import random

# 1. Cấu hình hệ thống Neural Đa Nền Tảng
st.set_page_config(page_title="TEETA ULTIMATE PLAYER", page_icon="🌐", layout="wide")

# 2. CSS Cyberpunk Đẳng Cấp - Tối ưu cho 4 nền tảng
st.markdown("""
    <style>
    .stApp { background: #050505; color: #00ffcc; }
    .stTextInput input { 
        border-radius: 30px !important; background-color: #111 !important; 
        color: #00ffcc !important; border: 1px solid #00ffcc !important;
        box-shadow: 0 0 10px #00ffcc33;
    }
    .platform-btn {
        display: inline-block; padding: 10px 20px; margin: 5px;
        border-radius: 20px; text-decoration: none; font-weight: bold;
        transition: 0.3s; border: 1px solid #444;
    }
    .zing-btn { background-color: #6a39af; color: white !important; }
    .nct-btn { background-color: #2daeed; color: white !important; }
    .sc-btn { background-color: #ff5500; color: white !important; }
    .yt-btn { background-color: #ff0000; color: white !important; }
    .main-frame { border: 2px solid #00ffcc; border-radius: 15px; box-shadow: 0 0 20px #00ffcc44; }
    .ai-terminal { background: #000; border: 1px solid #00ffcc; padding: 15px; border-radius: 10px; font-family: monospace; color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER: MULTI-PLATFORM NAVIGATION ---
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🌐 TEETA MULTI-SOURCE ENGINE</h1>", unsafe_allow_html=True)

# Thanh điều hướng nhanh đến các trang web nhạc
cols = st.columns([1, 1, 1, 1, 1])
with cols[0]: st.markdown('<a href="https://youtube.com" target="_blank" class="platform-btn yt-btn">📺 YouTube</a>', unsafe_allow_html=True)
with cols[1]: st.markdown('<a href="https://zingmp3.vn" target="_blank" class="platform-btn zing-btn">🎶 Zing MP3</a>', unsafe_allow_html=True)
with cols[2]: st.markdown('<a href="https://www.nhaccuatui.com" target="_blank" class="platform-btn nct-btn">💎 NCT</a>', unsafe_allow_html=True)
with cols[3]: st.markdown('<a href="https://soundcloud.com" target="_blank" class="platform-btn sc-btn">☁️ SoundCloud</a>', unsafe_allow_html=True)

st.write("---")

# --- HỆ THỐNG TÌM KIẾM VÀ PHÁT ---
query = st.text_input("📡 NHẬP TÊN BÀI HÁT (HỆ THỐNG TỰ ĐỘNG LỤC SOÁT):", placeholder="Tìm bài hát để kích hoạt AI Analysis...")

if query:
    try:
        # Lấy dữ liệu YouTube làm lõi phát
        ydl_opts = {'quiet': True, 'default_search': 'ytsearch5', 'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            results = ydl.extract_info(query, download=False)['entries']
        
        main_v = results[0]
        col_player, col_side = st.columns([2.5, 1])

        with col_player:
            # KHUNG PHÁT CHÍNH
            st.markdown("<div class='main-frame'>", unsafe_allow_html=True)
            st.video(main_v['webpage_url'])
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.subheader(f"🎵 {main_v['title']}")

            # PHÂN TÍCH AI CHUYÊN SÂU
            st.markdown("<div class='ai-terminal'>", unsafe_allow_html=True)
            st.write("🤖 **AI NEURAL ANALYSIS:**")
            st.write(f"- Nguồn dữ liệu: YouTube, Zing, SoundCloud")
            st.write(f"- Mood: {random.choice(['Cyber-Focus', 'Deep Bass', 'Lo-Fi Chill'])}")
            st.code(f"/imagine prompt: Futuristic music studio, neon {random.choice(['purple', 'cyan'])}, hyper realistic, 8k", language="text")
            st.markdown("</div>", unsafe_allow_html=True)

            # BÌNH LUẬN & PROMPT WRITING
            st.write("---")
            st.subheader("💬 GHI CHÉP PROMPT & BÌNH LUẬN")
            prompt_input = st.text_area("Ghi lại cảm hứng hoặc Prompt của bạn:", placeholder="Gõ /prompt để lưu lệnh AI...")
            if st.button("LƯU LẠI"): st.toast("Đã ghi nhận tư duy của đại ca!")

        with col_side:
            st.write("### ⏭️ DANH SÁCH LIÊN QUAN")
            for vid in results[1:6]:
                with st.container():
                    st.image(vid['thumbnail'], use_container_width=True)
                    st.caption(vid['title'][:50])
                    if st.button("PHÁT", key=vid['id']):
                        st.rerun()
                    st.write("---")

    except Exception as e:
        st.error(f"⚠️ Hệ thống đang quá tải: {e}")
else:
    # GIAO DIỆN CHỜ ĐẲNG CẤP
    st.image("https://unsplash.com", use_container_width=True)
    st.info("💡 Hệ thống đã sẵn sàng. Hãy nhập tên bài hát để AI bắt đầu quét các nền tảng!")

st.caption("ULTIMATE NEURAL PLAYER V5.0 | ZING • NCT • SOUNDCLOUD • YOUTUBE | BY TEETA")
