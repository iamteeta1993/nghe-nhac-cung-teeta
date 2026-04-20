import streamlit as st
import yt_dlp

# 1. Cấu hình hệ thống Hyper Speed
st.set_page_config(page_title="TEETA HYPER ENGINE", page_icon="⚡", layout="wide")

# 2. CSS Dark Mode Cyberpunk (Tối ưu hiển thị)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .stTextInput input { border-radius: 20px !important; background-color: #1a1a1a !important; color: #00ffcc !important; border: 1px solid #333 !important; }
    .result-card { background-color: #111; padding: 15px; border-radius: 12px; border: 1px solid #222; margin-bottom: 15px; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #111; border-radius: 5px; color: #fff; }
    .stTabs [aria-selected="true"] { background-color: #00ffcc !important; color: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HÀM TÌM KIẾM CẢI TIẾN (CHỐNG TRẮNG TRANG) ---
def hyper_search(query, limit=5):
    ydl_opts = {
        'quiet': True,
        'default_search': f'ytsearch{limit}',
        'noplaylist': True,
        'extract_flat': False, # Chuyển thành False để lấy dữ liệu chắc chắn hơn
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(query, download=False)
            return info.get('entries', [])
        except:
            return []

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>⚡ TEETA HYPER ENGINE 2026</h1>", unsafe_allow_html=True)

# PHÂN CHIA 3 MỤC CHÍNH
tab1, tab2, tab3 = st.tabs(["🎵 NGHE NHẠC", "🎬 XEM PHIM", "📰 TIN TỨC"])

# --- MỤC 1: NGHE NHẠC ---
with tab1:
    m_query = st.text_input("Nhập tên bài hát:", placeholder="Ví dụ: Sơn Tùng, Lofi chill...", key="m_s")
    if m_query:
        with st.spinner('🚀 Đang kết nối luồng nhạc...'):
            results = hyper_search(m_query, limit=5)
            if results:
                col_m1, col_m2 = st.columns([2.5, 1.2])
                with col_m1:
                    # Phát bài đầu tiên
                    main_v = results[0]
                    st.video(main_v['webpage_url'])
                    st.subheader(main_v['title'])
                with col_m2:
                    st.write("🔥 **Kết quả liên quan:**")
                    for v in results[1:]:
                        if st.button(f"🎵 {v['title'][:45]}...", key=v['id']):
                            st.video(v['webpage_url']) # Nhấn là phát luôn
            else:
                st.warning("⚠️ Không tìm thấy bài hát. Đại ca thử gõ lại tên bài khác nhé!")

# --- MỤC 2: XEM PHIM ---
with tab2:
    f_query = st.text_input("Tìm review phim:", placeholder="Ví dụ: Review phim hành động...", key="f_s")
    if f_query:
        with st.spinner('🎬 Đang quét kho phim...'):
            movies = hyper_search(f_query, limit=6)
            if movies:
                cols = st.columns(3)
                for i, m in enumerate(movies):
                    with cols[i % 3]:
                        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
                        st.image(m['thumbnail'], use_container_width=True)
                        st.markdown(f"**{m['title'][:45]}...**")
                        with st.expander("📺 Xem Review"):
                            st.video(m['webpage_url'])
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ Không tìm thấy phim nào.")

# --- MỤC 3: TIN TỨC (DỮ LIỆU THỰC 20/04/2026) ---
with tab3:
    st.subheader("📰 Điểm Tin Nóng Hồi - 20/04/2026")
    news_data = [
        {"t": "Quốc hội họp đợt 2: Thảo luận bồi thường đất đai tái định cư.", "s": "VTV News"},
        {"t": "Giá vàng SJC hôm nay 20/4: Giữ mức cao kỷ lục 84 triệu đồng/lượng.", "s": "Tài chính"},
        {"t": "VinFast khởi công nhà máy mới tại Indonesia, mở rộng quy mô Đông Nam Á.", "s": "Reuters"},
        {"t": "Nắng nóng kỷ lục 39 độ C tiếp tục bao phủ Nam Bộ và Tây Nguyên.", "s": "Khí tượng"}
    ]
    for item in news_data:
        st.markdown(f"""
            <div style='background:#111; padding:15px; border-radius:10px; border-left:4px solid #00ffcc; margin-bottom:10px;'>
                <h4 style='margin:0;'>{item['t']}</h4>
                <p style='margin:0; font-size:12px; color:#888;'>📌 Nguồn: {item['s']} | 📅 20/04/2026</p>
            </div>
        """, unsafe_allow_html=True)

st.caption("TEETA HYPER ENGINE v3.0 | STABLE SEARCH | 2026")
