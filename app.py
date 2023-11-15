import numpy as np
import pandas as pd
import streamlit as st
from scipy.stats import t
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from st_on_hover_tabs import on_hover_tabs
import pickle


SCALE = 'scale.sav'
MODEL = 'melhor_modelo.pkl'

def MODEL_CONCRETA_MORTAR(edited_df,scale,model):

    # # Entradas informadas pelo usuário
    # VAR1 = float(input("Enter the value of cement consumption (kg/m³): "))
    # VAR2 = float(input("Enter the value of superplasticizer consumption (kg/m³): "))
    # VAR3 = float(input("Enter the value of coarse aggregate consumption (kg/m³): "))
    # VAR4 = float(input("Enter the value of fine aggregate consumption (kg/m³): "))
    # VAR5 = float(input("Enter the value of curing time (days): "))
    # VAR6 = float(input("Enter the value of water-cement ratio: "))
    # VAR7 = float(input("Enter the value of filler materials consumption (kg/m³): "))
    # print("\n \n")

    # # Convertendo os valores em um dataframe Python
    # DOSAGEM = [[VAR1, VAR2, VAR3, VAR4, VAR5, VAR6, VAR7]]
    # DOSAGEM = [[222.36, 4.46, 967.08, 870.32, 3, 0.85, 96.67]]

    columns = ["FCK PREDICT"]
    results = pd.DataFrame(columns=columns)

    with open(model, 'rb') as file:
                modelo_carregado = pickle.load(file)

    with open(scale, 'rb') as file:
                ESCALAS = pickle.load(file)

    

    
    DOSAGEM = [list(edited_df.iloc[0])]
    print(DOSAGEM)

    DF_PREDICAO = pd.DataFrame(
        DOSAGEM, columns=["Ci", "Ca","NA","AR","RBMG","Adi","Cura","w-c"]
    )

    for COL in DF_PREDICAO:
        if COL != 'Res':
            DF_PREDICAO[COL] = DF_PREDICAO[COL].apply(lambda x: (x - ESCALAS[COL][0]) / ESCALAS[COL][1])
    
    RESULTS =  np.round(modelo_carregado.predict(DF_PREDICAO),2)
    
        # Relatório
        #results = modelo_carregado.predict(DOSAGEM)
    results.loc[len(results)] = [
            f"{RESULTS} MPa",
        ]
    
    results.set_index("FCK PREDICT")

    return results


# ----------------------------------------------------------------------------------------------------------------#
def standard(data):
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    return data


def load_excel(key, help):
    df = st.file_uploader(key, type="xlsx", help=help, key=key)
    return df


st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("Logotipo Tecnologia e Gaming Moderno Verde.png")
with col3:
    st.image(
        "data:image/png;base64,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"
    )
