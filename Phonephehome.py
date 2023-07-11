#
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# MySQL connection details
host = '127.0.0.1'
user = 'root'
password = 'root123456789'
port = 3307
database = 'mydt7'

# Create the engine for database connection
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
#

# Add widgets to the sidebar
st.sidebar.title("PhonePhe Data")
st.sidebar.text("Data Visualization via Indian-Map")

# Example of adding a selectbox - 1
options0 = ["aggregated_transaction", "aggregated_users", "map_transactions", "map_users", "top_transactions", "top_users"]
selected_option0 = st.sidebar.selectbox("Select an Option", options0, key="option1")

### - 01

if selected_option0 == "aggregated_transaction":
    Quarter = st.selectbox("Select the quarter:", [1, 2, 3, 4]) # Get user input using dropdowns #
    Year = st.selectbox("Select the year:", [2018, 2019, 2020, 2021, 2022])
    Transaction_type = st.selectbox("Select the Ttype:", ['Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services', 'Others'])
    
    query1 = """SELECT State, Year, Quarter, Transaction_type, MAX(Transaction_count) AS Max_Count,MAX(Transaction_amount) AS Max_Amount 
                FROM mydt7.aggregated_transaction 
                WHERE Quarter = %s AND Transaction_type = %s AND Year = %s 
                GROUP BY State, Year, Quarter, Transaction_type;"""
    
    df = pd.read_sql(query1, con=engine, params=(Quarter, Transaction_type, Year)) # Fetch data from the SQL table into a DataFrame
    #
    fig = px.choropleth(
        df,
        title='Indian Map - Aggregated_Transaction - Financial Services',
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Max_Count',
        hover_data=['Max_Amount'],
        color_continuous_scale='portland'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=800, width=800)
    st.plotly_chart(fig)
    st.write(df)
    #
    # Bar Chart #
    st.bar_chart(df.set_index('State')['Max_Amount'])
    #


### - 02

if selected_option0 == "aggregated_users":
    Quarter = st.selectbox("Select the quarter:", [1, 2, 3, 4]) # Get user input using dropdowns #
    Year = st.selectbox("Select the year:", [2018, 2019, 2020, 2021, 2022])
    Device_Brands = st.selectbox("Select the M-Brand:", ['Xiaomi', 'Samsung', 'Vivo', 'Oppo', 'OnePlus', 'Realme', 'Apple', 'Motorola', 'Lenovo', 'Huawei', 'Others'])
    
    query2 = """SELECT State, Year, Quarter, Device_Brands, Counts, Percentage
                FROM mydt7.aggregated_users
                WHERE Quarter = %s AND Year = %s AND Device_Brands = %s
                GROUP BY State, Year, Quarter, Counts, Percentage;"""
    
    df = pd.read_sql(query2, con=engine, params=(Quarter, Year,Device_Brands)) # Fetch data from the SQL table into a DataFrame
    #
    fig = px.choropleth(
        df,
        title='Indian Map - Aggregated_Users - Financial Services',
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Counts',
        hover_data=['Counts','Percentage'],
        color_continuous_scale='portland'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=800, width=800)
    st.plotly_chart(fig)
    st.write(df)
    #
    # Bar Chart #
    st.bar_chart(df.set_index('State')['Counts'])
    #
#

### - 03

if selected_option0 == "map_transactions":
    Quarter = st.selectbox("Select the quarter:", [1, 2, 3, 4]) # Get user input using dropdowns #
    Year = st.selectbox("Select the year:", [2018, 2019, 2020, 2021, 2022])
    
    query3 = """SELECT State, Year, Quarter, MAX(Counts) AS Max_Count, MAX(Amount) AS Max_Amount
                FROM mydt7.map_transactions
                WHERE Quarter = %s AND Year = %s
                GROUP BY State, Year, Quarter;"""
    
    df = pd.read_sql(query3, con=engine, params=(Quarter, Year)) # Fetch data from the SQL table into a DataFrame
    #
    fig = px.choropleth(
        df,
        title='Indian Map - Map_Transactions - Financial Services',
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Max_Count',
        hover_data=['Max_Amount'],
        color_continuous_scale='portland'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=800, width=800)
    st.plotly_chart(fig)
    st.write(df)
    #
    # Bar Chart #
    st.bar_chart(df.set_index('State')['Max_Amount'])
    #
#

### - 04

if selected_option0 == "map_users":
    Quarter = st.selectbox("Select the quarter:", [1, 2, 3, 4]) # Get user input using dropdowns #
    Year = st.selectbox("Select the year:", [2018, 2019, 2020, 2021, 2022])
    
    query4 = """SELECT State, Year, Quarter, District,MAX(RegisteredUsers) AS Max_Reg
                FROM mydt7.map_users
                WHERE Quarter = %s AND Year = %s
                GROUP BY State, Year, Quarter, District;"""
    
    df = pd.read_sql(query4, con=engine, params=(Quarter, Year)) # Fetch data from the SQL table into a DataFrame
    #
    fig = px.choropleth(
        df,
        title='Indian Map - Map_Users - Financial Services',
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Max_Reg',
        #hover_data=['Max_Amount'],
        color_continuous_scale='portland'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=800, width=800)
    st.plotly_chart(fig)
    st.write(df)
    #
    # Bar Chart #
    st.bar_chart(df.set_index('State')['Max_Reg'])
    #
#

### - 05

if selected_option0 == "top_transactions":
    Quarter = st.selectbox("Select the quarter:", [1, 2, 3, 4]) # Get user input using dropdowns #
    Year = st.selectbox("Select the year:", [2018, 2019, 2020, 2021, 2022])
    
    query5 = """SELECT State, Year, Quarter, MAX(Count) AS Max_Count,MAX(Amount) AS Max_Amount
                FROM mydt7.top_transactions
                WHERE Quarter = %s AND Year = %s
                GROUP BY State, Year, Quarter;"""
    
    df = pd.read_sql(query5, con=engine, params=(Quarter, Year)) # Fetch data from the SQL table into a DataFrame
    #
    fig = px.choropleth(
        df,
        title='Indian Map - Top_Transactions - Financial Services',
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Max_Count',
        hover_data=['Max_Amount'],
        color_continuous_scale='portland'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=800, width=800)
    st.plotly_chart(fig)
    st.write(df)
    #
    # Bar Chart #
    st.bar_chart(df.set_index('State')['Max_Amount'])


### - 06

if selected_option0 == "top_users":
    Quarter = st.selectbox("Select the quarter:", [1, 2, 3, 4]) # Get user input using dropdowns #
    Year = st.selectbox("Select the year:", [2018, 2019, 2020, 2021, 2022])
    
    query6 = """SELECT State, Year, Quarter, MAX(Registered_user) AS Max_Registered_user
                FROM mydt7.top_users
                WHERE Quarter = %s AND Year = %s
                GROUP BY State, Year;"""
    
    df = pd.read_sql(query6, con=engine, params=(Quarter, Year)) # Fetch data from the SQL table into a DataFrame
    #
    fig = px.choropleth(
        df,
        title='Indian Map - Top_Users - Financial Services',
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Max_Registered_user',
        #hover_data=['Max_Amount'],
        color_continuous_scale='portland'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=800, width=800)
    st.plotly_chart(fig)
    st.write(df)
    #
    # Bar Chart #
    st.bar_chart(df.set_index('State')['Max_Registered_user'])
    #
### - END - ###