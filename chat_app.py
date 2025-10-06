import streamlit as st

st.title("Relationship Helper Bot")
st.write("Each of you can write your thoughts below. The bot will give a neutral, palatable response considering both inputs. You won’t see each other’s messages.")

# Session state storage for inputs
if "user1_input" not in st.session_state:
    st.session_state.user1_input = ""
if "user2_input" not in st.session_state:
    st.session_state.user2_input = ""

# Choose your user
user_choice = st.radio("Who are you?", ["User 1", "User 2"])

# Input box for current user
if user_choice == "User 1":
    st.session_state.user1_input = st.text_area("Write your thoughts here:", value=st.session_state.user1_input, key="input1")
else:
    st.session_state.user2_input = st.text_area("Write your thoughts here:", value=st.session_state.user2_input, key="input2")

# Button to generate neutral response
if st.button("Generate Response"):
    u1 = st.session_state.user1_input or "[No input]"
    u2 = st.session_state.user2_input or "[No input]"

    response = f"""
    Therapist-style neutral response:

    Considering both users' inputs:

    - User 1 wrote: {u1}
    - User 2 wrote: {u2}

            Therapist-style advice:
        - Both of you have valid feelings and perspectives.
        - It's important to recognize each person's coping style.
        - Ask questions to help users understand themselves better.
        - Encourage users to ask their partner questions by giving prompts.
        - Use psychology-based information to describe feelings and actions.
        - Focus on listening and validating each other before reacting.
        - Avoid interpreting the other's actions as attacks; assume positive intent.
    """
    st.success(response)
