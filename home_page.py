import streamlit as st

# Função para a página inicial
def home_page():
    st.title("Página Inicial")
    st.write("""
    <p style='font-size: 16px; line-height: 1.6;'>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi.
        Phasellus vitae libero eu felis feugiat hendrerit. Sed ut turpis eros.
        Integer ac justo in massa mollis pretium. Vestibulum sit amet dapibus nisl.
        Nullam consectetur risus vel dolor scelerisque, nec posuere mi volutpat.
        Fusce sit amet sodales risus. Proin ac risus nec magna scelerisque sodales.
        Sed auctor, purus id suscipit tempor, est quam scelerisque nisl, a bibendum elit metus eu orci.
    </p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi.
        Phasellus vitae libero eu felis feugiat hendrerit. Sed ut turpis eros.
        Integer ac justo in massa mollis pretium. Vestibulum sit amet dapibus nisl.
        Nullam consectetur risus vel dolor scelerisque, nec posuere mi volutpat.
        Fusce sit amet sodales risus. Proin ac risus nec magna scelerisque sodales.
        Sed auctor, purus id suscipit tempor, est quam scelerisque nisl, a bibendum elit metus eu orci.
    """, unsafe_allow_html=True)