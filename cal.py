import streamlit as st

# 1) Set up page configuration
st.set_page_config(page_title="Basic Calculator", layout="centered")

# 2) Title
st.title("Simple Calculator")

# 3) Session state variables
if 'typed_expr' not in st.session_state:
    st.session_state.typed_expr = ""  # Stores what user types or clicks
if 'result' not in st.session_state:
    st.session_state.result = ""      # Stores the evaluated result

# 4) Function to handle button clicks
def press(key):
    if key == "C":
        # Clear both the typed expression and the result
        st.session_state.typed_expr = ""
        st.session_state.result = ""
    elif key == "=":
        try:
            # Evaluate the typed expression
            st.session_state.result = str(eval(st.session_state.typed_expr))
        except:
            # If there's an error, display "Error"
            st.session_state.result = "Error"
    else:
        # Append clicked key to the typed expression
        st.session_state.typed_expr += key

# 5) Text input: for user typing with the keyboard
typed_input = st.text_input("Enter expression:", value=st.session_state.typed_expr)
st.session_state.typed_expr = typed_input

# 6) Buttons (larger)
button_rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row in button_rows:
    cols = st.columns(len(row))  # Create columns for each row
    for i, key in enumerate(row):
        # 'use_container_width=True' makes the button full column width (bigger)
        if cols[i].button(key, use_container_width=True):
            press(key)

# 7) Display the result ONLY if '=' has been pressed
st.subheader("Output:")
if st.session_state.result:
    st.code(st.session_state.result)
