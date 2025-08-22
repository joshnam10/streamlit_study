import streamlit as st
import os

print(os.listdir('algorithm'))
# st.page_link("1.py", label="introduction")
# st.page_link("https://www.google.com",label="google")
pages={
    'intro':[],
    'algorithm':[],
    'dataScience':[],
    'streamlitEx':[],
    'py실습':[]
    }

folders=list(pages.keys())
for folder in folders:
    for file in os.listdir(folder):
        pages[folder].append(st.Page("./"+folder+"/"+file,title=file))
pg=st.navigation(pages)
pg.run()