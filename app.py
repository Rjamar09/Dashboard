import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image


st.title("Virat kholi 71 Centuries Analysis")
image = Image.open('Virat-Kohli-T20I-Century.webp')
st.image(image, caption='Virat Kholi')


df=pd.read_csv("71 Centuries of Virat Kohli.csv")
df.drop('Unnamed: 14',axis=1,inplace=True)
df['Strike Rate'] = df['Strike Rate'].fillna(0)
st.dataframe(df)

df['year']=pd.to_datetime(df['Date'])
df['year']=df['year'].dt.year
df['Date']=df['Date'].replace('08-09-2022','09-08-2022')
st.header("Virat kholi highest Century Scores")
a=df.groupby(['Against','year'],as_index=False)['Score'].max().sort_values(by='Score',ascending=False).reset_index(drop=True).head()
st.table(a)
st.markdown("Kohli Scores Highest (254) Runs Against South Africa in the year 2019 and against Sri Lanka in 2017")
st.header("Virat kholi Lowest Century Scores")
x=df.groupby(['Against','year'],as_index=False)['Score'].min().sort_values(by='Score',ascending=True).reset_index(drop=True).head()
st.table(x)
st.markdown("Kohli Scores Lowest(100) Runs Against Bangladesh in the year 2011 and against Australia in the year 2013")

fig=px.line(df,x='Date',y='Score',markers=True,template='simple_white',title='<b>Kohli\'s hundreds over time</b>')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig)

fig=px.bar(df.groupby('Against',as_index=False)['Score'].count().sort_values(by='Score',ascending=False).reset_index(drop=True),x='Against',y='Score',color='Against',text='Score',labels={'Score':'Count'},template='simple_white',title='<b>Kohli\'s Centuries Against Opponents</b>')
fig.update_layout(title_x=0.5)
fig.show()
st.plotly_chart(fig)
fig=px.bar(df.groupby(['Against','H/A'],as_index=False)['Score'].count().sort_values(by='Score',ascending=False).reset_index(drop=True),x='Against',y='Score',color='H/A',text='Score',labels={'Score':'Count'},template='simple_white',title='<b>Kohli\'s Centuries Analysis by Venue Home/Away</b>')
fig.update_layout(title_x=0.5,legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1))
st.plotly_chart(fig)


st.markdown("From the Above graph, Virat Kohli Scores more Centuries against Australia(15) , Srilanka(13) and West Indies(11).")

st.markdown("He Score (9) centuries from Away ground against Austalia and (8) Centuries against Srilanka.")

st.markdown("In Home Ground he Scores (6) centuries against Australia, west indies and New Zealand.")

fig=px.bar(df.groupby('year',as_index=False)['Score'].count(),x='year',y='Score',text='Score',labels={'Score':'Count'},color_discrete_sequence=['lightgreen'],template='seaborn',title='<b>Virat Kohli\'s hundreds year-by-year</b>')
fig.update_layout(title_x=0.5)
fig.show()
st.plotly_chart(fig)


fig=px.bar(df.groupby(['Against','Out/Not Out'],as_index=False)['Score'].count(),x='Against',y='Score',color='Out/Not Out',color_discrete_sequence=['olive',' #F8766D'],text='Score',labels={'Out/Not Out':'result','Score':'Count'},template='ggplot2',title='<b>Whether Virat Out or Not Out when he Hit a Century</b>')
fig.update_layout(title_x=0.5,legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1))
fig.show()
st.plotly_chart(fig)
fig=px.pie(df.groupby('Out/Not Out',as_index=False)['Score'].count().sort_values(by='Score',ascending=False).reset_index(drop=True),names='Out/Not Out',values='Score',color='Out/Not Out',color_discrete_sequence=[' #F8766D','olive'],labels={'Out/Not Out':'result','Score':'Count'},template='seaborn',hole=0.5,title='<b>Out or Not Out')
fig.update_layout(title_x=0.5,legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1))
fig.show()
st.plotly_chart(fig)
st.markdown("Out of 71 Centuries, Kohli outs 51 times")

st.markdown("He outs mostly for Australia i.e 13 times")

fig=px.sunburst(df.groupby(['Format','Against','Result'],as_index=False)['Score'].count(),path=['Format','Result','Against'],values='Score',color='Result',title='<b>Match results when kohli scores centuries against opponents')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig)


fig=px.pie(df.groupby(['Batting Order'],as_index=False)['Score'].count(),values = 'Score', names = 'Batting Order', hole = 0.4,template='seaborn',labels={'Score':'Count'},title='<b>Virat\'s Centuries based on Batting Order')
fig.update_layout(title_x=0.5,legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1))
st.plotly_chart(fig)


a=df
a['Date']=pd.to_datetime(a['Date'])
a.sort_values(by='Date',ascending=True,inplace=True)
a['Century']=[i for i in range(1,72)]
fig=px.line(a,x='Date',y='Century',markers=True,template='plotly_dark',color_discrete_sequence=['magenta'],title='<b>Total Centuries of kohli over time ')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig)


fig=px.choropleth(df.groupby('Against',as_index=False)['Score'].count(),locations='Against',locationmode='country names',color='Score',labels={'Score':'Count'},hover_data=['Score'],template='plotly',title='<b>Map View of Kohli\'s Centuries against opponents')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig)