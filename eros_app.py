import streamlit as st
import json
import datetime
import re
import random

# --- Storage ---
STORAGE_FILE = "chat_storage.json"

def load_chats():
    try:
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    except:
        return {"Aidan": [], "Ellie": []}

def save_chats(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- Psychology Terms & Links ---
PSYCH_TERMS = {
    "avoidant attachment": "https://en.wikipedia.org/wiki/Attachment_theory#Avoidant_attachment",
    "anxious attachment": "https://en.wikipedia.org/wiki/Attachment_theory#Anxious_attachment",
    "secure attachment": "https://en.wikipedia.org/wiki/Attachment_theory#Secure_attachment",
    "trauma": "https://en.wikipedia.org/wiki/Psychological_trauma",
    "C-PTSD": "https://en.wikipedia.org/wiki/Complex_post-traumatic_stress_disorder",
    "narcissism": "https://en.wikipedia.org/wiki/Narcissism",
    "emotional regulation": "https://en.wikipedia.org/wiki/Emotion_regulation",
    "boundaries": "https://en.wikipedia.org/wiki/Personal_boundary",
    "codependency": "https://en.wikipedia.org/wiki/Codependency",
    "empathy": "https://en.wikipedia.org/wiki/Empathy",
    "gaslighting": "https://en.wikipedia.org/wiki/Gaslighting",
    "projection": "https://en.wikipedia.org/wiki/Psychological_projection",
    "defense mechanism": "https://en.wikipedia.org/wiki/Defense_mechanism",
    "stress": "https://en.wikipedia.org/wiki/Stress_(psychological)",
    "trust": "https://en.wikipedia.org/wiki/Trust_in_relationships",
    "intimacy": "https://en.wikipedia.org/wiki/Intimate_relationship",
    "attachment theory": "https://en.wikipedia.org/wiki/Attachment_theory",
    "resentment": "https://en.wikipedia.org/wiki/Resentment",
    "self-soothing": "https://en.wikipedia.org/wiki/Self-soothing",
    "love language": "https://en.wikipedia.org/wiki/Five_love_languages",
    "trauma bond": "https://en.wikipedia.org/wiki/Trauma-bonding",
    "reassurance": "https://en.wikipedia.org/wiki/Reassurance",
    "validation": "https://en.wikipedia.org/wiki/Validation_(psychology)",
    "mindfulness": "https://en.wikipedia.org/wiki/Mindfulness",
    "overwhelm": "https://en.wikipedia.org/wiki/Stress_(psychological)#Acute_stress",
    "attachment style": "https://en.wikipedia.org/wiki/Attachment_theory#Adult_attachment_styles",
    "emotional intelligence": "https://en.wikipedia.org/wiki/Emotional_intelligence",
    "self-awareness": "https://en.wikipedia.org/wiki/Self-awareness",
    "coping mechanism": "https://en.wikipedia.org/wiki/Coping_(psychology)",
    "regret": "https://en.wikipedia.org/wiki/Regret",
    "vulnerability": "https://en.wikipedia.org/wiki/Vulnerability_(emotional)",
    "anger": "https://en.wikipedia.org/wiki/Anger",
    "sadness": "https://en.wikipedia.org/wiki/Sadness",
    "communication": "https://en.wikipedia.org/wiki/Interpersonal_communication",
    "conflict resolution": "https://en.wikipedia.org/wiki/Conflict_resolution",
    "forgiveness": "https://en.wikipedia.org/wiki/Forgiveness",
    "resentment": "https://en.wikipedia.org/wiki/Resentment",
    "attachment injury": "https://en.wikipedia.org/wiki/Attachment_injury",
    "compassion": "https://en.wikipedia.org/wiki/Compassion",
    "negotiation": "https://en.wikipedia.org/wiki/Negotiation",
    "respect": "https://en.wikipedia.org/wiki/Respect",
    "emotional safety": "https://en.wikipedia.org/wiki/Emotional_safety",
    "dependability": "https://en.wikipedia.org/wiki/Trust_in_relationships",
    "jealousy": "https://en.wikipedia.org/wiki/Jealousy",
    "insecurity": "https://en.wikipedia.org/wiki/Insecurity",
    "attachment wound": "https://en.wikipedia.org/wiki/Attachment_theory",
    "projection": "https://en.wikipedia.org/wiki/Psychological_projection",
    "mutual vulnerability": "https://en.wikipedia.org/wiki/Vulnerability_(emotional)",
    "self-reflection": "https://en.wikipedia.org/wiki/Self-reflection",
    "introspection": "https://en.wikipedia.org/wiki/Introspection",
    "emotional mirroring": "https://en.wikipedia.org/wiki/Mirroring_(psychology)"
}

def link_terms(text):
    for term, url in PSYCH_TERMS.items():
        text = re.sub(rf"\b{re.escape(term)}\b", f"[{term}]({url})", text, flags=re.IGNORECASE)
    return text

# --- Streamlit UI ---
st.set_page_config(page_title="Eros", page_icon="❤️", layout="wide")

st.markdown(
    """
    <style>
    body {background-color: #001f3f; color: #ffa07a;}
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {background-color: #fbe6dc; color: #001f3f;}
    .chat-box {background-color: rgba(255, 160, 122, 0.1); padding:10px; margin-bottom:5px; border-radius:8px;}
    </style>
    """, unsafe_allow_html=True
)

# Introduction
st.markdown("### Hi, I'm **Eros**, your compassionate relationship companion 💖")
st.markdown("I listen carefully to both partners and provide neutral, empathetic guidance. Tell me what's on your mind:")

# Select user
name = st.selectbox("Who are you?", ["Ellie", "Aidan"])
message = st.text_area("Your message")

# Submit
if st.button("Send"):
    if message.strip():
        chats = load_chats()
        chats[name].append({"time": str(datetime.datetime.now()), "text": message})
        save_chats(chats)

        # Prepare neutral response
        other_name = "Aidan" if name == "Ellie" else "Ellie"
        other_msgs = chats[other_name]
        latest_other_msg = other_msgs[-1]["text"] if other_msgs else "[No input yet]"

        neutral_response = f"""
**Eros says:**  

Hello {name}, I hear you. Considering both your input and {other_name}'s perspective, here’s a warm, understanding reflection:

- Both of you have real feelings and valid perspectives.  
- It's normal to have different coping styles.  
- Focus on listening, validating, and gently exploring emotions.  
- Avoid assuming the other intends harm. Assume positive intent.  
- Ask questions like: 'Can you help me understand this feeling?' or 'What would help you feel safe right now?'
- Remember: vulnerability and empathy are strengths, not weaknesses.
"""
        neutral_response = link_terms(neutral_response)
        st.markdown(neutral_response)

# Display chat stream
st.markdown("---")
st.markdown("### Chat Stream (for context, private input only)")
chats = load_chats()
for user in ["Ellie", "Aidan"]:
    for c in chats[user]:
        time = c["time"].split(".")[0]
        st.markdown(f"<div class='chat-box'><b>{user}</b> ({time}): [message hidden]</div>", unsafe_allow_html=True)
