import streamlit as st
import os
from groq import Groq
import json

# Page configuration
st.set_page_config(
    page_title="AI Story Generator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Cinematic Dark Theme
st.markdown("""
<style>
    /* Global Reset & Fonts */
    @import url('https://fonts.googleapis.com/css2?family= outfit:wght@300;400;500;600&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap');

    :root {
        --bg-color: #030712;
        --card-bg: rgba(17, 24, 39, 0.7);
        --text-primary: #f3f4f6;
        --text-secondary: #9ca3af;
        --accent-glow: rgba(99, 102, 241, 0.4);
        --border-subtle: rgba(255, 255, 255, 0.08);
    }

    .stApp {
        background-color: var(--bg-color);
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(56, 189, 248, 0.08), transparent 25%), 
            radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.08), transparent 25%);
        font-family: 'Outfit', sans-serif;
        color: var(--text-primary);
    }
    
    /* Hide Sidebar */
    [data-testid="stSidebar"] { display: none; }

    /* Typography */
    h1 {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 3rem;
        background: linear-gradient(to bottom right, #ffffff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: -0.03em;
        margin-bottom: 0.5rem;
    }

    h2, h3 {
        font-family: 'Outfit', sans-serif;
        font-weight: 500;
        color: var(--text-primary);
        letter-spacing: -0.01em;
    }

    p, label, .stMarkdown {
        color: var(--text-secondary) !important;
        font-weight: 300;
    }

    /* Inputs - Soft Glass */
    .stTextInput > div > div > input, 
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input {
        background-color: rgba(30, 41, 59, 0.4);
        border: 1px solid var(--border-subtle);
        border-radius: 12px;
        color: var(--text-primary);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus, 
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(99, 102, 241, 0.5);
        background-color: rgba(30, 41, 59, 0.6);
        box-shadow: 0 0 20px var(--accent-glow);
    }
    
    /* Remove input top borders from streamlit labels */
    .stTextInput, .stTextArea, .stSelectbox, .stNumberInput {
        border-radius: 12px;
        border: none;
    }

    /* Buttons - Glowing Gradient */
    .stButton > button {
        background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
        color: white;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 0.6rem 1.5rem;
        font-weight: 500;
        letter-spacing: 0.02em;
        box-shadow: 0 4px 20px rgba(79, 70, 229, 0.2);
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(79, 70, 229, 0.4);
        border-color: rgba(255,255,255,0.3);
    }

    /* Configuration Expander */
    div[data-testid="stExpander"] {
        background-color: rgba(15, 23, 42, 0.3);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
    }

    /* Story Card */
    .story-container {
        font-family: 'Merriweather', serif;
        font-size: 1.15rem;
        line-height: 1.9;
        color: #e5e7eb;
        background: rgba(17, 24, 39, 0.4);
        padding: 3.5rem;
        border-radius: 16px;
        border: 1px solid var(--border-subtle);
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.5);
        margin-top: 2rem;
        white-space: pre-wrap;
    }
    
    /* sliders */
    .stSlider [data-baseweb="slider"] {
        margin-top: 1rem;
    }

</style>
""", unsafe_allow_html=True)

# Helper Functions
def get_api_key():
    try:
        return st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
    except FileNotFoundError:
        return os.environ.get("GROQ_API_KEY")

def generate_story_with_groq(client, model, prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a master storyteller. Output only the story content."},
                {"role": "user", "content": prompt}
            ],
            model=model,
            temperature=0.8,
            max_tokens=4096, 
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Main App Layout
def main():
    # Header
    st.markdown("""
        <h1>AI Story Generator</h1>
        <div style="text-align: center; margin-bottom: 3rem; color: #94a3b8; font-family: 'Outfit', sans-serif; font-weight: 300;">
            Weaving digital dreams into narrative reality
        </div>
    """, unsafe_allow_html=True)

    # Initialize Session State
    if 'generated_story' not in st.session_state:
        st.session_state.generated_story = ""

    # Main Content Columns
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### Narrative Elements")
        
        # Genre Selection
        genre = st.selectbox(
            "Genre", 
            [
                "Sci-Fi", "Fantasy", "Cyberpunk", "Horror", "Noir", 
                "Young Adult (YA)", "Mystery/Thriller", "Romance", "LGBTQ+ Fiction", 
                "Memoir", "Self-Help", "Pop Culture Nonfiction", "Historical Nonfiction", "Investigative Journalism",
                "Abstract", "Surreal", "Ambient", "Experimental", "Cinematic",
                "Dystopian", "Space Opera", "Gothic", "Steampunk", "Post-Apocalyptic", 
                "Mythological", "Psychological Thriller", "Eldritch Horror", "Magical Realism",
                "Historical", "Western", "Mystery", "Hard Sci-Fi", "Solarpunk"
            ], 
            index=2
        )
        
        tone = st.select_slider("Tone", options=["Bleak", "Melancholic", "Neutral", "Hopeful", "Euphoric"], value="Neutral")
        length = st.select_slider("Length", options=["Flash", "Short", "Extended"], value="Short")

        st.markdown("### Protagonists")
        num_chars = st.number_input("Count", min_value=1, max_value=4, value=1)
        
        characters = []
        for i in range(int(num_chars)):
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input(f"Name", key=f"char_name_{i}", placeholder="e.g. Kael")
            with c2:
                role = st.text_input(f"Archetype", key=f"char_role_{i}", placeholder="e.g. Drifter")
            if name:
                characters.append(f"{name} ({role if role else 'Unknown'})")

    with col2:
        st.markdown("### World Building")
        setting = st.text_input("Setting", placeholder="e.g. A rain-slicked neo-tokyo alleyway...")
        plot_twist = st.text_area("Directives / Twists", height=200, placeholder="Enter specific themes, constraints, or mandatory plot points...")
        
        # Model Selection (User-Friendly)
        model_map = {
            "Cinematic (Rich Detail)": "llama-3.3-70b-versatile",
            "Classic (Balanced)": "llama-3.1-70b-versatile", 
            "Fast (Quick Reads)": "mixtral-8x7b-32768"
        }
        
        selected_style = st.selectbox("Narrative Style", options=list(model_map.keys()), index=0)
        model_option = model_map[selected_style]
        
        # API Key check (Silent)
        api_key = get_api_key()

        st.write("") 
        st.write("") 
        generate_btn = st.button("Generate Story", type="primary")

    # Generation Logic
    if generate_btn:
        if not api_key:
            st.error("Configuration Error: API Key is missing.")
        else:
            with st.spinner("Fabricating narrative layer..."):
                char_str = ", ".join(characters) if characters else "unidentified_entity"
                prompt_text = (
                    f"Write a {length.lower()} story in the {genre} genre. Tone: {tone.lower()}.\n"
                    f"Setting: {setting or 'undefined'}.\n"
                    f"Key Characters: {char_str}.\n"
                    f"Directives: {plot_twist}\n\n"
                    "Focus on sensory details, subtext, and immersion. Avoid clichés."
                )
                
                client = Groq(api_key=api_key)
                story_output = generate_story_with_groq(client, model_option, prompt_text)
                st.session_state.generated_story = story_output
                st.rerun()

    # Output Display
    if st.session_state.generated_story:
        st.markdown("---")
        st.subheader("Generated Manuscript")
        st.markdown(f'<div class="story-container">{st.session_state.generated_story}</div>', unsafe_allow_html=True)
        
        st.write("")
        st.download_button(
            label="Download Log",
            data=st.session_state.generated_story,
            file_name="story.md",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
