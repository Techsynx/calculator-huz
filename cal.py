import streamlit as st

# Function to perform calculations
def calculate(expression):
    try:
        # Evaluate the expression
        result = eval(expression)
        return result
    except Exception:
        return "Error"

# Streamlit app layout
st.title("Simple Arithmetic Calculator")

# Input field for the expression
expression = st.text_input("Enter your expression:", "", key="input")

# Button to calculate the result
if st.button("Calculate", key="calculate"):
    result = calculate(expression)
    st.write("Result:", result)

# Displaying a simple calculator interface
st.subheader("Calculator Buttons")
col1, col2, col3 = st.columns(3)

# Function to create buttons
def create_button(label):
    return st.button(label, key=label)

# Create buttons for numbers and operations
with col1:
    for i in range(1, 4):
        if create_button(str(i)):
            expression += str(i)
            st.session_state.input = expression  # Update the input field

    if create_button("+"):
        expression += "+"
        st.session_state.input = expression  # Update the input field

with col2:
    for i in range(4, 7):
        if create_button(str(i)):
            expression += str(i)
            st.session_state.input = expression  # Update the input field

    if create_button("-"):
        expression += "-"
        st.session_state.input = expression  # Update the input field

with col3:
    for i in range(7, 10):
        if create_button(str(i)):
            expression += str(i)
            st.session_state.input = expression  # Update the input field

    if create_button("*"):
        expression += "*"
        st.session_state.input = expression  # Update the input field

# Additional buttons
if create_button("0"):
    expression += "0"
    st.session_state.input = expression  # Update the input field

if create_button("/"):
    expression += "/"
    st.session_state.input = expression  # Update the input field

if create_button("C"):  # Clear button
    expression = ""
    st.session_state.input = expression  # Update the input field

if create_button("="):  # Equals button
    result = calculate(expression)
    st.write("Result:", result)

# Display the current expression
st.write("Current Expression:", expression)