# st.title("Concreta")
st.markdown("<style>" + open("./style.css").read() + "</style>", unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(
        tabName=["Mortar Compressive strenght", "Desirability", "About"],
        iconName=["dashboard", "money", "economy"],
        default_choice=0,
    )

if tabs == "Mortar Compressive strenght":
    
    st.markdown(
        "Hello, I am Concreta, the first Brazilian AI built to determine the mortar strength (fck) based on dosage data. I am one of the creations of the GPEE (Research and Studies Group in Civil Engineering) of UFCAT, and I am here to help you, Civil Engineer and engineering student who wants to determine the properties of concrete.")
    st.header("Inputs")
    st.markdown(
        "Please, fill in the table with the mixture parameters. For your consideration, here is an example:"
    )
    st.markdown(
        """                                             
        • Cement consumption (kg/m³): 384.3\n
        • Lime consumption (kg/m³) : 531.0\n 
        • Natural sand consumption (kg/m³) : 2350.0\n 
        • Artificial sand consumption (kg/m³) : 0.0\n
        • RBMG consumption (kg/m³) : 0.0\n
        • Superplasticizer consumption (L/m³) : 0.0\n
        • Curing time (days) : 7\n
        • Water-cement ratio : 1.686183\n"""
    )
    pl = st.radio('\n What is your platform?', ('PC', 'mobile'))

    if pl == 'PC':
        df = pd.DataFrame(
            [
                {   
                    "Sample": 0.0,
                    "Cement consumption (kg/m³)": 0.0,
                },
            ]
        ).set_index("Sample")

        df2 = pd.DataFrame(
            [
                {
                    "Sample": 0.0,
                    "Lime consumption (kg/m³)": 0.0,
                },
            ]
        ).set_index("Sample")

        df3 = pd.DataFrame(
            [
                {
                    "Sample": 0.0,
                    "Natural sand consumption (kg/m³)": 0.0,
                },
            ]
        ).set_index("Sample")
        

        df4 = pd.DataFrame(
        [
            {
                "Sample": 0.0,
                "Artificial sand consumption (kg/m³)": 0.0,
            },
        ]
        ).set_index("Sample")

        df5 = pd.DataFrame(
        [
            {
                "Sample": 0.0,
                "RBMG consumption (kg/m³)": 0.0,
            },
        ]
        ).set_index("Sample")

        df6 = pd.DataFrame(
        [
            {
                "Sample": 0.0,
                "Superplasticizer consumption (L/m³)": 0.0,
            },
        ]
        ).set_index("Sample")

        df7 = pd.DataFrame(
        [
            {
                "Sample": 0.0,
                "Curing time (days)": 0.0,
            },
        ]
        ).set_index("Sample")

        df8 = pd.DataFrame(
        [
            {
                "Sample": 0.0,
                "Water-cement ratio": 0.0,
            },
        ]
        ).set_index("Sample")

        col1, col2, col3 = st.columns([4,1,1])
        with col1:
            edited_df = st.data_editor(df,use_container_width=True)
            edited_df2 = st.data_editor(df2,use_container_width=True)
            edited_df3 = st.data_editor(df3,use_container_width=True)
            edited_df4 = st.data_editor(df4,use_container_width=True)
            edited_df5 = st.data_editor(df5,use_container_width=True)
            edited_df6 = st.data_editor(df6,use_container_width=True)
            edited_df7 = st.data_editor(df7,use_container_width=True)
            edited_df8 = st.data_editor(df8,use_container_width=True)


        edited_df = edited_df.join(edited_df2)
        edited_df = edited_df.join(edited_df3)
        edited_df = edited_df.join(edited_df4)
        edited_df = edited_df.join(edited_df5)
        edited_df = edited_df.join(edited_df6)
        edited_df = edited_df.join(edited_df7)
        edited_df = edited_df.join(edited_df8)
        edited_df = edited_df.reset_index()

        del edited_df['Sample']
    else: 
            st.markdown(
            "\n"
            )

            edited_df = pd.DataFrame(
            [
                {
                    "Cement consumption (kg/m³)": st.slider('Cement consumption (kg/m³)',136.0,2617.0,136.0,0.01),
                    "Lime consumption (kg/m³)": st.slider("Lime consumption (kg/m³)",0.0,1339.0,0.0,0.01),
                    "Natural sand consumption (kg/m³)": st.slider("Natural sand consumption (kg/m³)",0.0,5273.0,0.0,0.01),
                    "Artificial sand consumption (kg/m³)": st.slider("Artificial sand consumption (kg/m³)",0.0,2250.0,0.0,0.01),
                    "RBMG consumption (kg/m³)": st.slider("RBMG consumption (kg/m³)",0.0,353.0,0.0,0.01),
                    "Superplasticizer consumption (L/m³)": st.slider("Superplasticizer consumption (L/m³)",0.0,11.0,0.0,0.01),
                    "Curing time (days)": st.slider("Curing time (days)",1.0,360.0,1.0,1.0),
                    "Water-cement ratio": st.slider("Water-cement ratio",0.1,6.0,0.1,0.01),
                },
            ]
            )             


    # input = load_excel("Por favor, entre com o arquivo de treino", help)
    st.header("Results")

    if edited_df is not None:
        placeholder = st.empty()
        if placeholder.button("Run", disabled=False, key=1):
            placeholder.button("Run", disabled=True, key=2)
            if edited_df is not None:
                # if st.checkbox('Mostrar dados',key= f'check_{key}'):
                #      st.write(standard(df))
                with st.spinner("Please wait"):
                    results = MODEL_CONCRETA_MORTAR(edited_df,SCALE,MODEL)
                    st.success("Success!")
                    placeholder.button("Run", disabled=False, key=3)
                    # st.write(standard(results))
                    st.markdown(f"fck Predict: {results.iloc[0,0]}")

                    # st.bar_chart(chart_data)
                    st.markdown(
                    "Disclaimer: prediction information is not a recommendation to waive laboratory dosage tests. However, AI helps technicians in the area to get an estimate of the mechanical strength of the concrete mixture."
                     )

elif tabs == "Desirability":
    st.subheader("This feature is under construction with our team, stay tuned for new deliveries!")

elif tabs == "About":
    st.header("Research team")

    st.image(
        "http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id=K4460682U0",
        width=150,
    )
    st.markdown(
        r"Prof. Wanderlei Malaquias Pereira Junior [lattes](https://bra01.safelinks.protection.outlook.com/?url=http%3A%2F%2Flattes.cnpq.br%2F2268506213083114&data=05%7C01%7C%7Ca653a238242d42650f4608db25afdc19%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C638145209466723297%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=GP4tAI9hvkoBiyDBnl6%2FT6WZgvTfkgBNfPf%2BZAPNbSA%3D&reserved=0)"
    )

    st.image(
        "http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id=K4263660E3",
        width=150,
    )
    st.markdown(
        r"Prof. Antover Panazzolo Sarmento [lattes](https://bra01.safelinks.protection.outlook.com/?url=http%3A%2F%2Flattes.cnpq.br%2F4025685702530313&data=05%7C01%7C%7Ca653a238242d42650f4608db25afdc19%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C638145209466723297%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=HN%2FWp9r%2FcnHhVdQjBSxAGZk8X%2F4DF75fVrZAPGAhyIM%3D&reserved=0)"
    )

    st.image(
        "http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id=K4713856P6",
        width=150,
    )
    st.markdown(
        r"Prof. Rogério Pinto Espíndola [lattes](https://bra01.safelinks.protection.outlook.com/?url=http%3A%2F%2Flattes.cnpq.br%2F8968151880884493&data=05%7C01%7C%7Ca653a238242d42650f4608db25afdc19%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C638145209466723297%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=SDZvy5arc09gLzXfZMDj7D7gqFgGIO4xZ3i1wOcGGWI%3D&reserved=0)"
    )

    st.image(
        "http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id=K4768864J3",
        width=150,
    )
    st.markdown(
        r"Prof. Daniel de Lima Araújo [lattes](http://lattes.cnpq.br/8801080897723883)"
    )

    st.image(
        "http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id=K4759259U2",
        width=150,
    )
    st.markdown(
        r"Prof. Gustavo de Assis Costa [lattes](http://lattes.cnpq.br/1543798708473666)"
    )

    st.image(
        "http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id=K8173657Y6",
        width=150,
    )
    st.markdown(
        r"Eng. Ma. Amanda Isabela de Campos [lattes](http://lattes.cnpq.br/0348866215558920)"
    )

    st.image(
        "http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id=K8788266T0",
        width=150,
    )
    st.markdown(
        r"Eng. Roberto Viegas Dutra [lattes](http://lattes.cnpq.br/5798494916940315)"
    )

    st.image("http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id=K4768864J3", width=150)
    st.markdown(r"Comp. Nilson Jorge Leão Júnior")
