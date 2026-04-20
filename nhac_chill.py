import streamlit as st
import yt_dlp
import random

# 1. Cấu hình trang Đẳng cấp
st.set_page_config(page_title="Teeta AI Music Platform", page_icon="🎧", layout="wide")

# 2. CSS "Độ" giao diện YouTube Premium & Dark Mode
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: white; }
    .stTextInput input { border-radius: 40px !important; background-color: #121212 !important; color: white !important; border: 1px solid #333 !important; }
    .comment-box { background-color: #1a1a1a; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid #FF4B4B; }
    .ai-analysis { background: linear-gradient(90deg, #1e1e2f, #2a2a40); padding: 20px; border-radius: 15px; border: 1px solid #7f5af0; margin-top: 20px; }
    .suggest-card { cursor: pointer; transition: 0.3s; }
    .suggest-card:hover { background-color: #262626; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER: THANH TÌM KIẾM CHUẨN ---
st.markdown("<h2 style='text-align: center; color: #FF0000;'>🔴 TEETA MUSIC AI</h2>", unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Tìm kiếm bài hát, nghệ sĩ hoặc cảm xúc âm nhạc...", label_visibility="collapsed")

if query:
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch10'}) as ydl:
            results = ydl.extract_info(query, download=False)['entries']
        
        main_v = results[0]
        
        # --- CHIA LAYOUT 2 CỘT ---
        col_main, col_side = st.columns([2.5, 1])

        with col_main:
            # A. TRÌNH PHÁT NHẠC
            st.video(main_v['webpage_url'])
            st.title(main_v['title'])
            
            c1, c2, c3 = st.columns([2, 1, 1])
            with c1: st.write(f"👤 **{main_v['uploader']}** | 👁️ {main_v.get('view_count', 0):,} views")
            with c2: st.button("👍 Thích")
            with c3: st.button("🔔 Đăng ký", type="primary")

            # B. PHÂN TÍCH AI (AI ANALYSIS)
            st.markdown("<div class='ai-analysis'>", unsafe_allow_html=True)
            st.subheader("🤖 AI Music Insight")
            # Giả lập phân tích AI dựa trên tiêu đề bài hát
            ai_prompts = [
                f"Sáng tác hình ảnh dựa trên bài: '{main_v['title']}'",
                "Phong cách: Cinematic, Dreamy, 8k resolution",
                "Mood: Sâu lắng, hoài niệm, ánh sáng hoàng hôn"
            ]
            st.write(f"**Phân tích cảm xúc:** Bài hát mang âm hưởng {random.choice(['Sôi động', 'Trầm buồn', 'Chill Lofi'])}. Phù hợp để làm việc hoặc thư giãn.")
            st.write("**AI Prompts đề xuất cho bài này:**")
            for p in ai_prompts:
                st.code(p, language='text')
            st.markdown("</div>", unsafe_allow_html=True)

            # C. BÌNH LUẬN & GHI PROMPT
            st.markdown("---")
            st.subheader("💬 Bình luận & Ghi Prompt")
            
            # Ô nhập bình luận/prompt
            user_input = st.text_area("Ghi suy nghĩ hoặc Prompt của bạn về bài hát này:", placeholder="Ví dụ: /imagine một không gian vũ trụ theo điệu nhạc này...")
            if st.button("Gửi nội dung"):
                st.toast("Đã ghi nhận nội dung của đại ca!")
            
            # Danh sách bình luận giả lập
            comments =} chưa bao giờ làm tôi thất vọng."}
            ]
            for c in comments:
                st.markdown(f"""<div class='comment-box'><strong>{c['user']}</strong>: {c}</div>""", unsafe_allow_html=True)

        with col_side:
            # D. DANH SÁCH BÀI HÁT GỢI Ý (SIDEBAR)
            st.write("### ⏭️ Tiếp theo")
            for vid in results[1:7]:
                with st.container():
                    sc1, sc2 = st.columns([1, 1.5])
                    with sc1:
                        st.image(vid['thumbnail'], use_container_width=True)
                    with sc2:
                        st.markdown(f"<p style='font-size:14px; font-weight:bold;'>{vid['title'][:45]}...</p>", unsafe_allow_html=True)
                        st.caption(vid['uploader'])
                    if st.button("Nghe", key=vid['id']):
                        st.session_state['yt_search'] = vid['title']
                        st.rerun()
                    st.markdown("<br>", unsafe_allow_html=True)

    except Exception as e:
        st.error("Server nhạc đang bận, đại ca nhấn tìm lại nhé!")
else:
    st.image("https://unsplash.com")
    st.info("🔥 Chào mừng đại ca đến với hệ thống nhạc AI. Hãy nhập tên bài hát để bắt đầu trải nghiệm!")

st.divider()
st.caption("© 2026 Teeta AI Studio - The Future of Music Experience")
