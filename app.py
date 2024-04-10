from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle as pkl 
import streamlit as st

SCALE = 'scale.sav'
MODEL = 'model.sav'

# Carregar o modelo salvo e o scaler
with open('model.sav', 'rb') as file:
    modelo = pkl.load(file)

with open('scale.sav', 'rb') as file:
    escala = pkl.load(file)

# Pedir ao usuário os valores de entrada no streamlit
st.title("Previsão de f_ck")
st.write("Insira os valores de entrada para prever o f_ck")

# Pedir ao usuário os valores de entrada no streamlit
c = st.number_input("c")
sp = st.number_input("sp")
cag = st.number_input("cag")
fag = st.number_input("fag")
t = st.number_input("t")
w_c_ratio = st.number_input("w-c ratio")
add = st.number_input("add")

# Crie um botão para calcular
if st.button("Calcular"):
    # Crie o DataFrame com os dados inseridos pelo usuário
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
        if coluna != 'f_ck':
            escala_mean = escala.loc['mean', coluna]
            escala_std = escala.loc['std', coluna]
            x_normalizado[coluna] = (x_normalizado[coluna] - escala_mean) / escala_std

    # Predict do modelo
    previsao = modelo[0].predict(x_normalizado)
    st.write(f"Previsão de f_ck: {previsao[0]}")
