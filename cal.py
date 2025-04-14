import streamlit as st

# Function to perform calculations
def calculate(expression):
    try:
        # Evaluate the expression
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

# Streamlit app layout
st.title("Simple Arithmetic Calculator")

# Input field for the expression
expression = st.text_input("Enter your expression:", "")

# Button to calculate the result
if st.button("Calculate"):
    result = calculate(expression)
    st.write("Result:", result)

# Displaying a simple calculator interface
st.subheader("Calculator Buttons")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("1"):
        expression += "1"
    if st.button("2"):
        expression += "2"
    if st.button("3"):
        expression += "3"
    if st.button("+"):
        expression += "+"

with col2:
    if st.button("4"):
        expression += "4"
    if st.button("5"):
        expression += "5"
    if st.button("6"):
        expression += "6"
    if st.button("-"):
        expression += "-"

with col3:
    if st.button("7"):
        expression += "7"
    if st.button("8"):
        expression += "8"
    if st.button("9"):
        expression += "9"
    if st.button("*"):
        expression += "*"

# Additional buttons
if st.button("0"):
    expression += "0"
if st.button("/"):
    expression += "/"
if st.button("C"):  # Clear button
    expression = ""
if st.button("="):  # Equals button
    result = calculate(expression)
    st.write("Result:", result)

# Display the current expression
st.write("Current Expression:", expression)
