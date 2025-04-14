import streamlit as st
import re

# Custom CSS to style the app
st.markdown("""
    <style>
        .stApp {    
            background-color: #ffffff;
            background-image: linear-gradient(315deg, #ffffff 0%, #335c81 74%);
        }
        .button {
            font-size: 24px;    /* Bigger font size */
            padding: 20px 30px; /* Bigger padding */
            width: 100%;        /* Full width */
        }
        .result {
            font-size: 50px;
            font-weight: bold;
            color: #000000;
        }
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown("""
    <h1 style="font-size: 25px; font-weight: bold; color: #C0C0C0;">
        Hello, I am Huzaifa, welcome to my Advanced Calculator
    </h1>
""", unsafe_allow_html=True)


# Logic class
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


# UI class
class CalculatorUI:
    def __init__(self, calculator):
        self.calculator = calculator
        if "expression" not in st.session_state:
            st.session_state.expression = ""

    def handle_button_click(self, value):
        if value == "C":
            st.session_state.expression = ""
        else:
            st.session_state.expression += str(value)

    def display_calculator_buttons(self):
        cols = st.columns(4)
        col_list = [
            [7, 8, 9, '+'], 
            [4, 5, 6, '-'],  
            [1, 2, 3, '*'],  
            [0, '/', 'C', '']  
        ]
        for row in col_list:
            for i, button in enumerate(row):
                if button == '':
                    continue
                button = str(button)
                display_text = button
                if button == '+':
                    display_text = 'Add'
                elif button == '-':
                    display_text = 'Sub'
                elif button == '*':
                    display_text = 'Mul'
                with cols[i]:
                    if st.button(display_text, key=display_text):
                        if button == 'Add':
                            self.handle_button_click('+')
                        elif button == 'Sub':
                            self.handle_button_click('-')
                        elif button == 'Mul':
                            self.handle_button_click('*')
                        else:
                            self.handle_button_click(str(button))

    def display_result(self):
        expression_input = st.text_input("Enter the expression and press Enter:", 
                                         value=st.session_state.expression, 
                                         key="expression_input")

        # This will auto calculate when you press Enter
        if expression_input:
            result = self.calculator.calculate(expression_input)
            st.markdown(f"<div class='result'>Result of expression: {result}</div>", unsafe_allow_html=True)


# Initialize and run app
calculator = Calculator()
calculator_ui = CalculatorUI(calculator)
calculator_ui.display_calculator_buttons()
calculator_ui.display_result()
