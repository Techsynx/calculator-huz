import streamlit as st
import re

# --- Style ---
st.markdown("""
    <style>
        .stApp {
            background-color: #85FFBD;
            background-image: linear-gradient(315deg, #FFFB7D 0%, #335c81 74%);
        }
        .calc-button {
            font-size: 22px;
            padding: 20px;
            width: 100%;
            border-radius: 10px;
            margin: 0px !important;
        }
        .highlight {
            background-color: #ffdd57 !important;
            color: black !important;
        }
        .result {
            font-size: 40px;
            font-weight: bold;
            color: #000000;
            padding-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Calculator Logic ---
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
                raise ValueError('Error (division by zero)')
            return a / b
        elif operator == '%':
            return a % b
        elif operator == '//':
            return a // b

    def calculate(self, expression_input):
        try:
            operators = ['+', '-', '*', '/', '%', '//']
            split_result = [x.strip() for x in re.split(r'[\+\-\*/%\s//]+', expression_input)]
            extracted_operators = [op for op in expression_input if op in operators]
            split_result = [int(x) for x in split_result]
            result = split_result[0]
            for i, operator in enumerate(extracted_operators):
                result = self.perform_operation(result, split_result[i + 1], operator)
            return result
        except ValueError as ve:
            return f"Error: {ve}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

# --- UI Class ---
class CalculatorUI:
    def __init__(self, calculator):
        self.calculator = calculator
        if "expression" not in st.session_state:
            st.session_state.expression = ""
        if "last_key" not in st.session_state:
            st.session_state.last_key = ""
        if "calculated_result" not in st.session_state:
            st.session_state.calculated_result = ""

    def handle_button_click(self, value):
        if value == "C":
            st.session_state.expression = ""
            st.session_state.calculated_result = ""
        else:
            st.session_state.expression += str(value)
        st.session_state.last_key = str(value)

    def display_calculator_buttons(self):
        rows = [
            ['7', '8', '9', '+'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '*'],
            ['0', '/', 'C', '']
        ]

        for row in rows:
            cols = st.columns(4, gap="small")
            for i, key in enumerate(row):
                if key == '':
                    continue
                btn_class = "calc-button"
                if st.session_state.last_key == key:
                    btn_class += " highlight"

                with cols[i]:
                    if st.button(f"<span class='{btn_class}'>{key}</span>", key=key, use_container_width=True, unsafe_allow_html=True):
                        self.handle_button_click(key)

    def display_input_and_result(self):
        expression_input = st.text_input("Enter your expression:", 
                                         value=st.session_state.expression, 
                                         key="expression_input")

        # Keyboard typing sets last key for highlight effect
        if expression_input:
            last_char = expression_input[-1]
            if last_char.isalnum() or last_char in ['+', '-', '*', '/']:
                st.session_state.last_key = last_char
            st.session_state.expression = expression_input

        # Calculate on Enter or Button
        calculate_clicked = st.button("Calculate")
        if calculate_clicked or expression_input:
            result = self.calculator.calculate(expression_input)
            st.session_state.calculated_result = result

        # Display result
        if st.session_state.calculated_result != "":
            st.markdown(f"<div class='result'>Result: {st.session_state.calculated_result}</div>", unsafe_allow_html=True)

# --- Run App ---
calculator = Calculator()
calculator_ui = CalculatorUI(calculator)
calculator_ui.display_calculator_buttons()
calculator_ui.display_input_and_result()
