import streamlit as st

st.set_page_config(
    page_icon=":smiley:",
    page_title="TEST CODE",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS injected into the Streamlit app
st.markdown(
    """
    <style>
    /* 🛠️ NEW UPDATED CSS TO HIDE THE SIDEBAR AND THE EXPAND ARROW COMPLETELY */
    [data-testid="stSidebar"], 
    [data-testid="collapsedControl"] {
        display: none !important;
        width: 0px !important;
    }
    
    /* Adjusts the main content container to claim the hidden sidebar's blank space */
    .stMainBlockContainer {
        max-width: 100% !important;
        padding-left: 5rem !important;
        padding-right: 5rem !important;
    }

    /* Main container background and font */
    .stApp {
        background-color: #ffffff;
        color: #1e293b;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Header section styling */
    .header {
        background: linear-gradient(135deg, #facc15, #eab308);
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(234, 179, 8, 0.15);
        margin-bottom: 2rem;
    }
    .header h1 {
        color: #1e293b !important;
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        margin: 0 0 10px 0 !important;
        letter-spacing: -0.05em;
    }
    .header p {
        color: #451a03 !important;
        font-size: 1.1rem !important;
        margin: 0 !important;
        opacity: 0.85;
    }
    
    /* Base Column Box Styling */
    .column-box {
        background-color: #f8fafc;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        height: 100%;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .column-box:hover {
        transform: translateY(-2px);
        border-color: #eab308;
    }
    
    /* Typography inside column boxes */
    .column-box h2 {
        color: #ca8a04 !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin-top: 0 !important;
        margin-bottom: 1rem !important;
        line-height: 1.4 !important;
    }
    .column-box p {
        color: #475569 !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
        margin: 0 !important;
    }

    /* Main Content Section */
    .Main-content {
        background-color: #fef08a;
        padding: 2.5rem;
        border-radius: 16px;
        margin-top: 2rem;
        margin-bottom: 2rem;
        border: 1px solid #fef08a;
    }
    .Main-content h1 {
        color: #1e293b !important;
        font-size: 2rem !important;
        margin-top: 0 !important;
    }
    .Main-content p {
        color: #334155 !important;
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
        margin: 0 !important;
    }

    /* Custom layout styling for lower columns */
    .column3 {
        background-color: #f8fafc;
        padding: 2rem;
        border-radius: 12px 0 0 12px;
        border: 1px solid #e2e8f0;
        border-right: none;
        height: 100%;
    }
    .column3 h2 {
        color: #1e293b !important;
        margin: 0 !important;
    }
    
    .column4 {
        background-color: #ca8a04;
        padding: 2rem;
        border-radius: 0 12px 12px 0;
        height: 100%;
    }
    .column4 h2 {
        color: #ffffff !important;
        font-size: 1.2rem !important;
        margin: 0 0 8px 0 !important;
        font-weight: 600 !important;
    }
    .column4 h2:last-child {
        margin-bottom: 0 !important;
    }

    /* Footer Section Styling */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 2.5rem 1rem 1rem 1rem;
        background-color: #f8fafc;
        border-top: 2px dashed #e2e8f0;
        border-radius: 16px 16px 0 0;
    }
    .footer h1 {
        color: #1e293b !important;
        font-size: 1.75rem !important;
        font-weight: 700 !important;
        margin-bottom: 1.25rem !important;
    }

    /* Styling Native Streamlit Button for Footer Alignment */
    div.stButton {
        display: flex;
        justify-content: center;
        background-color: #f8fafc;
        padding-bottom: 2.5rem;
        border-radius: 0 0 16px 16px;
    }
    div.stButton > button {
        background-color: #1e293b !important;
        color: #ffffff !important;
        padding: 0.8rem 2.2rem !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        background-color: #ca8a04 !important;
        color: #ffffff !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(202, 138, 4, 0.3) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown(
    """
    <div class="header">
        <h1>THIS IS ONLY MADE FOR FUN</h1>
        <p>I am writing this code just for the sake of practice</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# About Me Section
st.markdown(
    """
    <div class="Main-content">
        <h1>I don't know why I am making this...</h1>
        <p>Hey, it's me Ruhaan! I am a BCA student and a beginner web developer. 
        I am making this web page just to improve my UI development skills.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Tools Section
col3, col4 = st.columns([1, 3])

with col3:
    st.markdown(
        """
        <div class="column3">
            <h2>Tools Used By Me</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="column4">
            <h2>VS Code</h2>
            <h2>Python</h2>
            <h2>Streamlit</h2>
            <h2>CSS</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Footer Title Section Open
st.markdown(
    """
    <div class="footer">
        <h1>Wanna Know More About Me??</h1>
    </div>
    """, 
    unsafe_allow_html=True
)
col7, col8, col9= st.columns([3,2,2])
# Native Streamlit Button Page Routing Condition
with col7:
    st.empty()

with col8:
    if st.button("PORTFOLIO", key="portfolio_page_btn"):
        st.switch_page("pages/portfolio.py")

with col9:
    st.empty()