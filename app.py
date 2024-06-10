import streamlit as st
import os
import tempfile
from amonymisation import anonymisation

st.set_page_config(page_title="IA APP", page_icon=":camera", layout="centered", initial_sidebar_state="collapsed")

st.image("assets/anonymation.jpg", use_column_width=True)
st.header("Anonimar imágenes")
st.subheader("Sube una imágen")
uploaded_image = st.file_uploader("Selecciona una imágen...", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

file_name = "processed_image.png"

if uploaded_image is not None:

    st.image(uploaded_image, caption="Imágen subida", use_column_width=True)
    anonymisation_button = st.button(label = "Anonimizar")

    if anonymisation_button:

        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_image.read())
                file_path = temp_file.name
            
            temp_final_img = anonymisation(file_name, file_path)

            st.image(temp_final_img, caption="Imágen anonimizada", use_column_width=True)
            with open(file_name, "rb") as f:
                image_data = f.read()

            st.download_button("Descargar Image sin Fondo", data=image_data, file_name=file_name)
            os.remove(file_name)

        except:
            st.error("Ha ocurrido un error, prueba con otra imagen.")
        
