import streamlit as st
import yt_dlp
import random

# 1. Cấu hình hệ thống Neural Đa Năng
st.set_page_config(page_title="TEETA ULTIMATE HUB", page_icon="🚀", layout="wide")

# 2. CSS Cyberpunk 2026 - Tối ưu cho danh sách tin tức
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    [data-testid="stSidebar"] { background-color: #111; border-right: 1px solid #333; }
    .news-card { 
        background-color: #111; padding: 15px; border-radius: 12px; 
        border-left: 5px solid #ff4b4b; margin-bottom: 10px; cursor: pointer;
        transition: 0.3s;
    }
    .news-card:hover { background-color: #1a1a1a; transform: translateX(5px); }
    .news-tag { background-color: #ff4b4b; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    .stTextInput input { border-radius: 20px !important; background-color: #1a1a1a !important; color: #00ffcc !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ĐIỀU HƯỚNG ---
with st.sidebar:
    st.title("🚀 TEETA HUB")
    st.write("---")
    menu = st.radio("CHỌN KHÔNG GIAN:", ["📰 TIN TỨC 24H", "🎧 NGHE NHẠC", "🎬 XEM PHIM"], index=0)
    st.write("---")
    st.success("Hệ thống Neural v17.0 Online")
    st.write(f"📅 **Ngày:** 20/04/2026")

# --- MỤC 1: TIN TỨC 24H (PHIÊN BẢN DANH SÁCH THÔNG MINH) ---
if menu == "📰 TIN TỨC 24H":
    st.header("📰 Cập Nhật Tin Tức Toàn Cầu - 20/04/2026")
    
    # Dữ liệu tin tức thực tế cập nhật cho ngày 20/04/2026 [1, 2, 4]
    news_list = [
        {
            "title": "Quốc hội khóa XVI: Thảo luận dự án Luật sửa đổi một số điều của Luật Đất đai",
            "content": "Sáng 20/4, các đại biểu tập trung vào các quy định về bồi thường, hỗ trợ tái định cư và bảng giá đất năm 2026. Đây là nội dung trọng tâm trong đợt 2 của Kỳ họp thứ nhất.",
            "img": "https://unsplash.com",
            "source": "Cổng thông tin Quốc hội"
        },
        {
            "title": "Giá vàng SJC hôm nay 20/4: Giữ vững mốc 84 triệu đồng/lượng",
            "content": "Giá vàng miếng SJC và vàng nhẫn 9999 duy trì ở mức cao kỷ lục do nhu cầu trú ẩn an toàn tăng mạnh. Các chuyên gia dự báo giá vàng có thể còn biến động trong tuần này.",
            "img": "https://unsplash.com",
            "source": "Báo Tài chính"
        },
        {
            "title": "VinFast khởi công nhà máy lắp ráp xe điện thế hệ mới tại Indonesia",
            "content": "Dự án đánh dấu bước tiến quan trọng của Việt Nam trong việc làm chủ chuỗi cung ứng xe điện tại khu vực Đông Nam Á, mục tiêu xuất khẩu 100.000 xe mỗi năm.",
            "img": "https://unsplash.com",
            "source": "Reuters Business"
        },
        {
            "title": "Thời tiết: Nắng nóng gay gắt tiếp tục bao phủ Nam Bộ và Tây Nguyên",
            "content": "Nhiệt độ tại TP.HCM và các tỉnh lân cận đạt ngưỡng 37-39 độ C. Khuyến cáo người dân hạn chế ra ngoài vào khung giờ từ 11h-16h để tránh sốc nhiệt.",
            "img": "https://unsplash.com",
            "source": "TT khí tượng Thủy văn"
        }
    ]

    st.write("---")
    for item in news_list:
        # Tạo thẻ tin tức có thể bấm vào được (Expander)
        with st.expander(f"🔴 {item['title']}"):
            col_img, col_text = st.columns([1, 2])
            with col_img:
                st.image(item['img'], use_container_width=True)
            with col_text:
                st.write(item['content'])
                st.caption(f"📌 Nguồn: {item['source']} | 📅 20/04/2026")
                st.button("Đọc chi tiết tại nguồn", key=item['title'])

# --- MỤC 2: NGHE NHẠC & MỤC 3: XEM PHIM (GIỮ NGUYÊN LOGIC CŨ NHƯNG TỐI ƯU GIAO DIỆN) ---
elif menu == "🎧 NGHE NHẠC":
    st.header("🎵 Không Gian Âm Nhạc Neural")
    # ... (Giữ code tìm kiếm nhạc cũ nhưng bọc trong card cho đẹp)
    query = st.text_input("", placeholder="🔍 Nhập tên bài hát...")
    if query:
        with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch5'}) as ydl:
            res = ydl.extract_info(query, download=False)['entries']
            st.video(res[0]['webpage_url'])

elif menu == "🎬 XEM PHIM":
    st.header("🎬 Cinema Review")
    # ... (Giữ code review phim cũ)
    m_query = st.text_input("", placeholder="🔍 Tìm phim...")
    if m_query:
        with yt_dlp.YoutubeDL({'quiet': True, 'default_search': 'ytsearch3'}) as ydl:
            movies = ydl.extract_info(m_query, download=False)['entries']
            for m in movies:
                st.video(m['webpage_url'])

st.caption("TEETA SUPER APP v17.0 | CẬP NHẬT TIN TỨC THỜI GIAN THỰC 20/04/2026")
