import altair as alt
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# intro info 

PLL_df = pd.read_csv('pll-team-stats22.csv')
st.set_page_config(page_title="Dark Mode Example", layout="wide")


st.title("Premier Lacrosse League Statistics")
st.subheader("Lillian Bowling")
    
with st.expander('About the Premier Lacrosse League'):
 st.write('In 2022 the Waterdog Lacrosse Club held the championship title. Reviewing regular season goal statistics is important to show how a team preforms, and why / if the team is champion material. The PLL was founded in 2018 and has been rapidly growing since. Recenly, in 2024 the Womens Lacrosse League (WLL) was founded and will debut in 2025 at the PLLs 2025 championship searies in February')


# team tabs

tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['HOME', 'Atlas','Archers', 'Cannons', 'Chaos', 'Chrome', 'Redwoods', 'Waterdogs', 'Whipsnakes'])


with tab0:
  data = {
    'LAT': [39.3335, 35.2185, 32.7731, 42.091, 39.6825, 42.68, 40.033, 40.4837],
    'LON': [-76.6209, -80.8286, -117.1836, -71.264, -104.9635, -73.83, -75.3367, -111.9795],
    'CITY': ['Baltimore, MA', 'Charlotte, NC', 'San Diego, California', 'Boston, MD', 'Albany, NY', 'Denver, CO', 'Philadelphia, PA', 'Salt Lake City, UT']
      }

  df = pd.DataFrame(data)
  st.write("Home City Stadiums", df)
  st.map(df)


  # bar chart 
  st.title("Goal Statistics of the 2022 Season")

  Teams = ['ATL', 'ARC', 'CAN', 'CHA', 'CHR', 'RED', 'WAT', 'WHP']
  Goals = [123, 115, 109, 97, 117, 105, 122, 111]

  
  fig1, ax1 = plt.subplots(figsize=(5, 4))


  bars = ax1.bar(Teams, Goals, color='Red')

 
  for bar in bars:
      yval = bar.get_height()
      ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
              round(yval, 2), ha='center', va='center', color='white')

 
  ax1.set_xlabel('Team')
  ax1.set_ylabel('Goals')
  ax1.set_title('Goals Per Team in 2022')


  st.pyplot(fig1)

  # Line Chart

  labels = ["ARC", "WAT", "ATL", "CHR", "WHP", "RED", "CAN", "CHA"]
  values = [75, 73, 72, 70, 59, 55, 55, 58]

  
  fig2, ax2 = plt.subplots()


  ax2.plot(labels, values, marker='o', color='red', linestyle='-', label='Assists')

  
  for i, value in enumerate(values):
      ax2.text(labels[i], value, str(value), ha='center', va='center', fontsize=4, fontweight='bold', color='white')

 
  ax2.set_title("Assists Per Team")
  ax2.set_xlabel("Teams")
  ax2.set_ylabel("Assists")
  ax2.legend()

  
  st.pyplot(fig2)


with tab1:
  filtered1 = PLL_df[PLL_df['Team'] == 'Atlas']
  st.write("All Statistics Recorded", filtered1)

  data = {
    'LAT': [42.68],
    'LON': [-73.83],
    'CITY': ['Albany, NY']
      }

  df = pd.DataFrame(data)
  st.write("Casey Stadium", df)
  st.map(df)


  st.title("Shots on Goal vs. Shots")
  TYPE = ['Shot', 'Shot on Goal']
  AMOUNT = [395, 252]

  fig1, ax1 = plt.subplots(figsize=(5, 4))

  bars = ax1.bar(TYPE, AMOUNT, color='Red')

  for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
                 round(yval, 2), ha='center', va='center', color='white')

  ax1.set_xlabel('TYPE')
  ax1.set_ylabel('AMOUNT')
  ax1.set_title('Shots on Goal vs. Shots')

  st.pyplot(fig1)



with tab2:
    filtered2 = PLL_df[PLL_df['Team'] == 'Archers']
    st.write("All Statistics Recorded", filtered2)

    data = {
    'LAT': [40.4837],
    'LON': [-111.9795],
    'CITY': ['Salt Lake City, UT']
      }

    df = pd.DataFrame(data)
    st.write("Zions Bank Stadium", df)
    st.map(df)

    st.title("Shots on Goal vs. Shots")
    TYPE = ['Shot', 'Shot on Goal']
    AMOUNT = [386, 268]

    fig1, ax1 = plt.subplots(figsize=(5, 4))

    bars = ax1.bar(TYPE, AMOUNT, color='Red')

    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
                 round(yval, 2), ha='center', va='center', color='white')

    ax1.set_xlabel('TYPE')
    ax1.set_ylabel('AMOUNT')
    ax1.set_title('Shots on Goal vs. Shots')

    st.pyplot(fig1)


