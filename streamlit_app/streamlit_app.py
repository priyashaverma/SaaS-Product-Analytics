

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("saas_customer_data.csv", parse_dates=['signup_date'])

st.title("SaaS Product Analytics Dashboard")


st.header("Key Metrics")
col1, col2, col3 = st.columns(3)

churn_rate = df['churned'].mean()
total_users = len(df)
total_revenue = df['monthly_revenue'].sum()

col1.metric("Total Users", total_users)
col2.metric("Total Monthly Revenue", f"${total_revenue}")
col3.metric("Churn Rate", f"{churn_rate:.2%}")


st.header("Plan Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(x='plan', data=df, ax=ax1)
st.pyplot(fig1)

# Sessions vs Churn
st.header("Sessions vs Churn")
fig2, ax2 = plt.subplots()
sns.boxplot(x='churned', y='sessions_last_month', data=df, ax=ax2)
st.pyplot(fig2)
