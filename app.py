# ==========================================
# FILE NAME MANDATORY EXTENSION: app.py
# ==========================================
import streamlit as st
import time

# Set page title and layout
st.set_page_config(page_title="A Gift For Rida", page_icon="💝", layout="centered")

# Custom Styling for the romantic theme
st.markdown("""
    <style>
    /* Light pink background for the entire page */
    .stApp {
        background-color: #FFF0F2 !important;
    }
    
    h1, h2, h3 { color: #D63447 !important; font-family: 'Courier New', Courier, monospace; }
    
    .stButton>button {
        background-color: #FF8E9E; color: white; border-radius: 20px;
        padding: 10px 25px; border: none; font-size: 18px;
    }
    .stButton>button:hover { background-color: #D63447; color: white; }
    
    /* Letter box with a very soft pink background and dark pink text */
    .letter-box {
        background-color: #FFE3E7; 
        padding: 30px; 
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(214, 52, 71, 0.1); 
        border: 2px dashed #FF8E9E;
        font-family: 'Georgia', serif; 
        line-height: 1.6; 
        color: #9E1B32 !important; /* Beautiful Dark Pink/Crimson Text */
        font-size: 18px;
    }
    
    /* Background falling flower pattern behind the letter */
    .flower-bg {
        font-size: 24px;
        opacity: 0.3;
        text-align: center;
        user-select: none;
        margin-bottom: -20px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state to track pages
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- PAGE 1: THE WELCOME SCREEN ---
if st.session_state.page == 'welcome':
    st.markdown("<h1 style='text-align: center;'>HEY BABY!</h1>", unsafe_allow_html=True)
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
    st.markdown("<h1 style='text-align: center;'>AW PLEASE? 🥺</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>I prepared this special gift just for you...</p>", unsafe_allow_html=True)
    if st.button("⬅️ Go Back"):
        st.session_state.page = 'welcome'
        st.rerun()

# --- PAGE 2: THE FLOWERS VASE ---
elif st.session_state.page == 'flowers':
    st.markdown("<h1 style='text-align: center;'>Flowers For You 🌹✨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Click the button below to open your virtual flowers and anniversary letter</p>", unsafe_allow_html=True)
    
    # Large floral arrangement display
    st.markdown("<div style='text-align: center; font-size: 100px; margin: 10px 0;'>🌹💮🌷🌸💮🌹</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #D63447;'>A bouquet of Lilies and Roses just for my future wife!</p>", unsafe_allow_html=True)
    
    if st.button("Open Rida's Anniversary Letter ✉️"):
        with st.spinner("Unfolding your letter..."):
            time.sleep(1.5)
        st.session_state.page = 'letter'
        st.rerun()

# --- PAGE 3: THE HEARTFELT LETTER & VIDEO ---
elif st.session_state.page == 'letter':
    st.markdown("<h2 style='text-align: center;'>Happy 6-Month Anniversary, My Love! ❤️</h2>", unsafe_allow_html=True)
    
    # Sweet instrumental background music
    st.markdown("""
        <iframe src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" allow="autoplay" id="audio" style="display:none;"></iframe>
        <audio autoplay loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

    # Cute Lily and Rose background elements above the letter
    st.markdown('<div class="flower-bg">🌸 🌹 🌷 🌸 🌹 🌷 🌸 🌹 🌷</div>', unsafe_allow_html=True)

    # Cleaned up layout with Dark Pink Text and Light Pink Card background
    st.markdown(f"""
    <div class="letter-box">
        <p><strong>Dearest Rida, My Future Wife,</strong></p>
        
        <p>Happy 6-month Monthsary! I can’t believe how fast time has flown, yet every single 
        moment with you feels incredibly special. Even though distance keeps us physically apart right now, 
        sending you these virtual lilies and roses is just a small reminder of how deeply you are always 
        rooted in my heart.</p>
        
        <p>Meeting you has been the greatest blessing of my life. You've brought so much genuine joy, warmth, 
        and bright color into my world. Before you, my days were ordinary, but knowing you are in my life 
        makes everything feel extraordinary. You make me feel seen, safe, and deeply loved in ways I never 
        imagined possible.</p>
        
        <p><strong>I want to take a moment to tell you how incredibly proud I am of you. You are one of the 
        strongest, most resilient people I have ever known. Watching how beautifully you handle everything 
        inspires me daily. Facing a long-distance relationship isn't always easy, but your strength makes us 
        unbreakable, and it makes me honor you even more as my future wife.</strong></p>
        
        <p>I cherish everything about us—the way we laugh together over the simplest things, the comfort 
        of your voice, and the beautiful future we are building step by step. You are not just my partner; 
        you are my home.</p>
        
        <p>As we celebrate hitting this beautiful 6-month milestone, I want you to know that my love for 
        you grows stronger every single day. I am so excited for all the memories we have yet to create, 
        the dreams we will chase, and the beautiful life we will build together once the distance is finally zero.</p>
        
        <p>Thank you for staying, for loving me so perfectly, and for just being you.</p>
        
        <p style='text-align: right;'><strong>Yours truly, forever and always,</strong><br>❤️</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cute Lily and Rose background elements below the letter
    st.markdown('<div class="flower-bg">🌷 🌹 🌸 🌷 🌹 🌸 🌷 🌹 🌸</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h3 style='text-align: center;'>Our Special Video Memory 🎥</h3>", unsafe_allow_html=True)
    
    # Integrates the video file into the interface
    try:
        with open('WhatsApp Video 2026-06-16 at 12.50.00 AM.mp4', 'rb') as video_file:
            video_bytes = video_file.read()
            st.video(video_bytes)
    except FileNotFoundError:
        st.warning("To display your video here, make sure to upload 'WhatsApp Video 2026-06-16 at 12.50.00 AM.mp4' to your GitHub project folder!")

    # Floral footer decoration
    st.markdown("<div style='text-align: center; font-size: 30px; margin-top: 30px;'>⚜️ 🌹 ⚜️ 🌷 ⚜️</div>", unsafe_allow_html=True)
