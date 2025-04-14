import streamlit as st
import re

# --- Custom Styles ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%) !important;
        }

        button[kind="secondary"] {
            font-size: 24px !important;
            height: 60px !important;
            width: 100% !important;
            border-radius: 12px !important;
            margin: 2px 0 !important;
        }

        .highlight-btn {
            background-color: #FFD700 !important;
            color: black !important;
        }

        .result {
            font-size: 40px;
            font-weight: bold;
            color: #000000;
            padding-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Calculator Logic ---
class Calculator:
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

# --- Calculator UI ---
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

                with cols[i]:
                    if st.button(key, key=f"btn_{key}"):
                        self.handle_button_click(key)

    def display_input_and_result(self):
        expression_input = st.text_input("Enter your expression:", 
                                         value=st.session_state.expression, 
                                         key="expression_input")

        # Sync keyboard typed key for highlight simulation
        if expression_input:
            last_char = expression_input[-1]
            if last_char.isalnum() or last_char in ['+', '-', '*', '/']:
                st.session_state.last_key = last_char
            st.session_state.expression = expression_input

        # Calculate manually or on Enter
        if st.button("Calculate", key="calculate_btn"):
            result = self.calculator.calculate(expression_input)
            st.session_state.calculated_result = result

        if st.session_state.calculated_result != "":
            st.markdown(f"<div class='result'>Result: {st.session_state.calculated_result}</div>", unsafe_allow_html=True)


# --- Run App ---
calculator = Calculator()
calculator_ui = CalculatorUI(calculator)
calculator_ui.display_calculator_buttons()
calculator_ui.display_input_and_result()
