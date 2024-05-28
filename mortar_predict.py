import streamlit as st
import pandas as pd
import pickle as pkl

modelo = 'model_mortar.sav'
escala = 'scale_mortar.sav'

# Carregar o modelo salvo e o scaler
with open(modelo, 'rb') as file:
    modelo = pkl.load(file)

with open(escala, 'rb') as file:
    escala = pkl.load(file)

# Função para a página de previsão de argamassa
def mortar_predict_page():
    st.title("Previsão de Argamassa")
    st.write("Esta é a página de previsão de argamassa.")
    st.write("Insira os dados necessários e clique em 'Prever' para ver a previsão.")
    
     # Pedir ao usuário os valores de entrada 
    ci = st.number_input("Cement consumption (kg/m³)")
    ca = st.number_input("Lime consumption (kg/m³)")
    na = st.number_input("Natural sand consumption (kg/m³)")
    ar = st.number_input("Artificial sand consumption (kg/m³)")
    rbmg = st.number_input("RBMG consumption (kg/m³)")
    adi = st.number_input("Superplasticizer consumption (kg/m³)")
    ag = st.number_input("Water consumption (kg/m³)")
    cura = st.number_input("Curing time (days)")
    
    if st.button("Calcular"):
        # Criar DataFrame com os dados fornecidos
        data = {
            'Ci': [ci],
            'Ca': [ca],
            'NA': [na],
            'AR': [ar],
            'RBMG': [rbmg],
            'Adi': [adi],
            'Ag': [ag],
            'Cura': [cura]
        }
        df = pd.DataFrame(data)

        # Adicionar coluna 'RCD' como a soma de 'AR' e 'RBMG'
        df['RCD'] = df['AR'] + df['RBMG']

        # Selecionar as colunas necessárias para predição
        df_predicao = df[['Ci', 'Ca', 'NA', 'Adi', 'Ag', 'Cura', 'RCD']]
        
        # Normalização dos dados com a escala
        for coluna in df_predicao.columns:
            if coluna in escala and coluna != 'Res':
                escala_mean = escala.loc['mean', coluna]
                escala_std = escala.loc['std', coluna]
                df_predicao[coluna] = df_predicao[coluna].apply(lambda x: (x - escala_mean) / escala_std)   

        # Predict do modelo
        previsao = modelo.predict(df_predicao)
        st.write(f"Previsão de Res: {previsao[0]}")
