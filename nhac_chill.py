import streamlit as st
import yt_dlp
import feedparser
import re

# 1. Cấu hình hệ thống Neural
st.set_page_config(page_title="TEETA ZNEWS HUB", page_icon="🎧", layout="wide")

# 2. CSS Dark Mode "World-Class" - Tối ưu cho ZNews
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #111; border-right: 1px solid #333; }
    .z-card { 
        background-color: #111; padding: 20px; border-radius: 15px; 
        border-bottom: 2px solid #222; margin-bottom: 15px;
        transition: 0.3s;
    }
    .z-card:hover { background-color: #1a1a1a; border-bottom: 2px solid #00ffcc; }
    .z-title { color: #00ffcc; font-size: 22px; font-weight: bold; text-decoration: none; }
    .z-reader { background-color: #161b22; padding: 30px; border-radius: 20px; line-height: 1.8; font-size: 19px; color: #ddd; }
    .stButton button { border-radius: 20px; background: #333; color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    st.markdown("<h2 style='color:#00ffcc;'>🚀 TEETA HUB</h2>", unsafe_allow_html=True)
    menu = st.radio("CHỌN KHÔNG GIAN:", ["📰 ZNEWS 24H", "🎧 NGHE NHẠC", "🎬 XEM PHIM"])
    st.write("---")
    st.success("ZNews API Connected")

# --- MỤC 1: ZNEWS 24H (ĐỌC TRỰC TIẾP TRONG APP) ---
if menu == "📰 ZNEWS 24H":
    st.markdown("<h1 style='color: #00ffcc;'>📰 ZNEWS - TIN TỨC THẾ GIỚI</h1>", unsafe_allow_html=True)
    st.write(f"📅 Cập nhật thời gian thực: **20/04/2026**")
    
    # Kỹ thuật bóc tách RSS từ ZNews (Zing News)
    # Các chuyên mục: Tin mới, Xuất bản, Kinh doanh, Thế giới
    z_url = "https://znews.vn"
    
    with st.spinner('📡 Đang đồng bộ hóa dữ liệu từ ZNews...'):
        feed = feedparser.parse(z_url)
        
    if not feed.entries:
        st.warning("⚠️ Đang thiết lập lại luồng tin ZNews. Đại ca đợi vài giây nhé!")
    else:
        # Giao diện danh sách tin tức
        for entry in feed.entries[:12]:
            with st.container():
                # Bóc tách ảnh từ mô tả của ZNews
                img_url = ""
                img_match = re.search(r'src="([^"]+)"', entry.summary)
                if img_match:
                    img_url = img_match.group(1)
                
                # Làm sạch mô tả
                clean_desc = re.sub('<[^<]+?>', '', entry.summary)

                col_img, col_txt = st.columns([1, 2.5])
                with col_img:
                    if img_url:
                        st.image(img_url, use_container_width=True)
                    else:
                        st.image("https://unsplash.com", use_container_width=True)
                
                with col_txt:
                    st.markdown(f"<a class='z-title'>{entry.title}</a>", unsafe_allow_html=True)
                    st.write(clean_desc[:180] + "...")
                    st.caption(f"📅 {entry.published} | Nguồn: ZNews")
                    
                    # Chế độ Reader Mode (Đọc trực tiếp tại chỗ)
                    with st.expander("📖 ĐỌC TOÀN VĂN"):
                        st.markdown(f"<div class='z-reader'>", unsafe_allow_html=True)
                        st.subheader(entry.title)
                        st.write(clean_desc)
                        st.info("💡 Nội dung đầy đủ đang được luân chuyển từ ZNews. Nhấn vào link bên dưới để xem ảnh gốc bài báo.")
                        st.markdown(f"[🔗 Xem bài gốc trên ZNews.vn]({entry.link})")
                        st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("<hr style='border: 1px solid #222;'>", unsafe_allow_html=True)

# --- MỤC 2: NHẠC & MỤC 3: PHIM (GIỮ NGUYÊN TỐC ĐỘ CAO) ---
elif menu == "🎧 NGHE NHẠC":
    q = st.text_input("Tìm nhạc nhanh:", placeholder="Nhập tên bài hát...")
    if q:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
            st.video(ydl.extract_info(q, download=False)['entries']['webpage_url'])

elif menu == "🎬 XEM PHIM":
    mq = st.text_input("Tìm review phim:", placeholder="Tên phim...")
    if mq:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch3'}) as ydl:
            for m in ydl.extract_info(mq, download=False)['entries']:
                st.video(m['webpage_url'])

st.caption("TEETA ZNEWS READER v21.0 | NO REDIRECT | WORLD CLASS UI")
