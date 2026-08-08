import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Ruhaan-Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Unique Creative & Ambitious Theme CSS Injection
# 2. Unique Creative Theme CSS Injection (Light Gray / White Mode)
st.markdown("""
<style>
   /* 🛠️ NEW UPDATED CSS TO HIDE THE SIDEBAR AND THE EXPAND ARROW COMPLETELY */
    [data-testid="stSidebar"], 
    [data-testid="collapsedControl"] {
        display: none !important;
        width: 0px !important;
    }

    /* Main background and global text color changed to Light Theme */
    .stApp {
        background-color: #f8fafc !important; /* Soft, premium light slate/gray */
        color: #1e293b !important; /* Deep dark charcoal for readable body text */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* Top header styling with creative gradient glow preserved */
    .header_container {
        border-bottom: 2px solid #ff7a00;
        padding-bottom: 25px;
        margin-bottom: 50px;
        background: linear-gradient(90deg, #ff7a00 0%, #ff007a 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 2px 4px rgba(255, 122, 0, 0.1));
    }
    .header_container h1 {
        font-size: 3.2rem !important;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0;
    }

    /* Left column section header */
    .column1_p h1 {
        color: #ff7a00 !important; /* Warm electric orange/amber */
        font-size: 1.6rem !important;
        font-weight: 700;
        letter-spacing: 0.5px;
        position: relative;
    }
    
    /* Small accent underline for the About Me header */
    .column1_p h1::after {
        content: '';
        display: block;
        width: 40px;
        height: 3px;
        background: #ff007a;
        margin-top: 8px;
        border-radius: 2px;
    }

    /* Right column about text container tuned for light gray background */
    .column2_p {
        background: #ffffff; /* Crisp pure white card surface */
        border: 1px solid #e2e8f0;
        padding: 30px;
        border-radius: 12px;
        margin-bottom: 30px;
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.05); /* Subtle clean soft shadow */
    }
    .column2_p p {
        color: #475569 !important; /* Professional slate gray body text */
        line-height: 1.8 !important;
        font-size: 1.1rem !important;
    }

    /* Lower content links section */
    .main_content {
        margin-top: 60px;
        padding-top: 40px;
        border-top: 1px solid #e2e8f0;
    }
    .main_c_title {
        color: #1e293b !important;
        font-size: 1.6rem !important;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 50px;
    }
    
    /* Project Image Container Styling with Dynamic Pop Hover */
    .project_one_img {
        width: 100%;
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .project_one_img img {
        width: 100%;
        max-width: 320px;
        height: auto;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background-color: #ffffff;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Bouncy pop preserved */
    }
    /* Hover effects preserved and enhanced for light theme contrast */
    .project_one_img img:hover {
        transform: translateY(-8px) scale(1.05);
        border-color: #ff7a00;
        box-shadow: 0 15px 30px rgba(255, 122, 0, 0.15);
    }

    /* Right Side Wrapper to manage layout spacing & alignment */
    .project_text_wrapper {
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
        margin-bottom: 60px;
    }

    /* Project description styling */
    .project_desc {
        color: #475569 !important;
        font-size: 1.1rem !important;
        line-height: 1.7;
        margin-bottom: 25px !important;
        text-align: left;
    }
    .project_desc strong {
        color: #1e293b !important;
        font-size: 1.2rem;
    }

    /* Wrapper container to center the button link */
    .btn_center_container {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    
    /* Cool Project Links with Sliding Liquid Gradient Animation preserved */
    .project_link {
        display: inline-block;
        color: #1e293b !important; /* Dark text for light mode visibility */
        text-decoration: none;
        border: 2px solid transparent;
        background: linear-gradient(#ffffff, #ffffff) padding-box,
                    linear-gradient(90deg, #ff7a00, #ff007a) border-box; /* Gradient border wrapper */
        padding: 10px 28px;
        border-radius: 30px;
        font-size: 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        text-align: center;
    }
    /* Hover fill-in animation preserved */
    .project_link:hover {
        background: linear-gradient(90deg, #ff7a00, #ff007a) border-box;
        color: #ffffff !important; /* Flips text color to white on gradient hover fill */
        box-shadow: 0 8px 20px rgba(255, 0, 122, 0.2);
        transform: translateY(-2px);
    }

    /* Footer container styling preserved */
    .footer_container {
        margin-top: 100px;
        padding: 40px 20px;
        border-top: 1px solid #e2e8f0;
        text-align: center;
    }
    .footer_text {
        color: #94a3b8 !important;
        font-size: 0.95rem;
        margin-bottom: 15px;
    }
    .footer_links {
        display: flex;
        justify-content: center;
        gap: 25px;
    }
    .footer_social_link {
        color: #64748b !important;
        text-decoration: none;
        font-size: 0.95rem;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    .footer_social_link:hover {
        color: #ff7a00 !important;
    }
</style>
""", unsafe_allow_html=True)


