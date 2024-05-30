import streamlit as st
from concrete_predict import *
from mortar_predict import *
from home_page import *

def main():
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Please select service:", ["Home", "Concrete Predict"])
    #page = st.sidebar.radio("Please select service:", ["Home", "Concrete Predict", "Mortar Predict"])

    if page == "Home":
        home_page()
    elif page == "Concrete Predict":
        concrete_predict_page()
    # elif page == "Mortar Predict":
    #     mortar_predict_page()

if __name__ == "__main__":
    main()
