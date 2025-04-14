import streamlit as st

# Set page config
st.set_page_config(page_title="Basic Calculator", layout="centered")

# App title
st.title("Simple Calculator")

# Initialize expression in session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Handle button press
def press(key):
    if key == "C":
        st.session_state.expression = ""
    elif key == "=":
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += key

# Keyboard input
input_text = st.text_input("Enter expression:", value=st.session_state.expression, key="input")
st.session_state.expression = input_text  # Sync typed input

# Buttons layout
button_rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

# Display buttons (large and spaced)
for row in button_rows:
    cols = st.columns(len(row))
    for i, key in enumerate(row):
        if cols[i].button(key, use_container_width=True):
            press(key)

# Display result
st.subheader("Output:")
st.code(st.session_state.expression)