# 3. Layout and Content
st.markdown('<div class="header_container"><h1>Ruhaan Kapoor</h1></div>', unsafe_allow_html=True)

# --- ABOUT ROW ---
col1, col2 = st.columns([2, 3])

with col1:  
    st.markdown('<div class="column1_p"><h1>About Me</h1></div>', unsafe_allow_html=True)    

with col2:
    st.markdown("""
    <div class="column2_p">
        <p>I am a student who loves to learn new skills. 
        I am not a programming expert, nor am I deeply familiar with coding, yet I like to create new programs and web pages.</p>
        <p>This is my portfolio, built for fun. Check out the links to my other projects below.</p>
    </div>
    """, unsafe_allow_html=True)  

# --- PROJECTS ROW ---
st.markdown('<div class="main_content">', unsafe_allow_html=True)
st.markdown('<h2 class="main_c_title">My Creations</h2>', unsafe_allow_html=True)

# --- PROJECT 1: XP TRACKER ---
col3, col4 = st.columns([1, 4])
with col3:
    # High-quality gaming abstract setup picture for XP Tracker placeholder
    img_url_1 = "static/xp.png"
    st.image(img_url_1, use_container_width=True) 
with col4:
    st.markdown("""
    <div class="project_text_wrapper">
        <p class="project_desc"><strong>XP Tracker:</strong> A webpage which helps gamers to track prices of their favourite games from different platforms and compare them.</p>
        <div class="btn_center_container">
            <a class="project_link" href="https://xp-tracker-version-1.streamlit.app/" target="_blank">View Live Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PROJECT 2: PLACEHOLDER ---
col5, col6 = st.columns([1, 4])
with col5:
    img_url_2 = "static/unitc.png"
    st.image(img_url_2, use_container_width=True) 
with col6:
    st.markdown("""
    <div class="project_text_wrapper">
        <p class="project_desc"><strong>Unit Converter:</strong> Unit Converter is a web app used to convert Units, it has a beautiful and responsive UI.</p>
        <div class="btn_center_container">
            <a class="project_link" href="https://unit-converter-v1.streamlit.app/" target="_blank">View Live Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PROJECT 3: PLACEHOLDER ---
col7, col8 = st.columns([1, 4])
with col7:
    img_url_3 = "static/pricec.png"
    st.image(img_url_3, use_container_width=True) 
with col8:
    st.markdown("""
    <div class="project_text_wrapper">
        <p class="project_desc"><strong>Price Cleaner:</strong> Price Cleaner is a web app used to remove any other details or symbols from text and give Float values in return.</p>
        <div class="btn_center_container">
            <a class="project_link" href="https://price-cleaner-class-project-v1.streamlit.app/" target="_blank">View Live Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PROJECT 4: PLACEHOLDER ---
col9, col10 = st.columns([1, 4])
with col9:
    img_url_4 = "static/authui.png"
    st.image(img_url_4, use_container_width=True) 
with col10:
    st.markdown("""
    <div class="project_text_wrapper">
        <p class="project_desc"><strong>AUTH UI:</strong> A clean login page with modern and beautiful UI with responsiveness.</p>
        <div class="btn_center_container">
            <a class="project_link" href="https://appui-ch-v1.streamlit.app/" target="_blank">View Live Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 4. NEW FOOTER SECTION ---
# Add your real profile links by changing the href="#" fields below
st.markdown("""
<div class="footer_container">
    <p class="footer_text">Designed & Developed by Ruhaan Kapoor</p>
    <div class="footer_links">
        <a class="footer_social_link" href="https://github.com" target="_blank">GitHub Profile</a>
        <a class="footer_social_link" href="https://streamlit.io" target="_blank">Streamlit Community Cloud</a>
    </div>
</div>
""", unsafe_allow_html=True)
