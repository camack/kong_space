# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:33:19 2022

@author: BANJIAJIA
"""

import streamlit as st
import requests,time
# from streamlit_lottie import st_lottie
import numpy as np

st.set_page_config(page_title='',page_icon=':computer:',layout='wide')
# st.title(':computer:'+'streamlit is yyds')
# data = np.random.randn(10,3)

# def load_lottie(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
# lottie_code = load_lottie('https://assets2.lottiefiles.com/packages/lf20_2QSlz3Li88.json')
# st_lottie(lottie_code,height=300,key='coding')
# lottie_code1 = load_lottie('https://assets3.lottiefiles.com/packages/lf20_tz0ueLYOIU.json')
# lottie_code2 = load_lottie('https://assets3.lottiefiles.com/packages/lf20_bisEAxBURd.json')
# lottie_code3 = load_lottie('https://assets3.lottiefiles.com/packages/lf20_ZarZVZIG3T.json')

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
#         )

# with st.sidebar:
#     with st.echo():
#         st.write("This code will be printed to the sidebar.")
        
#     with st.spinner("Loading..."):
#         time.sleep(2)
#     st.success("Done!")


st.subheader('日期：222年9月20日，星期二')
st.subheader('天气：多云:cloud:')
st.subheader('心情：惊讶、开心:smile::flushed:')
st.subheader('事件：操场的大树下有好多灯笼果')
st.subheader('记录人：孔妙妍:girl:')
st.markdown('---')

col1,col2 = st.columns([2,3])
with col1:
    st.image('rc.jpg')
with col2:
    st.subheader('操场旁的灯笼果')
    st.write(
        """
            学校操场的大树下，有好多可爱的“灯笼果”。
    说是灯笼果，其实是果子外面都有一层薄薄的外衣，只不灯笼果的外衣是金黄色的椭圆形，而小果子的外衣却是深粉色加淡绿色的三角形！神不神奇，还有更神奇的吗?有啊。这外衣里面不是一个大果子，而是三个隔间，每个隔间里长着两个小小小小果子。不过，好奇怪哦，小果子和灯笼果的外衣大小还差不多，为什么果子的差距这么大呢？
        """
        )












# st.write('---')

# col1,col2,col3 = st.columns(3)
# with col1:
#     st.subheader('心情美丽')
#     st_lottie(lottie_code1,height=200)
# with col2:
#     st.subheader('心情美丽')
#     st_lottie(lottie_code2,height=200)
# with col3:
#     st.subheader('心情美丽')
#     st_lottie(lottie_code3,height=200)
    
# st.write('---')
    
# col4,col5 = st.columns([2,3])
# with col4:
#     st.image('desert.jpg')
# with col5:
#     st.subheader('美丽中国:cactus:')
#     st.write('党的十八大以来，以习近平同志为核心的党中央以前所未有的力度抓生态文明建设，美丽中国建设迈出重大步伐，我国生态环境保护发生历史性、转折性、全局性变化')
#     st.write('[中能建建筑集团](http://www.aepc1.ceec.net.cn/)')
    
# col4,col5 = st.columns([2,3])
# with col4:
#     st.image('sky.jpg')
# with col5:
#     st.subheader('美丽中国:sunny:')
#     st.write('党的十八大以来，以习近平同志为核心的党中央以前所未有的力度抓生态文明建设，美丽中国建设迈出重大步伐，我国生态环境保护发生历史性、转折性、全局性变化')
#     st.write('[中能建建筑集团](http://www.aepc1.ceec.net.cn/)')

# col4,col5 = st.columns([2,3])
# with col4:
#     st.image('jungle.jpg')
# with col5:
#     st.subheader('美丽中国:leaves:')
#     st.write('党的十八大以来，以习近平同志为核心的党中央以前所未有的力度抓生态文明建设，美丽中国建设迈出重大步伐，我国生态环境保护发生历史性、转折性、全局性变化')
#     st.write('[中能建建筑集团](http://www.aepc1.ceec.net.cn/)')

# st.markdown('---')

# tab1,tab2,tab3 = st.tabs(['sky','desert','jungle'])
# with tab1:
#     st.subheader('中华一家亲')
#     st.image('sky.jpg',width=800)
# with tab2:
#     st.subheader('中华一家亲')
#     st.image('desert.jpg',width=800)
# with tab3:
#     st.subheader('中华一家亲')
#     st.image('jungle.jpg',width=800)
    
# st.markdown('---')

# st.bar_chart(data)
# with st.expander('阅读全文'):
#     st.write(
#         """
#         “美丽中国”是中国共产党第十八次全国代表大会提出的概念，强调把生态文明建设放在突出地位，融入经济建设、政治建设、文化建设、社会建设各方面和全过程。
#         2012年11月8日，在十八大报告中首次作为执政理念出现。
#         2015年10月召开的十八届五中全会上，“美丽中国”被纳入“十三五”规划，首次被纳入五年计划 。
#         2017年10月18日，习近平同志在十九大报告中指出，加快生态文明体制改革，建设美丽中国。
#         """
#         )
#     st.image('sky.jpg',width=300)
    
# st.markdown('---')

# with st.container():
#    st.write("This is inside the container")
#    # You can call any Streamlit command, including custom components:
#    st.bar_chart(np.random.randn(50, 3))
# st.write("This is outside the container")

# st.markdown('---')

# with st.empty():
#     for seconds in range(8):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")
    
# placeholder = st.empty()
# placeholder.text('Hello')
