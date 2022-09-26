import seaborn as sns
import streamlit as st
import pandas as pd
import plotly.express as px
df_peng=sns.load_dataset("penguins")
fig=sns.pairplot(data=df_peng, hue="sex", kind="scatter", diag_kind="kde", markers=["o","s"],
plot_kws={"s":100},diag_kws={"fill":True},corner=False)

st.write('''
# Penguin Dataset 
** Pair Plot **
# ''')
st.pyplot(fig)

