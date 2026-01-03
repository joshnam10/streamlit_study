import streamlit as st
import os
import glob

pages={}
for path in glob.glob('*'):
    if not os.path.isdir(path):
        continue
    if '__' in path:
        continue
    
    pages[path.replace('1','')]=[]
    for filePath in glob.glob(path+'/*'):
        file=os.path.split(filePath)[1]
        page=st.Page(filePath,title=file[:-3].replace('_',' '))
        pages[path.replace('1','')].append(page)

pg=st.navigation(pages)
pg.run()


logo_link='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png'
st.logo(logo_link)