with tab3:
  filtered3 = PLL_df[PLL_df['Team'] == 'Cannons']
  st.write("All Statistics Recorded", filtered3)

  data = {
    'LAT': [42.091],
    'LON': [-71.264],
    'CITY': ['Boston, MD']
      }

  df = pd.DataFrame(data)
  st.write("Home Stadium, Harvard Stadium", df)
  st.map(df)

  st.title("Shots on Goal vs. Shots")
  TYPE = ['Shot', 'Shot on Goal']
  AMOUNT = [394, 255]

  fig1, ax1 = plt.subplots(figsize=(5, 4))

  bars = ax1.bar(TYPE, AMOUNT, color='Red')

  for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
                 round(yval, 2), ha='center', va='center', color='white')

  ax1.set_xlabel('TYPE')
  ax1.set_ylabel('AMOUNT')
  ax1.set_title('Shots on Goal vs. Shots')

  st.pyplot(fig1)


with tab4:

  filtered4 = PLL_df[PLL_df['Team'] == 'Chaos']
  st.write("All Statistics Recorded", filtered4)


  data = {
    'LAT': [35.218580],
    'LON': [-80.8286],
    'CITY': ['Charlotte, NC']
      }

  df = pd.DataFrame(data)
  st.write("Home Stadium, American Legion Memorial Stadium", df)
  st.map(df)


  st.title("Shots on Goal vs. Shots")
  TYPE = ['Shot', 'Shot on Goal']
  AMOUNT = [316, 205]

  fig1, ax1 = plt.subplots(figsize=(5, 4))

  bars = ax1.bar(TYPE, AMOUNT, color='Red')

  for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
                 round(yval, 2), ha='center', va='center', color='white')

  ax1.set_xlabel('TYPE')
  ax1.set_ylabel('AMOUNT')
  ax1.set_title('Shots on Goal vs. Shots')

  st.pyplot(fig1)



with tab5:
  filtered5 = PLL_df[PLL_df['Team'] == 'Chrome']
  st.write("All Statistics Recorded", filtered5)

  data = {
    'LAT': [39.6825],
    'LON': [-104.9635],
    'CITY': ['Denver, CO']
      }

  df = pd.DataFrame(data)
  st.write("Home Stadium, Peter Barton Stadium", df)
  st.map(df)

  st.title("Shots on Goal vs. Shots")
  TYPE = ['Shot', 'Shot on Goal']
  AMOUNT = [371, 245]

  fig1, ax1 = plt.subplots(figsize=(5, 4))

  bars = ax1.bar(TYPE, AMOUNT, color='Red')

  for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
                 round(yval, 2), ha='center', va='center', color='white')

  ax1.set_xlabel('TYPE')
  ax1.set_ylabel('AMOUNT')
  ax1.set_title('Shots on Goal vs. Shots')

  st.pyplot(fig1)


with tab6:
  filtered6 = PLL_df[PLL_df['Team'] == 'Redwoods']
  st.write("All Statistics Recorded", filtered6)

  data = {
    'LAT': [32.7731],
    'LON': [-117.1836],
    'CITY': ['San Diego, CA']
      }

  df = pd.DataFrame(data)
  st.write("Home Stadium, Torero Stadium", df)
  st.map(df)


  st.title("Shots on Goal vs. Shots")
  TYPE = ['Shot', 'Shot on Goal']
  AMOUNT = [395, 252]

  fig1, ax1 = plt.subplots(figsize=(5, 4))

  bars = ax1.bar(TYPE, AMOUNT, color='Red')

  for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
                 round(yval, 2), ha='center', va='center', color='white')

  ax1.set_xlabel('TYPE')
  ax1.set_ylabel('AMOUNT')
  ax1.set_title('Shots on Goal vs. Shots')

  
  st.pyplot(fig1)


with tab7:
  filtered7 = PLL_df[PLL_df['Team'] == 'Waterdogs']
  st.write("All Statistics Recorded", filtered7)

  data = {
    'LAT': [40.033],
    'LON': [-75.3367],
    'CITY': ['Philadelphia, PA']
      }

  df = pd.DataFrame(data)
  st.write("Home Stadium, Villanova Stadium", df)
  st.map(df)

  st.title("Shots on Goal vs. Shots")
  TYPE = ['Shot', 'Shot on Goal']
  AMOUNT = [440, 275]

  fig1, ax1 = plt.subplots(figsize=(5, 4))

  bars = ax1.bar(TYPE, AMOUNT, color='Red')

  for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
                 round(yval, 2), ha='center', va='center', color='white')

  ax1.set_xlabel('TYPE')
  ax1.set_ylabel('AMOUNT')
  ax1.set_title('Shots on Goal vs. Shots')

  st.pyplot(fig1)

with tab8: 
  filtered8 = PLL_df[PLL_df['Team'] == 'Whipsnakes']
  st.write("All Statistics Recorded", filtered8)

  data = {
    'LAT': [39.3335],
    'LON': [-76.6209],
    'CITY': ['Baltimore, MA']
      }

  df = pd.DataFrame(data)
  st.write("Home Stadium, Homewood Field", df)
  st.map(df)


  st.title("Shots on Goal vs. Shots")
  TYPE = ['Shot', 'Shot on Goal']
  AMOUNT = [395, 252]

  fig1, ax1 = plt.subplots(figsize=(5, 4))


  bars = ax1.bar(TYPE, AMOUNT, color='Red')


  for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval / 2,
                 round(yval, 2), ha='center', va='center', color='white')

  ax1.set_xlabel('TYPE')
  ax1.set_ylabel('AMOUNT')
  ax1.set_title('Shots on Goal vs. Shots')

 
  st.pyplot(fig1)




