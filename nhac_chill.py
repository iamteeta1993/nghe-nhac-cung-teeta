import streamlit as st
import yt_dlp
import random
import time

# Cấu hình hệ thống Neural
st.set_page_config(page_title="TEETA NEURAL PLAYER", page_icon="🧠", layout="wide")

# Giao diện khác biệt hoàn toàn - Phong cách Cyberpunk Dark Mode
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #0d1117 0%, #000000 100%); color: #58a6ff; }
    .stTextInput input { 
        border-radius: 10px !important; background-color: #0d1117 !important; 
        color: #58a6ff !important; border: 1px solid #1f6feb !important;
        box-shadow: 0 0 15px #1f6feb33;
    }
    .main-player { border: 2px solid #1f6feb; border-radius: 20px; overflow: hidden; box-shadow: 0 0 30px #1f6feb44; }
    .ai-terminal { 
        background-color: #010409; border: 1px solid #238636; padding: 15px; 
        border-radius: 10px; font-family: 'Courier New', monospace; color: #39ff14;
    }
    .comment-card { background: #161b22; border-radius: 10px; padding: 15px; border-left: 5px solid #8957e5; margin-top: 10px; }
    .sidebar-vid { transition: 0.3s; cursor: pointer; border-radius: 10px; padding: 5px; }
    .sidebar-vid:hover { background: #1f6feb22; transform: translateX(5px); }
    </style>
    """, unsafe_allow_html=True)

# --- NEURAL HEADER ---
st.markdown("<h1 style='text-align: center; color: #58a6ff; text-shadow: 0 0 20px #1f6feb;'>🧠 TEETA NEURAL MUSIC ENGINE</h1>", unsafe_allow_html=True)

query = st.text_input("📡 TRUY VẤN HỆ THỐNG:", placeholder="Nhập tần số âm nhạc hoặc tên nghệ sĩ...")

if query:
    try:
        with st.status("🛸 Đang huy động các AI tìm kiếm bài hát...", expanded=False) as status:
            ydl_opts = {'quiet': True, 'default_search': 'ytsearch10', 'format': 'best'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                results = info['entries']
            status.update(label="✅ Kết nối thành công!", state="complete")

        main_v = results[0]
        
        # CHIA LAYOUT: TỐI ƯU TRẢI NGHIỆM NGHE NHÌN
        col_player, col_neural = st.columns([2.5, 1])

        with col_player:
            # KHUNG PHÁT NHẠC ĐẲNG CẤP
            st.markdown("<div class='main-player'>", unsafe_allow_html=True)
            st.video(main_v['webpage_url'])
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.title(f"🎵 {main_v['title']}")
            
            # PHÂN TÍCH CHUYÊN SÂU TỪ AI (KHÁC BIỆT)
            with st.expander("🤖 XEM PHÂN TÍCH NEURAL PROMPTS", expanded=True):
                st.markdown("<div class='ai-terminal'>", unsafe_allow_html=True)
                st.markdown(f"> **Hệ thống phân tích:** {main_v['title']}")
                st.markdown(f"> **Mood Core:** {random.choice(['Ethereal', 'Cyber-Vibe', 'High-Fidelity', 'Melancholy Digital'])}")
                st.markdown("> **Generated Prompts for Stable Diffusion:**")
                st.code(f"/imagine prompt: A holographic representation of {query}, futuristic city, rainy night, synthwave aesthetic, 16k, hyper-detailed --ar 16:9", language="text")
                st.markdown("> **Neural Status:** Bản nhạc phù hợp để kích thích sóng não Gamma.")
                st.markdown("</div>", unsafe_allow_html=True)

            # HỆ THỐNG BÌNH LUẬN & GHI PROMPT (DƯỚI BÀI HÁT)
            st.write("---")
            st.subheader("💬 PHẢN HỒI HỆ THỐNG & PROMPT WRITING")
            c_input = st.text_area("Nhập Prompt hoặc bình luận của bạn tại đây:", placeholder="Ghi nhận tư duy âm nhạc của đại ca...")
            if st.button("KÍCH HOẠT GỬI"):
                st.balloons()
                st.success("Hệ thống đã tiếp nhận dữ liệu!")

            # MOCKUP BÌNH LUẬN CHẤT LƯỢNG
            for m in [("Neural_Bot", "Nhịp điệu này đạt tần số 432Hz."), ("Teeta_Admin", "Code đã chạy xong, thưởng thức thôi!")]:
                st.markdown(f"<div class='comment-card'><strong>{m[0]}</strong>: {m[1]}</div>", unsafe_allow_html=True)

        with col_player: # Thêm phần bình luận lùi xuống
            pass

        with col_neural:
            st.markdown("### 📡 CÁC TẦN SỐ LIÊN QUAN")
            for vid in results[1:8]:
                st.markdown(f"""
                <div class='sidebar-vid'>
                    <img src="{vid['thumbnail']}" style='width:100%; border-radius:10px;'>
                    <p style='font-size:14px; font-weight:bold; margin-top:5px;'>{vid['title'][:50]}...</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button("Kích hoạt", key=vid['id']):
                    st.rerun()

    except Exception as e:
        st.error(f"⚠️ Hệ thống gặp sự cố: {e}")
else:
    st.image("https://unsplash.com", caption="HỆ THỐNG ĐANG CHỜ LỆNH TỪ ĐẠI CA")

st.divider()
st.caption("NEURAL PLAYER VERSION 4.0 - POWERED BY TEETA CORE AI")
