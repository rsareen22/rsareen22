import seaborn as sns
import streamlit as st
import pandas as pd
import plotly.express as px
df_iris=sns.load_dataset("iris")
df_iris
figure_scatter=px.scatter_3d(data_frame=df_iris, x='sepal_length', y="sepal_width", z="petal_length", color="species")
figure_scatter

st.write("""
# Iris Dataset 
A 3d Scatter Plot between sepal length sepal width and petal length
# """)
st.plotly_chart(figure_scatter, use_container_width=True)

st.write("""
# Exploring other plots
# """)

fig = px.scatter(data_frame=df_iris, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
           marginal_x="box", trendline="ols", template="simple_white")
fig