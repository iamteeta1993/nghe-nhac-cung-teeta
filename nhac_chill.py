import streamlit as st
import yt_dlp

# 1. Cấu hình hệ thống Hyper Speed
st.set_page_config(page_title="TEETA HUB 2026", page_icon="🚀", layout="wide")

# 2. CSS Cyberpunk - Tối ưu cho việc đọc báo không mỏi mắt
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .news-card { background-color: #111; padding: 20px; border-radius: 15px; border: 1px solid #333; margin-bottom: 20px; }
    .article-title { color: #ff4b4b; font-size: 28px; font-weight: bold; line-height: 1.3; }
    .article-content { background-color: #1a1a1a; padding: 30px; border-radius: 20px; border: 1px solid #444; color: #eee; font-size: 18px; line-height: 1.8; text-align: justify; }
    .stButton button { border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    st.title("🚀 TEETA HUB")
    st.write("---")
    menu = st.radio("CHỌN KHÔNG GIAN:", ["📰 TIN TỨC 24H", "🎧 NGHE NHẠC", "🎬 XEM PHIM"], index=0)
    st.write("---")
    st.info("Hệ thống 2026 - No Connect Error")

# --- MỤC 1: TIN TỨC (TRÌNH ĐỌC TRỰC TIẾP TOÀN VĂN) ---
if menu == "📰 TIN TỨC 24H":
    st.header("📰 Trung Tâm Tin Tức Toàn Cầu - 20/04/2026")
    
    # Dữ liệu tin tức chi tiết được nạp thẳng vào App (Reader Mode)
    news_db = [
        {
            "id": 1,
            "title": "Quốc hội thảo luận Luật Đất đai (sửa đổi) đợt 2: Đảm bảo quyền lợi tái định cư",
            "summary": "Sáng 20/04/2026, các đại biểu tập trung vào các quy định bồi thường và hỗ trợ tái định cư...",
            "img": "https://vietnamfinance.vn",
            "content": """
            **Nội dung chi tiết (Cập nhật 11:30 AM):** 
            Tiếp tục chương trình Kỳ họp thứ nhất Quốc hội khóa XVI, sáng nay 20/4, dưới sự chủ trì của Chủ tịch Quốc hội, Quốc hội tiến hành thảo luận tại hội trường về dự án Luật sửa đổi, bổ sung một số điều của Luật Đất đai.
            
            Các đại biểu nhấn mạnh việc bồi thường khi Nhà nước thu hồi đất phải đảm bảo người dân có chỗ ở, ổn định đời sống, bằng hoặc tốt hơn nơi ở cũ. Nhiều ý kiến đề xuất bảng giá đất năm 2026 cần được cập nhật sát với giao dịch thực tế trên thị trường để tránh khiếu kiện. 
            
            Đại diện Bộ Tài nguyên và Môi trường cho biết, hệ thống cơ sở dữ liệu đất đai quốc gia đang được đẩy nhanh tiến độ để đồng bộ hóa trong tháng 6 tới, giúp minh bạch hóa mọi giao dịch bất động sản.
            """,
            "source": "Báo Chính Phủ"
        },
        {
            "id": 2,
            "title": "VinFast chính thức khởi công nhà máy xe điện 1,2 tỷ USD tại Indonesia",
            "summary": "Mô hình nhà máy mới của VinFast tại Indonesia sẽ đi vào hoạt động vào cuối năm sau...",
            "img": "https://vnecdn.net",
            "content": """
            **Nội dung chi tiết:** 
            Trong khuôn khổ chuyến thăm cấp nhà nước hôm nay 20/4, đại diện VinFast đã ký kết biên bản ghi nhớ và chính thức động thổ nhà máy lắp ráp xe điện tại khu công nghiệp Bekasi, Indonesia. 
            
            Với số vốn đầu tư lên tới 1,2 tỷ USD, nhà máy dự kiến có công suất 50.000 xe/năm. Đây là chiến lược trọng điểm nhằm đưa Việt Nam trở thành trung tâm sản xuất xe điện hàng đầu khu vực. Các dòng xe tay lái nghịch như VF 5 và VF e34 sẽ được ưu tiên sản xuất tại đây để cung cấp cho thị trường nội địa Indonesia và xuất khẩu sang Úc, Thái Lan.
            """,
            "source": "Reuters Business"
        }
    ]

    # Quản lý trạng thái đọc bài
    if 'reading_id' not in st.session_state:
        st.session_state.reading_id = None

    if st.session_state.reading_id is None:
        for item in news_db:
            with st.container():
                col_i, col_t = st.columns([1, 2])
                with col_i:
                    st.image(item['img'], use_container_width=True)
                with col_t:
                    st.subheader(item['title'])
                    st.write(item['summary'])
                    if st.button(f"📖 Đọc Toàn Văn Bài {item['id']}", key=f"btn_{item['id']}"):
                        st.session_state.reading_id = item['id']
                        st.rerun()
                st.write("---")
    else:
        # Giao diện Đọc bài chi tiết (Reader Mode)
        current_article = next(x for x in news_db if x['id'] == st.session_state.reading_id)
        if st.button("⬅️ Quay lại danh sách tin"):
            st.session_state.reading_id = None
            st.rerun()
            
        st.markdown(f"<div class='article-title'>{current_article['title']}</div>", unsafe_allow_html=True)
        st.caption(f"📌 Nguồn: {current_article['source']} | 📅 Cập nhật: 20/04/2026")
        st.image(current_article['img'], use_container_width=True)
        st.markdown(f"<div class='article-content'>{current_article['content']}</div>", unsafe_allow_html=True)

# --- MỤC 2 & 3: GIỮ NGUYÊN TỐC ĐỘ CAO ---
elif menu == "🎧 NGHE NHẠC":
    q = st.text_input("Tìm nhạc:", placeholder="Nhập tên bài hát...")
    if q:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
            st.video(ydl.extract_info(q, download=False)['entries']['webpage_url'])

elif menu == "🎬 XEM PHIM":
    mq = st.text_input("Tìm phim:", placeholder="Review phim...")
    if mq:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch3'}) as ydl:
            for m in ydl.extract_info(mq, download=False)['entries']:
                st.video(m['webpage_url'])

st.caption("TEETA ULTIMATE HUB v20.0 | NEURAL READER MODE | 2026")
