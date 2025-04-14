import streamlit as st
import math

# Memory for storing values
memory = 0

# Function to perform the calculation
def calculate(operation, num1, num2=None):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == 'Power':
        return math.pow(num1, num2)
    elif operation == 'Square Root':
        return math.sqrt(num1)
    elif operation == 'Logarithm':
        return math.log10(num1)
    elif operation == 'Natural Log':
        return math.log(num1)
    elif operation == 'Sine':
        return math.sin(math.radians(num1))
    elif operation == 'Cosine':
        return math.cos(math.radians(num1))
    elif operation == 'Tangent':
        return math.tan(math.radians(num1))
    elif operation == 'Inverse Sine':
        return math.degrees(math.asin(num1))
    elif operation == 'Inverse Cosine':
        return math.degrees(math.acos(num1))
    elif operation == 'Inverse Tangent':
        return math.degrees(math.atan(num1))
    elif operation == 'Hyperbolic Sine':
        return math.sinh(num1)
    elif operation == 'Hyperbolic Cosine':
        return math.cosh(num1)
    elif operation == 'Hyperbolic Tangent':
        return math.tanh(num1)
    elif operation == 'Factorial':
        return math.factorial(int(num1))
    elif operation == 'Modulus':
        return num1 % num2
    else:
        return 'Invalid operation'

# Streamlit UI
st.title('Advanced Calculator')

# Theme options
theme = st.selectbox('Select Theme', ('Light', 'Dark'))
if theme == 'Dark':
    st.markdown(
        """
        <style>
        .reportview-container {
            background: #333333;
            color: #ffffff;
        }
        .sidebar .sidebar-content {
            background: #444444;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Using columns for better layout
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input('Enter the first number', value=0.0, format="%.2f")

# Selection of operation
operation = st.selectbox('Select an operation', (
    'Add', 'Subtract', 'Multiply', 'Divide', 'Power', 'Square Root', 'Logarithm',
    'Natural Log', 'Sine', 'Cosine', 'Tangent', 'Inverse Sine', 'Inverse Cosine', 
    'Inverse Tangent', 'Hyperbolic Sine', 'Hyperbolic Cosine', 'Hyperbolic Tangent', 
    'Factorial', 'Modulus'
))

# Display second number input only if the operation requires two numbers
num2 = None
if operation not in ['Square Root', 'Sine', 'Cosine', 'Tangent', 'Inverse Sine', 'Inverse Cosine', 'Inverse Tangent', 'Hyperbolic Sine', 'Hyperbolic Cosine', 'Hyperbolic Tangent', 'Factorial']:
    with col2:
        num2 = st.number_input('Enter the second number', value=0.0, format="%.2f")

# Memory functions
st.sidebar.header("Memory Functions")
if st.sidebar.button('M+'):
    memory += num1
elif st.sidebar.button('M-'):
    memory -= num1
elif st.sidebar.button('MR'):
    st.sidebar.write(f'Recalled memory: {memory}')
elif st.sidebar.button('MC'):
    memory = 0

# Perform the calculation
if st.button('Calculate'):
    result = calculate(operation, num1, num2)
    st.markdown(f'<h3 style="color:{"white" if theme == "Dark" else "blue"};">The result is: {result}</h3>', unsafe_allow_html=True)

# Display recent calculations (for simplicity, store the last calculation)
if 'history' not in st.session_state:
    st.session_state['history'] = []

if st.button('Show History'):
    st.write(st.session_state['history'])

# Store the latest calculation in history
if 'result' in locals() and result not in ['Invalid operation', 'Error: Division by zero']:
    st.session_state['history'].append(f'{num1} {operation} {num2 if num2 is not None else ""} = {result}')

# Option to switch between degrees and radians for trigonometric calculations
st.sidebar.header("Settings")
angle_unit = st.sidebar.radio('Angle Unit', ('Degrees', 'Radians'))

# Function to convert angles
def to_radians(angle, unit):
    if unit == 'Degrees':
        return math.radians(angle)
    return angle

# Update the trigonometric functions to respect the angle unit setting
if operation in ['Sine', 'Cosine', 'Tangent']:
    num1 = to_radians(num1, angle_unit)
