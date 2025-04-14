import streamlit as st
import re

# Set page config
st.set_page_config(page_title="Huzaifa's Calculator", layout="centered")

# Inject custom CSS
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #a8edea, #fed6e3);
        }
        .calculator-button {
            font-size: 30px;
            padding: 20px;
            width: 100%;
            background-color: #1f1f1f;
            color: white;
            border-radius: 10px;
        }
        .calculator-button:hover {
            background-color: #333;
        }
        .result-box {
            background-color: #111;
            color: #0f0;
            font-size: 30px;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style="text-align: center; color: #333333;">Hello, I am Huzaifa 👋<br>Welcome to my Advanced Calculator</h1>
""", unsafe_allow_html=True)

class Calculator:
    def __init__(self):
        self.expression = ""

    def perform_operation(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ValueError('Division by zero')
            return a / b
        elif operator == '%':
            return a % b
        elif operator == '//':
            return a // b

    def calculate(self, expression_input):
        try:
            expression_input = expression_input.replace('➕', '+').replace('➖', '-')\
                                             .replace('✖️', '*').replace('➗', '/')
            operators = ['+', '-', '*', '/', '%', '//']
            tokens = re.findall(r'\d+|[%s]' % re.escape(''.join(operators)), expression_input)
            if not tokens:
                return "Invalid input"
            result = int(tokens[0])
            i = 1
            while i < len(tokens):
                op = tokens[i]
                num = int(tokens[i+1])
                result = self.perform_operation(result, num, op)
                i += 2
            return result
        except Exception as e:
            return f"Error: {e}"


class CalculatorUI:
    def __init__(self, calculator):
        self.calculator = calculator
        if "expression" not in st.session_state:
            st.session_state.expression = ""
        if "result" not in st.session_state:
            st.session_state.result = None

    def handle_button_click(self, value):
        if value == "C":
            st.session_state.expression = ""
            st.session_state.result = None
        else:
            emoji_to_symbol = {'➕': '+', '➖': '-', '✖️': '*', '➗': '/'}
            real_value = emoji_to_symbol.get(value, value)
            st.session_state.expression += str(real_value)

    def display_calculator_buttons(self):
        layout = [
            ['7', '8', '9', '➕'],
            ['4', '5', '6', '➖'],
            ['1', '2', '3', '✖️'],
            ['0', '➗', 'C']
        ]
        for row in layout:
            cols = st.columns(len(row))
            for i, item in enumerate(row):
                if cols[i].button(item, key=f"btn_{item}", use_container_width=True):
                    self.handle_button_click(item)

    def display_input_and_result(self):
        expression_input = st.text_input("Enter your expression:", value=st.session_state.expression, key="expression_input")

        if expression_input != st.session_state.expression:
            st.session_state.expression = expression_input

        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("Calculate"):
                result = self.calculator.calculate(st.session_state.expression)
                st.session_state.result = result

        if st.session_state.result is not None:
            st.markdown(f"<div class='result-box'>Result: {st.session_state.result}</div>", unsafe_allow_html=True)

calculator = Calculator()
ui = CalculatorUI(calculator)
ui.display_calculator_buttons()
ui.display_input_and_result()
