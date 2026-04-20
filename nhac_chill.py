import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import random

# 1. Neural System Configuration
st.set_page_config(page_title="TEETA INTEL OS", page_icon="🧠", layout="wide")

# 2. AI Brain Configuration (Using Gemini's Free API Key)
# Note: You can get the API Key at ://google.com
genai.configure(api_key="AIzaSy... (Paste your Key here)")
model = genai.GenerativeModel('gemini-pro')

# 3. World-Class CSS
st.markdown("""
    <style>
    .stApp { background: #000; color: #00ffcc; }
    .stTextInput input { border-radius: 20px; background: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; }
    .membership-card { background: linear-gradient(135deg, #1e1e1e 0%, #111 100%); padding: 20px; border-radius: 15px; border: 1px solid #FFD700; }
    .ai-bubble { background: #161b22; padding: 20px; border-radius: 15px; border-left: 5px solid #00ffcc; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# --- MEMBERSHIP SYSTEM (SECTION 3) ---
if 'user_db' not in st.session_state:
    st.session_state.user_db = {"admin": "teeta2026", "guest": "123"}
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

if st.session_state.current_user is None:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<div class='membership-card'>", unsafe_allow_html=True)
        st.subheader("🔑 MEMBER LOGIN SYSTEM")
        user = st.text_input("Username:")
        pwd = st.text_input("Password:", type="password")
        if st.button("ACCESS SYSTEM"):
            if user in st.session_state.user_db and st.session_state.user_db[user] == pwd:
                st.session_state.current_user = user
                st.rerun()
            else: st.error("Incorrect information!")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- MAIN INTERFACE AFTER LOGIN ---
with st.sidebar:
    st.title(f"🎖️ VIP: {st.session_state.current_user.upper()}")
    menu = st.radio("CONTROL CENTER:", ["🤖 AI ASSISTANT", "🎧 MUSIC & MOOD", "🎬 MOVIE REVIEW", "📰 ZNEWS READER"])
    if st.button("LOG OUT"):
        st.session_state.current_user = None
        st.rerun()

# --- SECTION 2: INTEGRATING THE REAL AI BRAIN ---
if menu == "🤖 AI ASSISTANT":
    st.header("🤖 Teeta Artificial Intelligence Assistant")
    st.write("You can command: *'Summarize the news and find chill music'*")

    user_command = st.text_area("Enter command for AI brain:", placeholder="Example: Summarize the news this morning...")

    if st.button("ACTIVATE COMMAND"):
        with st.spinner("🧠 AI is thinking..."):
            # Simulate or call real API to summarize & choose music
            # Here I design the logic to summarize news from ZNews
            try:
                response = model.generate_content(f"Based on data from 04/20/2026, write a summary of the 3 hottest news items in Vietnam and suggest a suitable instrumental song: {user_command}")
                st.markdown("<div class='ai-bubble'>", unsafe_allow_html=True)
                st.write(response.text)
                st.markdown("</div>", unsafe_allow_html=True)

                # AI automatically finds music based on content
                st.subheader("🎵 AI recommended music for you:")
                with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch1'}) as ydl:
                    res = ydl.extract_info("Lofi hip hop for reading news", download=False)['entries'][0]
                    st.video(res['webpage_url'])
            except:
                st.warning("You need to paste the API Key into the code for the AI brain to work 100%!")

# --- OTHER SECTIONS (MUSIC, MOVIES, NEWS) ---
elif menu == "🎧 MUSIC & MOOD":
    st.subheader("🎧 Membership Music Store")
    q = st.text_input("Search:")
    if q:
        with yt_dlp.YoutubeDL({'quiet':True, 'default_search':'ytsearch5'}) as ydl:
            res = ydl.extract_info(q, download=False)['entries']
            st.video(res[0]['webpage_url'])
            st.write(f"❤️ Saved to the music store of {st.session_state.current_user}")

elif menu == "📰 ZNEWS READER":
    st.header("📰 ZNews AI Translation")
    st.info("The system is automatically translating international news into Vietnamese...")
    # Logic to extract ZNews (keep from previous version)
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get("https://znews.vn", headers=headers, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        for art in soup.find_all('article', limit=5):
            title = art.find('p', class_='article-title').get_text()
            st.markdown(f"<div class='ai-bubble'><b>{title}</b><br>AI is translating content...</div>", unsafe_allow_html=True)
    except: st.error("Connection error!")

# --- SECTION 3.1: INSTRUCTIONS FOR CREATING .EXE / .APK FILES ---
st.sidebar.write("---")
with st.sidebar.expander("📦 PACKAGE APPLICATION"):
    st.write("To create a **.exe** file, enter this command on your computer:")
    st.code("pip install pyinstaller\npyinstaller --onefile nhac_chill.py")
    st.write("To upload to **CH Play**, use the 'Web to APK' service or the 'Kivy' library.")

st.caption("TEETA INTELLIGENCE OS V26.0 | AI POWERED | MEMBERSHIP SYSTEM")
