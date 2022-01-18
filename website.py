from sympy import *
import pandas as pd
import streamlit as st


def set_page_configuration():  # sets page configuration
    st.set_page_config(page_title="Derivative Calc", page_icon=":sunglasses:")


def website_intro():  # prints the intro of the website
    st.title("Hi, Welcome to Derivative Calculator :smile:")
    st.write("Please follow this instructions when entering your function:")

    # instructions table
    rules = {"Operations and Symbols": ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Power', '\u03C0', 'e', 'e^x'], "How to write": ['+', '-', '*', '/', '** or ^', 'pi', 'exp(1)', 'exp(x)']}
    rules_df = pd.DataFrame(rules)
    st.table(rules_df)  # print the instructions table
    st.write("* Use parentheses to obtain order of operations if needed.")


def get_function():  # get the function to derive from the user
    return st.text_input("Please enter your function:", )  #


def get_derivative_variable():  # get the variable to derive with respect to
    return st.text_input("Derive with respect to:", )


def compute_and_print_derivative(user_func, dev_var):
    derivative = None
    try:  # if a user inserts ax instead of a*x an exception will be raised
        derivative = diff(user_func, dev_var)
    except Exception as E:
        st.error("Wrong input. Please enter your function again and mind the instruction table above.")
        st.stop()
    st.write("The derivative is:", derivative)
    return derivative


def get_free_symbols(derivative):  # returns the free variables in the derivative
    return exp(derivative).free_symbols


def get_point(free_symbols):  # get the point input from the user - value for every free symbol found in the derivative
    st.write("Now, please enter your point:")
    symbols_vals = {}
    for s in free_symbols:
        symbols_vals[s] = st.text_input(str(s), )
    return symbols_vals


def run_app():
    set_page_configuration()
    with st.container():
        website_intro()
        user_func = get_function()
        if user_func:  # wait until user_func is entered
            dev_var = get_derivative_variable()
            if dev_var:  # wait until dev_var is entered
                derivative = compute_and_print_derivative(user_func, dev_var)
                free_symbols = get_free_symbols(derivative)
                if len(free_symbols) > 0:  # if there are free symbols in the derivative we need to get the point values
                    st.write("Identified free symbols", free_symbols)
                    symbols_vals = get_point(free_symbols)
                    if len(symbols_vals) == len(free_symbols):
                        st.write("The derivative in this point is:", derivative.subs(symbols_vals))
                else:
                    st.write("No free symbols identified, no need to enter point.")


if __name__ == '__main__':
    run_app()
