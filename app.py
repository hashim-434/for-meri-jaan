# ==========================================
# FILE NAME MANDATORY EXTENSION: app.py
# ==========================================
import streamlit as st
import time

# Set page title and layout
st.set_page_config(page_title="A Gift For Rida", page_icon="💝", layout="centered")

# Custom CSS Styling for the romantic theme
st.markdown("""
    <style>
    /* Soft light pink background for the whole page */
    .stApp {
        background-color: #FFF0F2 !important;
    }
    
    /* Elegant Romantic Headings */
    h1, h2, h3 { 
        color: #D63447 !important; 
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    
    /* Interactive Buttons styling */
    .stButton>button {
        background-color: #FF8E9E; color: white; border-radius: 20px;
        padding: 10px 25px; border: none; font-size: 18px;
    }
    .stButton>button:hover { background-color: #D63447; color: white; }
    
    /* Deep Crimson/Dark Pink Paragraph text styling */
    .romantic-text {
        font-family: 'Georgia', serif;
        font-size: 19px;
        color: #9E1B32 !important; /* Beautiful Dark Pink/Crimson */
        line-height: 1.7;
        margin-bottom: 15px;
    }
    
    .romantic-text-bold {
        font-family: 'Georgia', serif;
        font-size: 19px;
        color: #9E1B32 !important;
        line-height: 1.7;
        margin-bottom: 15px;
        font-weight: bold;
    }
    
    /* Floral background dividers */
    .flower-divider {
        font-size: 24px;
        opacity: 0.4;
        text-align: center;
        user-select: none;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state to track pages
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- PAGE 1: THE WELCOME SCREEN ---
if st.session_state.page == 'welcome':
    st.markdown("<h1>HEY BABY!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #666;'>WOULD YOU LIKE TO SEE YOUR GIFT?</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col2:
        if st.button("❌"):
            st.session_state.page = 'rejected'
            st.rerun()
    with col3:
        if st.button("✅"):
            st.session_state.page = 'flowers'
            st.rerun()

# --- PAGE 1b: IF SHE CLICKS NO ---
elif st.session_state.page == 'rejected':
    st.markdown("<h1>AW PLEASE? 🥺</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>I prepared this special gift just for you...</p>", unsafe_allow_html=True)
    if st.button("⬅️ Go Back"):
        st.session_state.page = 'welcome'
        st.rerun()

# --- PAGE 2: THE FLOWERS VASE ---
elif st.session_state.page == 'flowers':
    st.markdown("<h1>Flowers For You 🌹✨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Click the button below to open your virtual flowers and anniversary letter</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='text-align: center; font-size: 100px; margin: 10px 0;'>🌹💮🌷🌸💮🌹</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #D63447;'>A bouquet of Lilies and Roses just for my future wife!</p>", unsafe_allow_html=True)
    
    if st.button("Open Rida's Anniversary Letter ✉️"):
        with st.spinner("Unfolding your letter..."):
            time.sleep(1.5)
        st.session_state.page = 'letter'
        st.rerun()

# --- PAGE 3: THE HEARTFELT LETTER & VIDEO ---
elif st.session_state.page == 'letter':
    st.markdown("<h2>Happy 6-Month Anniversary, My Love! ❤️</h2>", unsafe_allow_html=True)
    
    # Plays ONLY Arctic Monkeys - I Wanna Be Yours smoothly in the background
    st.write(
        f'<iframe src="https://www.youtube.com/embed/nyuo9-OjNNg?autoplay=1&loop=1&playlist=nyuo9-OjNNg" width="0" height="0" frameborder="0" allow="autoplay"></iframe>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="flower-divider">🌸 🌹 🌷 🌸 🌹 🌷 🌸 🌹 🌷</div>', unsafe_allow_html=True)

    # Creating a beautiful container for the letter with zero string leaks
    with st.container():
        st.markdown('<p class="romantic-text"><strong>Dearest Rida, My Future Wife,</strong></p>', unsafe_allow_html=True)
        
        st.markdown('<p class="romantic-text">Happy 6-month Monthsary! I can’t believe how fast time has flown, yet every single moment with you feels incredibly special. Even though distance keeps us physically apart right now, sending you these virtual lilies and roses is just a small reminder of how deeply you are always rooted in my heart.</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="romantic-text">Meeting you has been the greatest blessing of my life. You\'ve brought so much genuine joy, warmth, and bright color into my world. Before you, my days were ordinary, but knowing you are in my life makes everything feel extraordinary. You make me feel seen, safe, and deeply loved in ways I never imagined possible.</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="romantic-text-bold">I want to take a moment to tell you how incredibly proud I am of you. You are one of the strongest, most resilient people I have ever known. Watching how beautifully you handle everything inspires me daily. Facing a long-distance relationship isn\'t always easy, but your strength makes us unbreakable, and it makes me honor you even more as my future wife.</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="romantic-text">I cherish everything about us—the way we laugh together over the simplest things, the comfort of your voice, and the beautiful future we are building step by step. You are not just my partner; you are my home.</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="romantic-text">As we celebrate hitting this beautiful 6-month milestone, I want you to know that my love for you grows stronger every single day. I am so excited for all the memories we have yet to create, the dreams we will chase, and the beautiful life we will build together once the distance is finally zero.</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="romantic-text">Thank you for staying, for loving me so perfectly, and for just being you.</p>', unsafe_allow_html=True)
        
        st.markdown('<p style="text-align: right; color: #9E1B32; font-family: Georgia; font-size: 19px;"><strong>Yours truly, forever and always,</strong><br>❤️</p>', unsafe_allow_html=True)

    st.markdown('<div class="flower-divider">🌷 🌹 🌸 🌷 🌹 🌸 🌷 🌹 🌸</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h3>Our Special Video Memory 🎥</h3>", unsafe_allow_html=True)
    
    # Integrates your WhatsApp video file into the layout
    try:
        with open('WhatsApp Video 2026-06-16 at 12.50.00 AM.mp4', 'rb') as video_file:
            video_bytes = video_file.read()
            st.video(video_bytes)
    except FileNotFoundError:
        st.warning("To display your video here, make sure to upload 'WhatsApp Video 2026-06-16 at 12.50.00 AM.mp4' to your GitHub repository folder!")

    st.markdown("<div style='text-align: center; font-size: 30px; margin-top: 30px;'>⚜️ 🌹 ⚜️ 🌷 ⚜️</div>", unsafe_allow_html=True)
