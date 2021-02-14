import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import time

st.title('This page was built using Streamlit')


"""
## Image view
```
st.write('DisplayImage')
img = Image.open('img/sample.png')
st.image(img,caption="sample")
```
"""
if st.checkbox("show image"):
    img = Image.open('img/sample.png')
    st.image(img,caption="sample")


"""
## Simple Dataframe control
```Python code
st.write(df)
st.dataframe(df.style.highlight_max(axis=1))
st.table(df.style.highlight_max(axis=0))
```
"""
if st.checkbox("show more"):
    df1 = pd.DataFrame({
        "1列目":[1,2,3,4],
        "2列目":[10,20,30,40]
    })
    st.write(df1)
    st.dataframe(df1.style.highlight_max(axis=1))
    st.table(df1.style.highlight_max(axis=0))




"""
## Chart Drawing
### unsorted randn_data
```Python code
df2 = pd.DataFrame(
    np.random.randn(20,3),
    columns=["x","y","z"]
)
st.write(df2)
st.line_chart(df2)
```
"""
df2 = pd.DataFrame(
    np.random.randn(20,3),
    columns=["x","y","z"]
)
st.write(df2)
st.line_chart(df2)
"""
### sorted by x randn_data
```
df2_ = df2.sort_values("x")
df2_ = df2_.reset_index()
df2_ = pd.DataFrame(df2_.iloc[:,1:4])
st.write(df2_)
st.area_chart(df2_)
```
"""
df2_ = df2.sort_values("x")
df2_ = df2_.reset_index()
df2_ = pd.DataFrame(df2_.iloc[:,1:4])
st.write(df2_)
st.area_chart(df2_)



"""
### Normal Distribution
```Python code
arr = np.random.normal(1,1,size=1000)
fig,ax = plt.subplots()
ax.hist(arr,bins=50,label="test")
st.pyplot(fig)
```
"""
option = st.selectbox("Select the number of times to extract from the normal distribution in the range from 0 to 1000",list(range(0,1100,50)))

arr = np.random.normal(1,1,size=option)
fig,ax = plt.subplots()
ax.hist(arr,bins=50,label="test")
st.pyplot(fig)



"""
## Map Plotter
Add a random number to the latitude and longitude of the area near Shinjuku.
```
df = pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[35.69,139.70],
    columns=["lat","lon"]
)
st.map(df)
```
"""
slide = st.slider("num of samples",0,200,30)
df = pd.DataFrame(
np.random.randn(slide,2)/[50,50]+[35.69,139.70],
columns=["lat","lon"]
)
st.map(df)

