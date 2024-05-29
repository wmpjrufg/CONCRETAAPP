import streamlit as st
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle as pkl

modelo = 'model_concrete.sav'
escala = 'scale_concrete.sav'

# Carregar o modelo salvo e o scaler
with open(modelo, 'rb') as file:
    modelo = pkl.load(file)

with open(escala, 'rb') as file:
    escala = pkl.load(file)

# Função para a página de previsão de concreto
def concrete_predict_page():
    st.title("Previsão de Concreto")
    st.write("Esta é a página de previsão de concreto.")
    st.write("Insira os dados necessários e clique em 'Prever' para ver a previsão.")
    

    # Pedir ao usuário os valores de entrada no streamlit
    c = st.number_input("Cemeter consumption (kg/m³)")
    sp = st.number_input("Superplasticizer consumption(kg/m³)")
    cag = st.number_input("Coarse agregate consumption(kg/m³)")
    fag = st.number_input("Fine aggregate consumption (kg/m³)")
    t = st.number_input("Curring time (days)")
    w_c_ratio = st.number_input("Water-Cement ratio")
    add = st.number_input("Additions (kg/m³)")
    if st.button("Calcular"):
        data = {
            'c': [c],
            'sp': [sp],
            'cag': [cag],
            'fag': [fag],
            't': [t],
            'w-c ratio': [w_c_ratio],
            'add': [add]
        }

        # Normalização dos dados com a escala
        x_normalizado = pd.DataFrame(data).copy()
        for coluna in x_normalizado.columns:
            if coluna in escala and coluna != 'f_ck':
                escala_mean = escala.loc['mean', coluna]
                escala_std = escala.loc['std', coluna]
                x_normalizado[coluna] = x_normalizado[coluna].apply(lambda x: (x - escala_mean) / escala_std) 

        # Predict do modelo
        previsao = modelo[0].predict(x_normalizado)
        st.write(f"Previsão de f_ck: {previsao[0]}")