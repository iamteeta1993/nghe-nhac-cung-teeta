import streamlit as st
import yt_dlp
import random

# Cấu hình trang rộng để giả lập giao diện YouTube
st.set_page_config(page_title="Teeta YouTube", page_icon="🎧", layout="wide")

# CSS tạo giao diện Dark Mode chuẩn YouTube Premium
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: white; }
    .stTextInput input { 
        border-radius: 40px !important; background-color: #121212 !important; 
        color: white !important; border: 1px solid #333 !important; 
        padding: 10px 20px !important;
    }
    .video-card { background-color: #121212; border-radius: 10px; padding: 10px; transition: 0.3s; }
    .video-card:hover { background-color: #262626; }
    .ai-box { background: #1a1a1a; padding: 15px; border-radius: 12px; border-left: 4px solid #FF0000; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER: THANH TÌM KIẾM ---
st.markdown("<h2 style='color: red; font-family: sans-serif;'>🔴 TEETA MUSIC</h2>", unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Tìm kiếm bài hát hoặc nghệ sĩ...", label_visibility="collapsed")

if query:
    try:
        # Tìm kiếm 10 kết quả
        ydl_opts = {'quiet': True, 'default_search': 'ytsearch10', 'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            results = ydl.extract_info(query, download=False)['entries']
        
        main_v = results[0]  # Video đầu tiên làm video chính
        
        # --- CHIA LAYOUT: TRÁI (3/4) - PHẢI (1/4) ---
        col_left, col_right = st.columns([2.8, 1.2])

        with col_left:
            # 1. TRÌNH PHÁT CHÍNH
            st.video(main_v['webpage_url'])
            st.title(main_v['title'])
            st.write(f"👤 **{main_v['uploader']}** | 👁️ {main_v.get('view_count', 0):,} lượt xem")
            
            # 2. PHÂN TÍCH AI & BÌNH LUẬN (DƯỚI VIDEO)
            with st.expander("🤖 PHÂN TÍCH AI & PROMPTS", expanded=True):
                st.markdown("<div class='ai-box'>", unsafe_allow_html=True)
                st.write(f"**Cảm xúc bài hát:** {random.choice(['Sôi động', 'Chill', 'Sâu lắng'])}")
                st.write("**AI Image Prompt:**")
                st.code(f"/imagine prompt: A cinematic visual for {query}, 8k, futuristic style", language='text')
                st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("---")
            st.subheader("💬 Bình luận")
            st.text_area("Viết bình luận...", placeholder="Chia sẻ cảm nghĩ của đại ca...", label_visibility="collapsed")
            st.button("Gửi bình luận")

        with col_right:
            # 3. DANH SÁCH GỢI Ý BÊN PHẢI
            st.subheader("⏭️ Tiếp theo")
            for vid in results[1:8]:
                with st.container():
                    c1, c2 = st.columns([1, 1.2])
                    with c1:
                        st.image(vid['thumbnail'], use_container_width=True)
                    with c2:
                        st.markdown(f"<p style='font-size:14px; font-weight:bold;'>{vid['title'][:45]}...</p>", unsafe_allow_html=True)
                        st.caption(vid['uploader'])
                        if st.button("Nghe", key=vid['id']):
                            # Kỹ thuật chuyển bài nhanh
                            st.session_state['last_query'] = vid['title']
                            st.rerun()
                st.write("")

    except Exception as e:
        st.error("Kết nối YouTube đang bận, đại ca gõ lại tên bài nhé!")
else:
    st.image("https://unsplash.com", caption="Chào mừng đại ca quay trở lại với giao diện truyền thống!")

st.caption("TEETA YOUTUBE CLASSIC V8.0 | 2026")
