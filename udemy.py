import pandas as pd
import numpy as np
import math
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import streamlit as st
import altair as alt
import plotly.express as px

data=pd.read_csv("/Users/macos/github/udemy_ca/udemy_stre/udemy_courses-raw.csv",parse_dates=True,index_col=["published_timestamp"])
data["year"] = data.index.year
def serch_by_word(title):
        course=[]
        a=str(title)
        f=data['course_title'].str.lower()

        for i in range(len(f)):
          if a in f[i]:
            course.append( f[i])
        prices=[]
        for i in range(len(course)):
          e=data[data['course_title'].str.lower()==course[i]]['course_title']
          prices.append(list(e))
          flat_list = [item for sublist in prices for item in sublist]
          de=data[data['course_title'].isin(flat_list)]
        return st.dataframe(de)

def scatte(t,e):
    #a=data[x] + np.random.normal(0,2.5, size=len(data))
    #st.bar_chart(data[x],data[y])
    r=data[t].to_list
    o=data[e].to_list
    #st.bar_chart(x=r,y=o)
    st.bar_chart(data=data, x=t, y=e, width=0, height=0, use_container_width=True)
def course(x):
 #plt1= data[x].value_counts().plot(kind='bar')
 st.bar_chart(data[x].value_counts())

import plotly.express as px
def scatter(x,y): 
 fig = px.scatter(
    data[data["subject"]==x].head(y),
    x="num_reviews",
    y="num_subscribers",
    size="price",
    color="level",
    log_x=True,
    width=600, height=400
 )

 st.plotly_chart(fig)

   
menu = ["Home", "EDA", "prediction"]
choice = st.sidebar.selectbox("Menu", menu)
limit=st.sidebar.slider('select year', 2011, 2016, 2017 )
if limit:
  data=data[data["year"]==limit]
else:
  data=data
if choice == "Home":
    st.header(' 📚Little Info About the Project 📚')
if choice == "EDA":
    title = st.text_input('enter titles')
    serch_by_word(title)
    a=list(data.columns)

    options = st.multiselect('enter',a)
    scatte(options[0],options[1])
    optio = st.selectbox('select',a)
    course(optio)
    chart = alt.Chart(data).mark_circle().encode(
    x='price',
    y='num_subscribers',
    color='level',).interactive()
    tab1,tab2 = st.tabs(["plot", "lot"])

    with tab1:
    
     st.altair_chart(chart, use_container_width=True)
    with tab2:
        st.altair_chart(chart, use_container_width=True)
    e=list(data['subject'].unique())
    opti = st.selectbox('select',e)
    t = st.slider('select how many rows ?', 10, 50, 200)


    scatter(opti,t)


    



 
 


  


