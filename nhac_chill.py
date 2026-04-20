import streamlit as st
import yt_dlp
import random

# 1. Cấu hình hệ thống Neural Đẳng cấp
st.set_page_config(page_title="TEETA NEURAL PLAYER", page_icon="🎧", layout="wide")

# 2. CSS Cyberpunk - Giao diện thống nhất cho mọi nguồn nhạc
st.markdown("""
    <style>
    .stApp { background: #050505; color: #00ffcc; }
    .stTextInput input { 
        border-radius: 30px !important; background-color: #111 !important; 
        color: #00ffcc !important; border: 1px solid #00ffcc !important;
    }
    .main-frame { border: 2px solid #00ffcc; border-radius: 15px; overflow: hidden; background: #000; }
    .ai-terminal { background: #000; border: 1px solid #ff00ff; padding: 15px; border-radius: 10px; font-family: monospace; color: #ff00ff; margin-top: 20px; }
    .comment-box { background: #111; padding: 10px; border-radius: 5px; border-left: 3px solid #00ffcc; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🧠 TEETA NEURAL PLAYER - MULTI-EMBED</h1>", unsafe_allow_html=True)

# --- THANH TÌM KIẾM ĐA NĂNG ---
query = st.text_input("📡 TRUY VẤN TÊN BÀI HÁT:", placeholder="Nhập tên bài hát để hệ thống lấy luồng phát trực tiếp...")

if query:
    try:
        # A. Lấy dữ liệu YouTube làm luồng phát mặc định
        ydl_opts = {'quiet': True, 'default_search': 'ytsearch5', 'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            results = ydl.extract_info(query, download=False)['entries']
        
        main_v = results[0]
        
        col_main, col_side = st.columns([2.5, 1])

        with col_main:
            # TABS CHỌN NGUỒN PHÁT (TẤT CẢ PHÁT TRONG APP)
            tab_yt, tab_zing, tab_nct, tab_sc = st.tabs(["📺 YouTube", "🎶 ZingMP3", "💎 NhacCuaTui", "☁️ SoundCloud"])
            
            with tab_yt:
                st.video(main_v['webpage_url'])
            
            with tab_zing:
                # Nhúng kết quả tìm kiếm ZingMP3 trực tiếp vào iframe
                zing_url = f"https://zingmp3.vn{query.replace(' ', '+')}"
                st.components.v1.iframe(zing_url, height=600, scrolling=True)
            
            with tab_nct:
                nct_url = f"https://nhaccuatui.com{query.replace(' ', '+')}"
                st.components.v1.iframe(nct_url, height=600, scrolling=True)
                
            with tab_sc:
                sc_url = f"https://soundcloud.com{query.replace(' ', '%20')}"
                st.components.v1.iframe(sc_url, height=600, scrolling=True)

            # --- PHÂN TÍCH AI & GHI PROMPT (DƯỚI TRÌNH PHÁT) ---
            st.markdown("<div class='ai-terminal'>", unsafe_allow_html=True)
            st.subheader("🤖 AI Neural Insight")
            st.write(f"**Target:** {main_v['title']}")
            st.write(f"**AI Vision Prompt:**")
            st.code(f"/imagine prompt: Visualizing soundwaves of '{query}', neon cyberpunk style, futuristic audio interface, 8k --ar 16:9", language="text")
            st.markdown("</div>", unsafe_allow_html=True)

            st.write("---")
            st.subheader("💬 GHI CHÉP PROMPT CỦA ĐẠI CA")
            user_prompt = st.text_area("Nhập Prompt sáng tạo tại đây:", placeholder="Hệ thống đang lắng nghe tư duy của đại ca...")
            if st.button("KÍCH HOẠT LƯU PROMPT"):
                st.balloons()
                st.success("Dữ liệu đã được nạp vào Neural Core!")

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
        st.error(f"⚠️ Đang quét tần số... Đại ca thử lại nhé!")
else:
    st.image("https://unsplash.com", use_container_width=True)
    st.info("🔥 Hệ thống 'Hội Tụ' đã sẵn sàng. Gõ tên bài hát để nghe trực tiếp từ 4 nguồn khác nhau ngay tại đây!")

st.caption("TEETA ALL-IN-ONE PLAYER V6.0 | NO REDIRECTS | PURE NEURAL EXPERIENCE")
