import streamlit as st
import yt_dlp
import random

# 1. Cấu hình trang
st.set_page_config(page_title="Teeta AI Music", page_icon="🎧", layout="wide")

# 2. CSS Dark Mode chuẩn YouTube
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: white; }
    .stTextInput input { border-radius: 40px !important; background-color: #121212 !important; color: white !important; border: 1px solid #333 !important; padding: 10px 20px !important; }
    .comment-box { background-color: #1a1a1a; padding: 12px; border-radius: 8px; margin-bottom: 8px; border-left: 3px solid #FF0000; }
    .ai-box { background: linear-gradient(135deg, #1e1e2f 0%, #111 100%); padding: 20px; border-radius: 15px; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

# --- THANH TÌM KIẾM ---
st.markdown("<h2 style='text-align: center; color: red;'>🔴 TEETA MUSIC AI</h2>", unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Tìm kiếm bài hát hoặc nghệ sĩ...", label_visibility="collapsed")

if query:
    try:
        # Tìm kiếm nhạc
        ydl_opts = {'quiet': True, 'default_search': 'ytsearch10', 'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            results = info['entries']
        
        main_v = results[0] # Bài đầu tiên
        
        # --- CHIA 2 CỘT: TRÁI (VIDEO/AI/BÌNH LUẬN) - PHẢI (DANH SÁCH) ---
        col_left, col_right = st.columns([2.5, 1])

        with col_left:
            # PHÁT NHẠC
            st.video(main_v['webpage_url'])
            st.title(main_v['title'])
            st.write(f"👤 **{main_v['uploader']}** | 👁️ {main_v.get('view_count', 0):,} lượt xem")
            
            # PHÂN TÍCH AI
            with st.container():
                st.markdown("<div class='ai-box'>", unsafe_allow_html=True)
                st.subheader("🤖 Phân tích AI & Prompts")
                st.write(f"**Mood:** {random.choice(['Sâu lắng', 'Mạnh mẽ', 'Chill Lofi'])}")
                st.write("**AI Prompt gợi ý cho hình ảnh:**")
                st.code(f"/imagine prompt: A cinematic visual of {query}, neon lights, 8k, detailed", language='text')
                st.markdown("</div>", unsafe_allow_html=True)

            # BÌNH LUẬN & GHI PROMPT
            st.markdown("---")
            st.subheader("💬 Bình luận & Cộng đồng")
            new_comment = st.text_area("Ghi bình luận hoặc Prompt của bạn:", height=100)
            if st.button("Gửi lên hệ thống"):
                st.toast("Đã lưu nội dung của đại ca!")
            
            # Mockup bình luận
            st.markdown("<div class='comment-box'><strong>AI_Assistant</strong>: Bài này có vòng hợp âm rất hay cho việc tập trung code.</div>", unsafe_allow_html=True)
            st.markdown("<div class='comment-box'><strong>Fan_Cung</strong>: Đỉnh cao Teeta ơi!</div>", unsafe_allow_html=True)

        with col_right:
            st.subheader("⏭️ Tiếp theo")
            for vid in results[1:7]:
                with st.container():
                    c1, c2 = st.columns([1, 1.5])
                    with c1:
                        st.image(vid['thumbnail'], use_container_width=True)
                    with c2:
                        st.markdown(f"**{vid['title'][:40]}...**")
                        if st.button("Nghe", key=vid['id']):
                            st.session_state['last_query'] = vid['title']
                            st.rerun()
                    st.write("")

    except Exception as e:
        st.error("Lỗi kết nối YouTube. Đại ca thử gõ lại tên bài hát nhé!")
else:
    st.info("🔥 Nhập tên bài hát để trải nghiệm hệ thống AI Music đẳng cấp thế giới!")

st.caption("© 2026 Teeta AI Studio - YouTube Clone Project")
