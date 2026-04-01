import streamlit as st

st.title("Division Calculator")

col1, col2 = st.columns(2)
with col1:
    num1 = st.text_input("First number (dividend):")
with col2:
    num2 = st.text_input("Second number (divisor):")

if st.button("Divide"):
    try:
        n1 = float(num1)
        n2 = float(num2)
        result = n1 / n2
    except ValueError:
        st.error("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        st.error("Cannot divide by zero!")
    else:
        st.success(f"Division successful. Result: {result}")