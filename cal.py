import streamlit as st

# 1. Page configuration and title
st.set_page_config(page_title="Basic Calculator", layout="centered")
st.title("Simple Calculator")

# 2. Initialize session state variables for the typed expression and result
if 'typed_expr' not in st.session_state:
    st.session_state.typed_expr = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# 3. Define function for processing button clicks
def press(key):
    if key == "C":
        st.session_state.typed_expr = ""
        st.session_state.result = ""
    elif key == "=":
        try:
            st.session_state.result = str(eval(st.session_state.typed_expr))
        except Exception:
            st.session_state.result = "Error"
    else:
        st.session_state.typed_expr += key

# 4. Define callback to evaluate the expression when Enter is pressed
def evaluate_input():
    try:
        st.session_state.result = str(eval(st.session_state.typed_expr))
    except Exception:
        st.session_state.result = "Error"

# 5. Inject custom CSS to style operator buttons differently  
#    (This CSS targets the fourth button in rows that have 4 buttons and the only button row)
st.markdown(
    """
    <style>
    /* For rows with 4 buttons, style the 4th button (operators) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(4) button {
         background-color: #FF5733 !important;
         color: white !important;
         font-weight: bold;
    }
    /* For a full-width row (like the "=" row) */
    div[data-testid="stHorizontalBlock"]:last-child button {
         background-color: #FF5733 !important;
         color: white !important;
         font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 6. Text input for keyboard typing.
# When the user presses Enter, the on_change callback evaluates the expression.
st.text_input("Enter expression (Press Enter to calculate):", 
              value=st.session_state.typed_expr, 
              key="input", 
              on_change=evaluate_input)

# 7. Define the calculator layout (rows of buttons)  
button_rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

# 8. Display the buttons with larger clickable areas
for row in button_rows:
    cols = st.columns(len(row))  # Create a row with as many columns as buttons
    for i, key in enumerate(row):
        if cols[i].button(key, use_container_width=True):
            press(key)

# 9. Display the result only if it has been calculated and is different from the typed expression
st.subheader("Output:")
if st.session_state.result and st.session_state.result != st.session_state.typed_expr:
    st.code(st.session_state.result)
