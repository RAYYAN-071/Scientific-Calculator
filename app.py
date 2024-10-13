import streamlit as st
import math

# Title and introduction
st.title("Scientific Calculator")
st.write("This is a simple scientific calculator implemented using Streamlit.")

# Select the operation
operation = st.selectbox("Choose an operation:", 
                         ["Add", "Subtract", "Multiply", "Divide", 
                          "Power", "Square Root", "Logarithm", 
                          "Sine", "Cosine", "Tangent"])

# Input fields
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)

elif operation == "Square Root":
    num1 = st.number_input("Enter a number:", value=0.0)

elif operation == "Logarithm":
    num1 = st.number_input("Enter a number:", value=0.0)
    base = st.number_input("Enter the base (default is 10):", value=10.0)

elif operation in ["Sine", "Cosine", "Tangent"]:
    angle = st.number_input("Enter the angle in degrees:", value=0.0)

# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Perform the calculation and display the result
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"Result: {num1} + {num2} = {result}")

    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"Result: {num1} - {num2} = {result}")

    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"Result: {num1} * {num2} = {result}")

    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"Result: {num1} / {num2} = {result}")

    elif operation == "Power":
        result = power(num1, num2)
        st.write(f"Result: {num1} ^ {num2} = {result}")

    elif operation == "Square Root":
        result = square_root(num1)
        st.write(f"Result: √{num1} = {result}")

    elif operation == "Logarithm":
        result = logarithm(num1, base)
        st.write(f"Result: log base {base} of {num1} = {result}")

    elif operation == "Sine":
        result = sine(angle)
        st.write(f"Result: sin({angle}°) = {result}")

    elif operation == "Cosine":
        result = cosine(angle)
        st.write(f"Result: cos({angle}°) = {result}")

    elif operation == "Tangent":
        result = tangent(angle)
        st.write(f"Result: tan({angle}°) = {result}")
