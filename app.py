import streamlit as st 
from logic.funciones import Sumar
#Semejanza con el print muchos usos para mostrar distintos tipos de mensajes
st.write("Hola Mundo")

#ELEMENTOS DE TEXTO DE STREAMLIT

st.title("Este es un título")        # Título principal de la página
st.header("Este es un encabezado")   # Encabezado de una sección
st.caption("Este es un título pequeño",)  # Texto descriptivo pequeño
st.text("Texto pequeño")             # Texto plano sin formato




input_texto=st.text_input("Ingrese su nombre",max_chars=15)


st.write(input_texto)


input_num=st.number_input("Ingrese su edad",min_value=0,max_value=120)


btn_Saludar=st.button("Presionar"
                      ,help="Este boton sirve para saludar"
                      ,type="primary")


if btn_Saludar:
    st.text(f"Hola mi nombre es: {input_texto}")
    
    
select_box=st.selectbox("Seleccione su lenguaje",
                        options=["JS","Python","C++"],
                        accept_new_options=False)


num_a=st.number_input("Ingrese El numero 1",min_value=0,max_value=120)
num_b=st.number_input("Ingrese El numero 2",min_value=0,max_value=120)

btn_Sumar=st.button("Sumar"
                      ,help="Este boton sirve para sumar"
                      ,type="primary")


if btn_Sumar:
    suma=Sumar(num_a,num_b)
    st.write(suma)
