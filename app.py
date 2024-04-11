import streamlit as st
from concrete_predict import *
from mortar_predict import *
from home_page import *

def main():
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            transition: margin-left .5s, box-shadow .5s;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.sidebar.title("Menu")
    menu_state = st.sidebar.checkbox("Menu", True)
    if menu_state:
        st.sidebar.write("Selecione uma página:")
        page = st.sidebar.radio("", ["Home", "Concrete Predict", "Mortar Predict"])
    else:
        page = st.sidebar.radio("Selecione uma página:", ["Home", "Concrete Predict", "Mortar Predict"])

    if page == "Home":
        home_page()
    elif page == "Concrete Predict":
        concrete_predict_page(modelo, escala)
    elif page == "Mortar Predict":
        mortar_predict_page()

if __name__ == "__main__":
    main()
