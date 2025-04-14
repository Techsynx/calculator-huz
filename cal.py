import streamlit as st
from streamlit.components.v1 import html

# Initialize session state
if 'expression' not in st.session_state:
    st.session_state.expression = ''
if 'result' not in st.session_state:
    st.session_state.result = ''

def calculate():
    try:
        st.session_state.result = eval(st.session_state.expression)
    except:
        st.session_state.result = 'Error'

def clear():
    st.session_state.expression = ''
    st.session_state.result = ''

# JavaScript for auto-focus and keyboard input
keyboard_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const handleKeyPress = (event) => {
        const key = event.key;
        const validKeys = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','.','Enter','Backspace'];
        
        if (validKeys.includes(key)) {
            if (key === 'Enter') {
                parent.document.querySelector('input[type="text"]').value += '';
                parent.document.querySelector('input[type="text"]').dispatchEvent(new Event('input'));
                parent.window.top.document.querySelector('button[kind="secondary"]').click();
            } else if (key === 'Backspace') {
                parent.document.querySelector('input[type="text"]').value = 
                    parent.document.querySelector('input[type="text"]').value.slice(0, -1);
                parent.document.querySelector('input[type="text"]').dispatchEvent(new Event('input'));
            } else {
                parent.document.querySelector('input[type="text"]').value += key;
                parent.document.querySelector('input[type="text"]').dispatchEvent(new Event('input'));
            }
        }
    };

    // Auto-focus on page load
    parent.document.querySelector('input[type="text"]').focus();
    
    // Add event listener for key presses
    document.addEventListener('keydown', handleKeyPress);
});
</script>
"""

# Inject keyboard handling JavaScript
html(keyboard_js, height=0)

# Calculator UI
st.title("Calculator")

# Input field
expression = st.text_input("", value=st.session_state.expression, key='expression')

# Buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("7", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '7'))
    st.button("4", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '4'))
    st.button("1", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '1'))
    st.button(".", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '.'))

with col2:
    st.button("8", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '8'))
    st.button("5", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '5'))
    st.button("2", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '2'))
    st.button("0", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '0'))

with col3:
    st.button("9", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '9'))
    st.button("6", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '6'))
    st.button("3", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '3'))
    st.button("=", on_click=calculate, type='primary')

with col4:
    st.button("÷", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '/'))
    st.button("×", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '*'))
    st.button("-", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '-'))
    st.button("+", on_click=lambda: st.session_state.update(expression=st.session_state.expression + '+'))

st.button("Clear", on_click=clear)

# Display result
if st.session_state.result != '':
    st.subheader(f"Result: {st.session_state.result}")
