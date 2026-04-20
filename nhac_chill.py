import streamlit as st
import yt_dlp

# 1. Cấu hình hệ thống Neural
st.set_page_config(page_title="TEETA ULTIMATE HUB", page_icon="🚀", layout="wide")

# 2. CSS Dark Mode chuẩn 2026
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .news-card { 
        background-color: #111; padding: 15px; border-radius: 12px; 
        border: 1px solid #333; margin-bottom: 15px;
    }
    .stVideo { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    st.title("🚀 TEETA HUB")
    menu = st.radio("CHỌN KHÔNG GIAN:", ["📰 TIN TỨC 24H", "🎧 NGHE NHẠC", "🎬 XEM PHIM"])

# --- MỤC 1: TIN TỨC (ĐỌC TRỰC TIẾP TOÀN VĂN) ---
if menu == "📰 TIN TỨC 24H":
    st.header("📰 Tin Tức Toàn Cầu - Cập nhật 20/04/2026")
    
    # Danh sách tin tức với link thật để nhúng
    news_list = [
        {
            "title": "Quốc hội thảo luận Luật Đất đai (sửa đổi) đợt 2",
            "url": "https://baochinhphu.vn", # Link chuyên mục thời sự
            "img": "https://vietnamfinance.vn",
            "desc": "Thảo luận về phương án bồi thường và hỗ trợ tái định cư cho người dân."
        },
        {
            "title": "Giá vàng SJC hôm nay 20/4: Giữ ngưỡng 84 triệu đồng",
            "url": "https://vtv.vn",
            "img": "https://mediacdn.vn",
            "desc": "Thị trường vàng biến động mạnh, giá vàng nhẫn lập đỉnh mới."
        },
        {
            "title": "VinFast khởi công nhà máy xe điện tại Indonesia",
            "url": "https://vnexpress.net",
            "img": "https://vnecdn.net",
            "desc": "Bước tiến chiến lược của VinFast tại thị trường Đông Nam Á."
        }
    ]

    for i, item in enumerate(news_list):
        with st.container():
            col_img, col_txt = st.columns([1, 2])
            with col_img:
                st.image(item['img'], use_container_width=True)
            with col_txt:
                st.subheader(item['title'])
                st.write(item['desc'])
                
                # Nút kích hoạt trình đọc trực tiếp
                if st.button(f"📖 ĐỌC TOÀN VĂN BÀI {i+1}", key=f"btn_{i}"):
                    st.info("Đang kết nối luồng dữ liệu bài báo...")
                    # Kỹ thuật Iframe nhúng trực tiếp trang báo
                    st.components.v1.iframe(item['url'], height=800, scrolling=True)
            st.markdown("---")

# --- MỤC 2: NHẠC & MỤC 3: PHIM (TỐI ƯU TỐC ĐỘ) ---
elif menu == "🎧 NGHE NHẠC":
    query = st.text_input("Tìm nhạc:", placeholder="Nhập tên bài hát...")
    if query:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
            res = ydl.extract_info(query, download=False)['entries'][0]
            st.video(res['webpage_url'])

elif menu == "🎬 XEM PHIM":
    m_query = st.text_input("Tìm phim:", placeholder="Review phim...")
    if m_query:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch3'}) as ydl:
            movies = ydl.extract_info(m_query, download=False)['entries']
            for m in movies:
                st.video(m['webpage_url'])

st.caption("TEETA HUB v19.0 | TRÌNH ĐỌC BÁO XUYÊN THẤU | 20/04/2026")
