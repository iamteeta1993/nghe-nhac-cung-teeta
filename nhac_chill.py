import streamlit as st
import yt_dlp

# 1. Cấu hình giao diện đẳng cấp
st.set_page_config(page_title="Teeta Global Music", page_icon="🎧", layout="wide")

# CSS "Độ" thanh search dính liền khối chuẩn YouTube (Fix lỗi vỡ khung)
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: white; }
    div[data-testid="stHorizontalBlock"] .stTextInput input {
        border-radius: 40px 0 0 40px !important;
        background-color: #121212 !important;
        color: white !important;
        border: 1px solid #333 !important;
        height: 40px !important;
    }
    div[data-testid="stHorizontalBlock"] button {
        border-radius: 0 40px 40px 0 !important;
        background-color: #333 !important;
        border: 1px solid #333 !important;
        height: 40px !important;
        margin-left: -32px !important;
        width: 60px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h2 style='color: red;'>🔴 TEETA YOUTUBE AI</h2>", unsafe_allow_html=True)

# --- THANH TÌM KIẾM ---
c1, c2, c3 = st.columns([4, 0.5, 1])
with c1:
    query = st.text_input("", placeholder="🔍 Nhập tên bài hát (Ví dụ: Chúng ta của hiện tại)...", label_visibility="collapsed")
with c2:
    search_btn = st.button("🔍")

# --- XỬ LÝ PHÁT NHẠC ---
if query:
    with st.spinner('🚀 Đang kết nối server nhạc toàn cầu...'):
        try:
            # Sử dụng yt-dlp để lấy link video thật (Fix lỗi IP)
            ydl_opts = {'quiet': True, 'default_search': 'ytsearch5', 'format': 'best'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                results = info['entries']
            
            main_v = results[0]
            
            col_main, col_side = st.columns([2.8, 1.2])

            with col_main:
                # Dùng trình phát chính chủ của Streamlit - Không bao giờ lỗi IP
                st.video(main_v['webpage_url'])
                st.subheader(main_v['title'])
                st.write(f"👤 {main_v['uploader']} | 👁️ {main_v.get('view_count', 0):,} lượt xem")
                
                # PHÂN TÍCH AI & PROMPT
                with st.expander("🤖 AI NEURAL INSIGHT"):
                    st.code(f"/imagine prompt: Cinematic visual for {query}, 8k, futuristic neon style", language="text")
                    st.text_area("Ghi chú Prompt của đại ca:", placeholder="Nhập tại đây...")

            with col_side:
                st.write("⏭️ **Danh sách liên quan**")
                for vid in results[1:]:
                    with st.container():
                        sc1, sc2 = st.columns([1, 1.5])
                        with sc1:
                            st.image(vid['thumbnail'], use_container_width=True)
                        with sc2:
                            st.markdown(f"<p style='font-size:12px; font-weight:bold;'>{vid['title'][:40]}...</p>", unsafe_allow_html=True)
                            if st.button("Xem", key=vid['id']):
                                st.rerun()

        except Exception as e:
            st.error("⚠️ Không tìm thấy bài hát. Đại ca thử gõ lại tên bài nhé!")
else:
    st.info("💡 Hãy nhập tên bài hát vào thanh search phía trên!")

st.caption("Teeta YouTube Premium v13.0 - Fix IP Error")
