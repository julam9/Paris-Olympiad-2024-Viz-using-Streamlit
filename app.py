import pandas as pd 
import streamlit as st 
import plotly.express as px

medals_ = pd.read_csv('data/medals_total.csv')
coach_ = pd.read_csv('data_clean/coach_clean.csv')
medallist_ = pd.read_csv('data_clean/medallist_clean.csv') 
athlete_ = pd.read_csv('data_clean/athlete_data.csv')

def intro():
    st.write("# Welcome to Paris Olympiad 2024 Dashboard! 👋")
    st.sidebar.success("Select a category you want to know.")

    st.markdown(
        """
        The 2024 Summer Olympics (French: Jeux olympiques d'été de 2024), officially the Games of the XXXIII Olympiad (French: Jeux de la XXXIIIe olympiade de l'ère moderne) and branded as Paris 2024, were an international multi-sport event held from 26 July to 11 August 2024 in France (Wikipedia)
    """
    )

def athlete():
    st.title("Athlete in the Olympic 2024")

def coach():
    st.title("Coach in the Olympic 2024")
    
def medals():
    st.title("Medal distribution")
        
page_names_to_funcs = {
    "General": intro,
    "Athlete": athlete,
    "Coach" : coach,
    "Medals" : medals
}

demo_name = st.sidebar.selectbox("Choose a scope", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
