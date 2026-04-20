import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

st.set_page_config(page_title="TEETA NEURAL OS", page_icon="🧠", layout="wide")

API_KEY = "AIzaSyDR5qfvuNz9m_agr53g1ZywlZHjZ697fdI"
genai.configure(api_key=API_KEY)

def get_brain():
    models_to_try = ['gemini-1.5-flash-latest', 'gemini-1.5-flash', 'gemini-pro']
    for m in models_to_try:
        try:
            brain = genai.GenerativeModel(m)
            brain.generate_content("ping")
            return brain
        except: continue
    return None

model = get_brain()

st.markdown("<style>.stApp {background-color: #050505; color: #00ffcc;} .ai-bubble {background: #161b22; padding: 25px; border-radius: 15px; border-left: 5px solid #00ffcc;}</style>", unsafe_allow_html=True)

if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if not st.session_state.logged_in:
    c1, c2, c3 = st.columns(3)
    with c2:
        st.subheader("🔐 TRUY CẬP VIP")
        user = st.text_input("Username:")
        pwd = st.text_input("Password:", type="password")
        if st.button("KÍCH HOẠT"):
            if user == "admin" and pwd == "teeta2026":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("Sai rồi đại ca!")
    st.stop()

with st.sidebar:
    st.title("🧠 TEETA OS V26")
    menu = st.radio("CHỌN:", ["🤖 TRỢ LÝ AI", "🎵 NHẠC", "🎬 PHIM", "📰 TIN TỨC"])

if menu == "🤖 TRỢ LÝ AI":
    st.header("🤖 Trợ Lý AI Teeta")
    user_input = st.text_area("Ra lệnh cho AI:")
    if st.button("KÍCH HOẠT LỆNH"):
        if model:
            with st.spinner("🧠 AI đang nghĩ..."):
                try:
                    response = model.generate_content(f"Trả lời tiếng Việt: {user_input}")
                    st.markdown(f"<div class='ai-bubble'>{response.text}</div>", unsafe_allow_html=True)
                    with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
                        res = ydl.extract_info(user_input, download=False)['entries']
                        st.video(res[0]['webpage_url'])
                except Exception as e: st.error(f"Lỗi: {e}")
        else: st.error("Lỗi API Key!")

elif menu == "🎵 NHẠC":
    q = st.text_input("Tìm nhạc:")
    if q:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
            res = ydl.extract_info(q, download=False)['entries']
            st.video(res[0]['webpage_url'])

elif menu == "📰 TIN TỨC":
    st.header("📰 ZNews Reader")
    try:
        resp = requests.get("https://znews.vn", headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        for art in soup.find_all('article', limit=5):
            title = art.find('p', class_='article-title') or art.find('h3')
            if title: st.markdown(f"<div class='ai-bubble'><b>🔥 {title.get_text()}</b></div>", unsafe_allow_html=True)
    except: st.error("Lỗi kết nối!")

st.caption("TEETA OS V26.0 | 20/04/2026")
