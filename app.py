import streamlit as st

st.markdown('**@author: koshal**')
html = """
<div style='background-color:tomato;padding:10px'>
<h2 style='color:white;text-align:center;'><b>Racing Bar Charts</b> </h2>
</div>
"""
st.markdown(html, unsafe_allow_html=True)
#st.subheader('')

st.markdown("""     <div style='background-color:white;padding:10px'>
                    <h4 style='color:black'> About App </style></h4>
                        <ol>
                        <li>All the Videos are made with Python's Matplotlib Library only</li>
                        <li>Matplotlib's Animation class is used</li>
                        <li>Audio is added manually after creating Video</li>
                        <li>Select a Topic to play video</li></ol>
                    """, unsafe_allow_html=True)

st.markdown("""<h4 style='color:green;'><b>Select The Race</b></h4>""", unsafe_allow_html=True)

bars = ['World Population','Total Army Personal','World GDP','Expenditure on Army','Mobile Subscriptions']
box = st.selectbox('',bars)

but = st.button('Begin Race')
if but:
    if box == 'World Population':
        st.markdown("""
                    <h4 style='color:black'>Features :</h4>
                        <ol>
                        <li>Top Ten Countries in each year with higgest Population </li>
                        <li>From 1960 to 2016</li></ol>
                    """, unsafe_allow_html=True)
        video_file = open('pop.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        
    if box == 'World GDP':
        st.markdown("""
                    <h4 style='color:black'>Features :</h4>
                        <ol>
                        <li>Top Ten Countries in each year with higgest GDP </li>
                        <li>GDP is in Billion US Dollars</li>
                        <li>From 1960 to 2018</li>
                        </ol>
                    """, unsafe_allow_html=True)
        video_file = open('gdp.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    
    if box == 'Total Army Personal':
        st.markdown("""
                    <h4 style='color:black'>Features :</h4>
                        <ol>
                        <li>Top Ten Countries with largest Army </li>                        
                        <li>From 1989 to 2017</li>
                        </ol>
                    """, unsafe_allow_html=True)
        video_file = open('total_army.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
      
    if box == 'Expenditure on Army':
        st.markdown("""
                    <h4 style='color:black'>Features :</h4>
                        <ol>
                        <li>Top Ten Countries with highest Expenditure on Army/Forces </li>                        
                        <li>From 1960 to 2018</li>
                        </ol>
                    """, unsafe_allow_html=True)
        video_file = open('army_expenditure.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)   
        
    if box == 'Mobile Subscriptions':
        st.markdown("""
                    <h4 style='color:black'>Features :</h4>
                        <ol>
                        <li>Top Ten Countries with highest Mobile Users </li>                        
                        <li>From 1980 to 2018</li>
                        </ol>
                    """, unsafe_allow_html=True)
        video_file = open('Subscriptions.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
