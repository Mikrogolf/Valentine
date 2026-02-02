import streamlit as st
import streamlit.components.v1 as components

# 1. Setup Session State
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

st.set_page_config(page_title="A Special Message", layout="centered")

st.title("I Was Going To Ask You...")

# 2. Unlocker Button
if not st.session_state.unlocked:
    st.write("I made something for you. Are you ready?")
    if st.button("I'm Ready"):
        st.session_state.unlocked = True
        st.rerun()

# 3. The Interactive Component
if st.session_state.unlocked:
    # Use a direct link to a heart or romantic image
    image_url = "https://s.yimg.com/ny/api/res/1.2/dP95AEjwx16sEweEB40KvA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyNDI7aD02OTg7Y2Y9d2VicA--/https://media.zenfs.com/en/abc_audio_244/9a019b7544bc10e08fd6c951fbe6d0ea"

    valentine_html = f"""
    <div id="container" style="height: 500px; width: 100%; position: relative; border: 2px dashed #ffb7c5; display: flex; flex-direction: column; justify-content: center; align-items: center; overflow: hidden; background-color: #fff0f0; border-radius: 20px; font-family: sans-serif;">
        
        <div id="dialog-label" style="margin-bottom: 20px; font-size: 1.5rem; font-weight: bold; color: #d63384; text-align: center; cursor: pointer; padding: 20px; border: 2px solid #ffb7c5; border-radius: 15px; background: #fff; z-index: 5;">
            Click to start...
        </div>

        <img id="secret-image" src="{image_url}" style="display: none; margin-bottom: 20px; border-radius: 15px; max-width: 80%; z-index: 1;">

        <div id="button-wrapper" style="display: none; gap: 20px; align-items: center; justify-content: center; width: 100%; margin-top: auto; padding-bottom: 40px;">
            <button id="stay-still" style="padding: 12px 25px; cursor: pointer; border-radius: 10px; border: 1px solid #ffb7c5; background: white; font-weight: bold; color: #d63384; z-index: 10;">
                YES!!!
            </button>

            <button id="move-me" style="padding: 12px 25px; cursor: pointer; border-radius: 10px; border: 1px solid #ccc; background: white; font-weight: bold; transition: all 0.05s ease; z-index: 20; position: relative;">
                no
            </button>
        </div>
    </div>

    <script>
        const runner = document.getElementById('move-me');
        const staticBtn = document.getElementById('stay-still');
        const wrapper = document.getElementById('button-wrapper');
        const label = document.getElementById('dialog-label');
        const container = document.getElementById('container');
        const secretImage = document.getElementById('secret-image');

        const messages = [
        "You know I had a whole plan to ask you something",
        "I was going to ask you-",
        "Will you be my Valentine this summer",
        "Don't go to Russia",
        "We'll have so much fun",
        "We can watch a movie",
        "Eat some sushi",
        "Completely alone",
        "Together"
    ];
        let currentMessageIndex = 0;

        label.addEventListener('click', function() {{
            if (currentMessageIndex < messages.length) {{
                label.innerText = messages[currentMessageIndex];
                currentMessageIndex++;
            }} else {{
                label.innerText = "Be My Valentine?";
                wrapper.style.display = "flex";
            }}
        }});

        staticBtn.addEventListener('click', function() {{
            label.style.display = "none";
            wrapper.style.display = "none";
            secretImage.style.display = "block";
        }});

        const moveRunner = () => {{
            if (runner.style.position !== 'absolute') {{
                const rect = runner.getBoundingClientRect();
                const containerRect = container.getBoundingClientRect();
                runner.style.top = (rect.top - containerRect.top) + 'px';
                runner.style.left = (rect.left - containerRect.left) + 'px';
                runner.style.position = 'absolute';
            }}
            
            const newTop = Math.random() * (container.offsetHeight - runner.offsetHeight - 80);
            const newLeft = Math.random() * (container.offsetWidth - runner.offsetWidth - 80);
            runner.style.top = Math.max(10, newTop) + 'px';
            runner.style.left = Math.max(10, newLeft) + 'px';
        }};

        container.addEventListener('mousemove', function(e) {{
            const rect = runner.getBoundingClientRect();
            const mouseX = e.clientX;
            const mouseY = e.clientY;
            const buttonCenterX = rect.left + rect.width / 2;
            const buttonCenterY = rect.top + rect.height / 2;
            const distance = Math.hypot(mouseX - buttonCenterX, mouseY - buttonCenterY);

            if (distance < 100) {{
                moveRunner();
            }}
        }});

        runner.addEventListener('mouseover', moveRunner);
    </script>
    """

    # We use height=550 to give the 500px container some breathing room
    components.html(valentine_html, height=550)

if st.button("Reset"):
    st.session_state.unlocked = False
    st.rerun()