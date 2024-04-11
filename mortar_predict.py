import streamlit as st
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle as pkl

# modelo = 'model_mortar.sav'
# escala = 'scale_mortar.sav'

# # Carregar o modelo salvo e o scaler
# with open(modelo, 'rb') as file:
#     modelo = pkl.load(file)

# with open(escala, 'rb') as file:
#     escala = pkl.load(file)

# Função para a página de previsão de argamassa
def mortar_predict_page():
    st.title("Under Construction...")
    
"""    st.title("Previsão de Argamassa")
    st.write("Esta é a página de previsão de argamassa.")
    st.write("Insira os dados necessários e clique em 'Prever' para ver a previsão.")
    
     # Pedir ao usuário os valores de entrada 
    ci = st.number_input("Cement consumption (kg/m³)")
    ca = st.number_input("Lime consumption (kg/m³)")
    na = st.number_input("Natural sand consumption (kg/m³)")
    ar = st.number_input("Artificial sand consumption (kg/m³)")
    rbmg = st.number_input("RBMG consumption (kg/m³)")
    adi = st.number_input("Superplasticizer consumption (L/m³)")
    cura = st.number_input("Curing time (days)")
    w_c = st.number_input("Water-cement ratio")
    if st.button("Calcular"):
        data = {
            'Ci': [ci],
            'Ca': [ca],
            'NA': [na],
            'AR': [ar],
            'RBMG': [rbmg],
            'Adi': [adi],
            'Cura': [cura],
            'w-c': [w_c]
        }"""
