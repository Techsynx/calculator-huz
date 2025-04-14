import streamlit as st

# Step 1: Page Config (Set title and layout)
st.set_page_config(page_title="Simple Calculator", layout="centered")

# Step 2: Title of the App
st.title("🧮 Streamlit Calculator")

# Step 3: Create session state to store input
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Step 4: Function to handle button press
def press(button_text):
    if button_text == "C":
        st.session_state.expression = ""
    elif button_text == "=":
        try:
            # Evaluate the expression safely
            st.session_state.expression = str(eval(st.session_state.expression))
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += button_text

# Step 5: Text input for keyboard typing
keyboard_input = st.text_input("Type your expression or use the buttons below:", 
                               value=st.session_state.expression,
                               key="input_box")

# Sync typed input with session state
st.session_state.expression = keyboard_input

# Step 6: Display calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

# Step 7: Show buttons as columns
for row in buttons:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        if cols[i].button(button):
            press(button)

# Step 8: Show result/output
st.subheader("Result:")
st.code(st.session_state.expression)
