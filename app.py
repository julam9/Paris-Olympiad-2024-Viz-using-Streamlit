import pandas as pd 
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go

medals_st = pd.read_csv('data/medals_total.csv')
coach_st = pd.read_csv('data_clean/coach_clean.csv')
medallist_st = pd.read_csv('data_clean/medallist_clean.csv') 
athlete_st = pd.read_csv('data_clean/athlete_data.csv')
medals_intro = medals_st[:5]

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
    """
    )
    
    st.subheader("Olympics Overall Statistics")
    st.markdown(f"""
    <div style="text-align: center;">
        <h1 style="font-size: 60px;">{medals_st.shape[0]}</h1>
        <p>Countries particicapting in this year Olympic</p>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown(f"""
    <div style="text-align: center;">
        <h1 style="font-size: 60px;">{medals_st.Total.sum()}</h1>
        <p>Medals contested in this Olympic with distribution as this : </p>
    </div>
    """, unsafe_allow_html=True)
    
    gold_medal_total = medals_st['Gold Medal'].sum()
    silver_medal_total = medals_st['Silver Medal'].sum() 
    bronze_medal_total = medals_st['Bronze Medal'].sum()
    total_medal_dist = px.pie(values=[gold_medal_total, silver_medal_total, bronze_medal_total], names=['Gold Medal', 'Silver Medal', 'Bronze Medal'])
    st.plotly_chart(total_medal_dist)

    fig_medal = go.Figure()
    # Add bars for each medal type
    fig_medal.add_trace(go.Bar(
        x=medals_intro['country_code'],
        y=medals_intro['Gold Medal'],
        name='Gold Medal',
        marker_color='gold'
    ))
    fig_medal.add_trace(go.Bar(
        x=medals_intro['country_code'],
        y=medals_intro['Silver Medal'],
        name='Silver Medal',
        marker_color='silver'
    ))
    fig_medal.add_trace(go.Bar(
        x=medals_intro['country_code'],
        y=medals_intro['Bronze Medal'],
        name='Bronze Medal',
        marker_color='#cd7f32'  # Bronze color
    ))
    # Update layout bar chart
    fig_medal.update_layout(
        barmode='group',
        title='Medals Count by Country',
        xaxis_title='Country Code',
        yaxis_title='Number of Medals'
    )
    # Display the plot 
    st.plotly_chart(fig_medal)
    
    st.markdown(f"""
    <div style="text-align: center;">
        <h1 style="font-size: 60px;">{athlete_st.disciplines.nunique()}</h1>
        <p>Sports discipline  contested in this Olympic</p>
    </div>
    """, unsafe_allow_html=True)
    
    # to let the viewers see the others
    st.markdown( 
    """ 
    If you want to know more details about Paris Olympic, you can choose the category 👈 
    """)
    

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
    
    height_ath = px.histogram(athlete_st[athlete_st['height']!=0.0], x="height", nbins=20, title="Athlete Height Distribution")
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

    weight_ath = px.histogram(athlete_st[athlete_st['weight']!=0.0], x="weight", nbins=20, title="Athlete Weight Distribution")
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

    age_ath = px.histogram(athlete_st, x="age", nbins=20, title="Athlete Age Distribution")
    st.plotly_chart(age_ath)
    
    nationality_ath = px.bar(athlete_st.same_country.value_counts(), x=athlete_st.same_country.value_counts().index, y=athlete_st.same_country.value_counts().values, 
                        labels={'x': 'Nationality and Country Represented Sameness', 'y': 'Count'}, title="Does athletes represent their own country?")
    nationality_ath.update_layout(bargap=0.7, width=800, yaxis=dict(showgrid=False))
    st.plotly_chart(nationality_ath)
    
    top_edu = athlete_st.education.value_counts(normalize=True)[:5].to_frame().reset_index()
    edu_ath = px.bar(top_edu, y='education', x='proportion',
                      orientation='h', labels={'y': 'Education of Athletes ', 'x': 'Count'}, title="Education background of athletes")
    st.plotly_chart(edu_ath)
    st.caption('Most athletes come from physical education background')
    
    top_occup = athlete_st.occupation.value_counts(normalize=True)[:5].to_frame().reset_index()
    occup_ath = px.bar(top_occup, y='occupation', x='proportion',
                      orientation='h', labels={'y': 'Occupation of Athletes ', 'x': 'Count'}, title="Occupation of athletes")
    st.plotly_chart(occup_ath)
    st.caption('Most athletes occupy as only athlete, there are also some athlete occupy as students')
    
    
    same_living_ath = px.bar(athlete_st.same_living.value_counts(), x=athlete_st.same_living.value_counts().index, y=athlete_st.same_living.value_counts().values, 
                        labels={'x': 'Home and Country Represented Sameness', 'y': 'Count'}, title="Does athletes stay at country they represent?")
    same_living_ath.update_layout(bargap=0.7, width=800, yaxis=dict(showgrid=False))
    st.plotly_chart(same_living_ath)
         
def coach():
    st.title("Coach in the Olympic 2024")
    st.markdown(f"""
    <div style="text-align: center;">
        <h1 style="font-size: 60px;">{coach_st.name.nunique()}</h1>
        <p>Coaches coaching in this event.</p>
    </div>
    """, unsafe_allow_html=True)
    
    gender_coach = px.bar(coach_st.gender.value_counts(), x=coach_st.gender.value_counts().index, y=coach_st.gender.value_counts().values,
                        labels={'x': 'Gender', 'y': 'Count'}, title="Coach Gender in Olympic")
    gender_coach.update_layout(bargap=0.7, width=800, yaxis=dict(showgrid=False))
    st.plotly_chart(gender_coach)
    st.caption("Same as athlete, the coaches dominated by male coach")
    
    func_coach = px.bar(coach_st.function.value_counts(), y=coach_st.function.value_counts().index, x=coach_st.function.value_counts().values,
                        orientation='h', labels={'x': 'Function', 'y': 'Count'}, title="Coach Function in Olympic")
    st.plotly_chart(func_coach)
    st.caption("Most of the coaches functioning as coach")
    
    country_coach = px.bar(coach_st.country.value_counts()[:5], y=coach_st.country.value_counts()[:5].index, x=coach_st.country.value_counts()[:5].values,
                        labels={'x': 'Count', 'y': 'Country'}, title="Top 5 Countries with most Coaches")
    country_coach.update_layout(bargap=0.7, width=800, yaxis=dict(showgrid=False))
    st.plotly_chart(country_coach)
    
    age_coach = px.histogram(coach_st[coach_st['age']!='Age unavaible'], x='age', nbins=20, title='Coaches Age Distribution')
    st.plotly_chart(age_coach)
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
    <p class="centered-caption">The plot is adjusted for the only avaible age in the data</p>
    """,
    unsafe_allow_html=True 
    )
    
    st.markdown(f"""
    <div style="text-align: center;">
        <h1 style="font-size: 60px;">{coach_st.disciplines.nunique()}</h1>
        <p>Sports discipline coached in this Olympic</p>
    </div>
    """, unsafe_allow_html=True)
    
page_names_to_funcs = {
    "General": intro,
    "Athlete": athlete,
    "Coach" : coach
}

demo_name = st.sidebar.selectbox("Choose a scope", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
