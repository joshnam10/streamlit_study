import streamlit as st
st.title('media')

st.subheader('image')
image_link='https://www.fitpetmall.com/wp-content/uploads/2023/10/GettyImages-492548888-1.png'
st.image(image_link,caption='강아지')

st.divider()

st.subheader('video')
video_link='https://cdn.pixabay.com/video/2016/12/31/6962-197634410_large.mp4'
st.video(video_link, autoplay=True, muted=True)

st.divider()

