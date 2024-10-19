import pandas as pd 
import streamlit as st 
import plotly.express as px

medals_st = pd.read_csv('data/medals_total.csv')
coach_st = pd.read_csv('data_clean/coach_clean.csv')
medallist_st = pd.read_csv('data_clean/medallist_clean.csv') 
athlete_st = pd.read_csv('data_clean/athlete_data.csv')

def intro():
    st.write("# Welcome to Paris Olympiad 2024 Dashboard! 🏆")
    st.sidebar.success("Select a category you want to know.")

    st.markdown(
        """
        The 2024 Summer Olympics (French: Jeux olympiques d'été de 2024), officially the Games of the XXXIII Olympiad (French: Jeux de la XXXIIIe olympiade de l'ère moderne) and branded as Paris 2024, were an international multi-sport event held from 26 July to 11 August 2024 in France (Wikipedia)
        """ 
    
    """
    In 2024 Paris Olympic, there are some facts that you should know. Based on [Time](https://time.com/7003861/paris-olympics-2024-host-city-surprising-facts/) :
    - Paris has hosted the Olympics twice before
    - The park outside the Eiffel Tower has a bloody history
    - Many consider the river Seine to be the “main character” of the city
    - Paris is not the city’s original name
    - The city is home to 6 million preserved skeletons 
    - The Grand Mosque of Paris has a rich history 
    - The international prototype of the kilogram is located in Paris 
    - Some Parisians refer to non-Parisians as “ploucs” 
    - The Louvre is the world’s most visited museum 
    - The Bastille prison no longer exists
    
    If you want to know more details about Paris Olympic, you can choose the category at the sidebar 👈
    """
    )
    

def athlete():
    st.title("Athlete in the Olympic 2024") 
    st.markdown(f"""
    <div style="text-align: center;">
        <h1 style="font-size: 60px;">{athlete_st.name.nunique()}</h1>
        <p>Athletes participated in this event.</p>
    </div>
    """, unsafe_allow_html=True)

    gender_ath = px.bar(athlete_st.gender.value_counts(), x=athlete_st.gender.value_counts().index, y=athlete_st.gender.value_counts().values, 
                        labels={'x': 'Gender', 'y': 'Count'}, title="Athlete Gender in Olympic")
    gender_ath.update_layout(bargap=0.7, width=800, yaxis=dict(showgrid=False))
    st.plotly_chart(gender_ath)
    
    activeness_ath = px.bar(athlete_st.current.value_counts(), x=athlete_st.current.value_counts().index, y=athlete_st.current.value_counts().values, 
                        labels={'x': 'Still Active', 'y': 'Count'}, title="Still Active as an Athlete")
    activeness_ath.update_layout(bargap=0.7, width=800, yaxis=dict(showgrid=False))
    st.plotly_chart(activeness_ath)
    
    height_ath = px.box(athlete_st[athlete_st['height']!=0.0], x="height", labels={'x': 'Height', 'y': 'Count'}, title="Athlete Height Distribution")
    height_ath.update_layout(bargap=0.7, width=800, yaxis=dict(showgrid=False))
    st.plotly_chart(height_ath)
    st.markdown(
    """
    <style>
    .centered-caption {
        text-align: center;
        color: white;
        font-size: 0.9rem;
        margin-top: -20px;  /* Adjust to bring it closer */
    }
    </style>
    <p class="centered-caption">The plot is adjusted for non zero height that is presence in the data</p>
    """,
    unsafe_allow_html=True
    )

    weight_ath = px.box(athlete_st[athlete_st['weight']!=0.0], x="weight", title="Athlete Weight Distribution")
    weight_ath.update_layout(bargap=0.7, width=800, yaxis=dict(showgrid=False))
    st.plotly_chart(weight_ath)
    st.markdown(
    """
    <style>
    .centered-caption {
        text-align: center;
        color: white;
        font-size: 0.9rem;
        margin-top: -20px;  /* Adjust to bring it closer */
    }
    </style>
    <p class="centered-caption">The plot is adjusted for non zero weight that is presence in the data</p>
    """,
    unsafe_allow_html=True
    )
     
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
