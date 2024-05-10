import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title = "Ley de ohm",
    page_icon = "⚡"
)

st.header('⚡**LEY DE OHM**⚡', divider='gray', anchor= "str",)

col1, col2= st.columns(2)
with col1:
    st.header("Que desea calcular")
    selected = option_menu(menu_title =None , options = ['Tension', 'Corriente', 'Resistencia'])

with col2:
    st.header("")
    st.header("")
    if selected == "Tension":
        i = st.number_input(label = "Coloque el valor de la corriente", value=0)
        r = st.number_input(label = "Coloque el valor de la resistencia", value=0)

        if st.button("Calcular"):
            v = i * r
            st.write("El valor de la tension es de", v , "[V]")

    if selected == "Corriente":
        v = st.number_input(label = "Coloque el valor de la Tension", value=0)
        r = st.number_input(label = "Coloque el valor de la resistencia", value=0)

        if st.button("Calcular"):
            i = v / r
            st.write("El valor de la tension es de", i , "[A]")

    if selected == "Resistencia":
        v = st.number_input(label = "Coloque el valor de la Tension", value=0)
        i = st.number_input(label = "Coloque el valor de la Corriente", value=0)

        if st.button("Calcular"):
            r = v / i
            st.write("El valor de la tension es de", r , "Ω")