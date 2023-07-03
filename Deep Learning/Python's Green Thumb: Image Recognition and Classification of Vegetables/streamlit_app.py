import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
#import cv2
#import pandas as pd
#from st_aggrid import AgGrid
#import plotly.express as px
import io 
from Image_recognition import predict_picture
from text_generator import get_fact, get_fact_kids, get_fact_kids, get_recipe, get_story
from gtts import gTTS

    
def button(text: str = None, color='#FFFFFF', height='20px'):
    st.markdown(
        f"""
        <div style="
            display: inline-flex;
            align-items: center;
            padding: 0.5em 1em;
            color: #321E37;
            background-color: {color};
            border-radius: 20px;
            text-decoration: none;
            height: {height};
            width: 100px;
            font-size: 16px;
            font-weight: bold;">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )

import streamlit as st

def button_with_triangles(text: str = None, color='#FFFFFF', height='20px'):
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <div style="
                width: 0;
                height: 0;
                border-bottom: 12px solid transparent;
                border-top: 12px solid transparent;
                border-left: 12px solid {color};">
            </div>
            <div style="
                display: inline-flex;
                align-items: center;
                padding: 0.5em 1em;
                color: #EEEEEE;
                background-color: {color};
                border-radius: 20px;
                text-decoration: none;
                height: {height};
                width: 90px;
                font-size: 16px;">
                {text}
            </div>
            <div style="
                width: 0;
                height: 0;
                border-bottom: 12px solid transparent;
                border-top: 12px solid transparent;
                border-right: 12px solid {color};">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )



def txt_with_bck(text: str = None, color='#FFFFFF', height='20px', width='500px'):
    st.markdown(
        f"""
        <div style="
            display: inline-flex;
            align-items: center;
            padding: 0.5em 1em;
            color: #321E37;
            background-color: {color};
            border-radius: 20px;
            text-decoration: none;
            height: {height};
            width: {width};
            font-size: 16px;
            text-align: justify;">  <!-- Aggiunto 'text-align: justify;' -->
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )

    
    

    
# GRAFICAL ELEMENTS

emoji_dictionary = {
'cabbage':'🥬',
'capsicum':'🫑',
'carrot':'🥕',
'cauliflower':'🥦',
'chilli pepper':'🌶️',
'cucumber':'🥒',
'eggplant':'🍆',
'garlic':'🧄',
'ginger':'🫚',
'lettuce':'🥬',
'onion':'🧅',
'peas':'🫛',
'potato':'🥔',
'spinach':'🥬',
'sweetcorn':'🌽',
'tomato':'🍅'
}
    

color_dictionary = {
'cabbage':'E7F5E1',
'capsicum':'C7DBC8',
'carrot':'F9DDCB',
'cauliflower':'FFFEF8',
'chilli pepper':'F3C1BD',
'cucumber':'C4D6BC',
'eggplant':'CAB7C9',
'garlic':'FFFCF8',
'ginger':'FAEAD6',
'lettuce':'E7F5E1',
'onion':'FEE2BF',
'peas':'FAFCF1',
'potato':'E9DFD2',
'spinach':'C8D6BC',
'sweetcorn':'FCF8CB',
'tomato':'F0CCC5'
}


# Define the custom objects dictionary
custom_objects = {'KerasLayer': hub.KerasLayer}
#Load the model using the custom objects
model = tf.keras.models.load_model(
    'models/inception_16cl_40ep.h5', custom_objects=custom_objects)




with st.sidebar:
    choose = option_menu("App Gallery", ["Upload your picture", "Learning", "To know and taste","About"],
                         icons=['camera', 'balloon', 'egg-fried','house'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "#FFC89C", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#007893"},
    }
    )
    
 



input_img = None




#------------------- UPLOADING PAGE --------------------#

if choose == "Upload your picture":
    
    col1, col2 = st.columns([0.2, 0.8])
    with col1:
        way = st.radio("Load a picture via",('Upload','Camera'))
    with col2:
        if way == 'Camera':
            input_img = st.camera_input("")
        else:
            input_img = st.file_uploader("", type=["jpg", "jpeg","png", "bmp"])
    if input_img is not None:        
        with col2:
            st.image(input_img, width=200)
            ingredient_datafile = predict_picture(input_img, model)
            st.write(f"The image is a {ingredient_datafile} {emoji_dictionary[ingredient_datafile]}")
            
        #Call ChatGPT API for later use. In this way we concentrate the running time here
    
        #KIDS: facts
            kids_fact1 = get_fact_kids(ingredient_datafile)
            kids_fact2 = get_fact_kids(ingredient_datafile)
            kids_fact3 = get_fact_kids(ingredient_datafile)
            kids_fact4 = get_fact_kids(ingredient_datafile)
        #KIDS: story
            kids_story = get_story(ingredient_datafile)
        #ADULTS: facts
            historical_fact = get_fact(ingredient_datafile,'historical')
            cultural_fact = get_fact(ingredient_datafile,'cultural')
            healthy_fact = get_fact(ingredient_datafile,'healthy')
            funny_fact = get_fact(ingredient_datafile,'funny')
            bad_fact = get_fact(ingredient_datafile,'bad')
        #ADULTS: recipe
            recipe = get_recipe(ingredient_datafile)
        #Print the result for image calssification
            st.write(f"The image is a {ingredient_datafile} {emoji_dictionary[ingredient_datafile]}")

        #Create sidebar variables
            st.session_state.shared_variable = ingredient_datafile
            st.session_state.kids_fact_1 = kids_fact1
            st.session_state.kids_fact_2 = kids_fact2
            st.session_state.kids_fact_3 = kids_fact3
            st.session_state.kids_fact_4 = kids_fact4
            st.session_state.story = kids_story
            st.session_state.historical_fact = historical_fact
            st.session_state.cultural_fact = cultural_fact
            st.session_state.healthy_fact = healthy_fact
            st.session_state.funny_fact = funny_fact
            st.session_state.bad_fact = bad_fact
            st.session_state.recipe = recipe

