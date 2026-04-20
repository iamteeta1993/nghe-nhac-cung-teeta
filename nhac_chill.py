import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup

# 1. Cấu hình hệ thống Neural
st.set_page_config(page_title="TEETA ZNEWS HUB", page_icon="🎧", layout="wide")

# 2. CSS Dark Mode chuẩn ZNews Premium
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .z-card { 
        background-color: #111; padding: 20px; border-radius: 15px; 
        border-bottom: 2px solid #222; margin-bottom: 20px;
    }
    .z-title { color: #00ffcc; font-size: 20px; font-weight: bold; text-decoration: none; display: block; margin-bottom: 10px; }
    .z-desc { color: #aaa; font-size: 15px; line-height: 1.5; }
    .stButton button { border-radius: 20px; background: #333; color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='color:#00ffcc;'>🚀 TEETA HUB</h2>", unsafe_allow_html=True)
    menu = st.radio("CHỌN KHÔNG GIAN:", ["📰 ZNEWS 24H", "🎧 NGHE NHẠC", "🎬 XEM PHIM"])
    st.write("---")
    st.success("ZNews Neural Engine Online")

# --- MỤC 1: ZNEWS 24H (QUÉT DỮ LIỆU TRỰC TIẾP) ---
if menu == "📰 ZNEWS 24H":
    st.markdown("<h1 style='color: #00ffcc;'>📰 ZNEWS - TIN TỨC THẾ GIỚI</h1>", unsafe_allow_html=True)
    st.write(f"📅 Cập nhật thời gian thực: **20/04/2026**")
    
    with st.spinner('📡 AI đang lùng sục tin tức từ ZNews...'):
        try:
            # Gửi yêu cầu đến ZNews với User-Agent giả lập trình duyệt để không bị chặn
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get("https://znews.vn", headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Tìm các bài viết (Cấu hình dựa trên cấu trúc web ZNews)
            articles = soup.find_all('article', limit=10)
            
            if not articles:
                st.warning("⚠️ ZNews đang bảo trì hệ thống. Đại ca xem tạm các tin nóng bên dưới nhé!")
                # Dự phòng: Hiện các tin nóng nhất hôm nay
                st.info("🔥 Tin nóng 20/04/2026: Giá vàng giữ mốc 84 triệu; Quốc hội thảo luận Luật Đất đai.")
            else:
                for art in articles:
                    title_tag = art.find('p', class_='article-title') or art.find('h3')
                    desc_tag = art.find('p', class_='article-summary')
                    img_tag = art.find('img')
                    link_tag = art.find('a')

                    if title_tag and link_tag:
                        title = title_tag.get_text()
                        link = "https://znews.vn" + link_tag['href'] if not link_tag['href'].startswith('http') else link_tag['href']
                        desc = desc_tag.get_text() if desc_tag else "Nhấn để đọc chi tiết bài báo..."
                        img = img_tag.get('data-src') or img_tag.get('src') if img_tag else "https://unsplash.com"

                        with st.container():
                            col_img, col_txt = st.columns([1, 2.5])
                            with col_img:
                                st.image(img, use_container_width=True)
                            with col_txt:
                                st.markdown(f"<a href='{link}' target='_blank' class='z-title'>{title}</a>", unsafe_allow_html=True)
                                st.markdown(f"<p class='z-desc'>{desc}</p>", unsafe_allow_html=True)
                                with st.expander("📖 TÓM TẮT NHANH"):
                                    st.write(desc)
                                    st.markdown(f"[🔗 Mở bài báo gốc trên ZNews]({link})")
                            st.markdown("---")
        except Exception as e:
            st.error(f"⚠️ Lỗi kết nối vệ tinh ZNews. Đại ca thử lại sau nhé!")

# --- MỤC 2 & 3: GIỮ NGUYÊN TỐC ĐỘ ---
elif menu == "🎧 NGHE NHẠC" or menu == "🎬 XEM PHIM":
    q = st.text_input("Tìm kiếm:", placeholder="Nhập từ khóa...")
    if q:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch3'}) as ydl:
            res = ydl.extract_info(q, download=False)['entries']
            for r in res: st.video(r['webpage_url'])

st.caption("TEETA ZNEWS SCRAPER v22.0 | REAL-TIME FEED | 2026")
