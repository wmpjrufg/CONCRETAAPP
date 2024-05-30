import streamlit as st

# Função para a página inicial
def home_page():
    st.title("Hello, I'm CONCRETA")
    st.write("""
    <p style='font-size: 16px; line-height: 1.6; text-align: justify;'>
    the first Brazilian AI to be built to determine the concrete strength (fck) based on dosage data. Come and learn a little about my story. 
    I am one of the creations of the GPEE (Research and Studies Group in Civil Engineering) of UFCAT (Federal University of Catalão) and 
    I am here to help you who want to determine properties of concrete.<br><br>
    In side bar select service to use me.
    </p>
    """, unsafe_allow_html=True)
    
    with open("paper_concrete.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        
    st.download_button(label="Download Concrete Paper",
                       data=PDFbyte,
                       file_name = f'paper_concrete.pdf')
    
    with open("dataset-full_concrete.xlsx", "rb") as exc_file:
        EXCbyte = exc_file.read()
    
    st.download_button(label="Download Concrete Dataset",
                    data=EXCbyte,
                    file_name = f'dataset-full_concrete.xlsx')