#------------------- KIDS PAGE --------------------#       


        
elif choose == "Learning":
    # Access the shared variable in Option Upload your picture
    if st.session_state.shared_variable is not None:
        logo = Image.open(f'/Users/G/Desktop/Documents/Formazione in Data Science/WBS/WBS Bootcamp/10. Final Project/data/streamlit_images/{st.session_state.shared_variable}.jpg')
        head1, head2 = st.columns([0.8, 0.2])
        with head1:               # To display the header text using css style
            st.markdown(""" <style> .font {
            font-size:35px ; color: #000000;} 
            </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">Learning about the {st.session_state.shared_variable}</p>', unsafe_allow_html=True)    
        with head2:               # To display brand log
            st.image(logo, width=130 )


        col_facts_1, col_space, col_facts_2 = st.columns( [0.5,0.1,0.5])


        with col_facts_1:
            button_with_triangles('-----------','#E2E0ED','20px')
            st.write('')
            with st.expander('Unwrap candy 1'):
                st.write(st.session_state.kids_fact_1)
            button_with_triangles('-----------','#FFC89C','20px')
            st.write('')
            with st.expander('Unwrap candy 2'):
                st.write(st.session_state.kids_fact_2)
        with col_facts_2:
            button_with_triangles('-----------','#FF2F92','20px')
            st.write('')
            with st.expander('Unwrap candy 3'):
                st.write(st.session_state.kids_fact_3)
            button_with_triangles('-----------','#92D050','20px')
            st.write('')
            with st.expander('Unwrap candy 4'):
                st.write(st.session_state.kids_fact_4)
        st.divider()
        col_margin_1, col_story, col_margin_2 = st.columns([0.1,0.6,0.2])
        with col_story:
            st.markdown(""" <style> .font {
        font-size:30px ; color: #000000;} 
        </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">A story by the author GPT </p>', unsafe_allow_html=True)
            txt_with_bck(st.session_state.story, f'#{color_dictionary[st.session_state.shared_variable]}', height=f'{round(len(st.session_state.recipe[1]))}px')

        
        
        
        
        
        
        

#------------------- ADULTS PAGE --------------------#          
elif choose == "To know and taste":
    if st.session_state.shared_variable is not None:
        logo = Image.open(f'/Users/G/Desktop/Documents/Formazione in Data Science/WBS/WBS Bootcamp/10. Final Project/data/streamlit_images/{st.session_state.shared_variable}.jpg')
                 
        st.markdown(""" <style> .font {
        font-size:35px ; color: #000000;} 
        </style> """, unsafe_allow_html=True)
        st.markdown(f'<p class="font">To know on and to taste </p>', unsafe_allow_html=True)    

            
        
        col_margin_1, col_facts, col_margin_2 = st.columns([0.1,0.4,0.2])
        with col_facts:
            st.header(f'')
            st.header(f'')
            with st.expander(f'The {st.session_state.shared_variable} in history'):
                st.write(st.session_state.historical_fact)
            with st.expander(f'Some culture around {emoji_dictionary[st.session_state.shared_variable]}{emoji_dictionary[st.session_state.shared_variable]}'):
                st.write(st.session_state.cultural_fact)
            with st.expander(f'One {emoji_dictionary[st.session_state.shared_variable]} a day keeps the doctor away: health'):
                st.write(st.session_state.healthy_fact)
            with st.expander(f'Fun fact about the {st.session_state.shared_variable}'):
                st.write(st.session_state.funny_fact)
            with st.expander(f'{emoji_dictionary[st.session_state.shared_variable]}{emoji_dictionary[st.session_state.shared_variable]} and bad facts'):
                st.write(st.session_state.bad_fact)
        with col_margin_2:
            st.image(logo, width=130 )
        with col_margin_1:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            # Flip the image horizontally
            flipped_logo = logo.transpose(Image.FLIP_LEFT_RIGHT)

            # Convert the flipped image to bytes
            byte_array = io.BytesIO()
            flipped_logo.save(byte_array, format='PNG')
            byte_array = byte_array.getvalue()

            # Display the flipped image
            st.image(byte_array, width=70)
        
        st.divider()
         
        
        col_margin_1, col_story, col_margin_2 = st.columns([0.1,0.6,0.2])
        with col_story:
            st.markdown(""" <style> .font {
        font-size:30px ; color: #000000;} 
        </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">Chef GPT recommends {st.session_state.recipe[0]}</p>', unsafe_allow_html=True)
            txt_with_bck(st.session_state.recipe[1], f'#{color_dictionary[st.session_state.shared_variable]}', height=f'{round(len(st.session_state.recipe[1])/2)}px')

    
    
    
    
    
    
    
#------------------- ABOUT PAGE --------------------#    
    
elif choose == "About":
    st.write('**About the creators**')
    st.write('**Resources**')
    st.write("https://medium.com/codex/create-a-multi-page-app-with-the-new-streamlit-option-menu-component-3e3edaf7e7ad")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
