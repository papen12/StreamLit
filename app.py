import streamlit as st 
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np 
import altair as alt
st.write("Hola mundo")

num1=st.number_input("numero 1")

#titulo 



st.title("Este es un titulo")

st.header("Esta es un encabezado ")

st.subheader("This is our Sub-header")

st.caption("Este es un titulo pequeño")


st.text("Hola mundo")

st.markdown("# Título grande")
st.markdown("## Subtítulo")
st.markdown("### Más pequeño")
st.markdown("***Texto en cursiva/negrita***")


df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)


chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b']
)

st.write(chart)


"""
# Magic Feature
Markdown working without defining its function explicitly.
"""




