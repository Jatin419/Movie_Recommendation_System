import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (update path if necessary)
@st.cache_data
def load_data():
    df = pd.read_csv("Blinkit_Sales.csv")  # Change filename as needed
    return df

data = load_data()

# Sidebar
st.sidebar.title("Blinkit Sales Analysis")
st.sidebar.write("Select options to explore the dataset")

# Show dataset
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Dataset Preview")
    st.write(data.head())
    
# Summary Statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Sales Over Time
st.subheader("Sales Over Time")
data['Date'] = pd.to_datetime(data['Date'])  # Ensure Date column is in datetime format
sales_over_time = data.groupby('Date')['Sales'].sum()
fig, ax = plt.subplots()
ax.plot(sales_over_time, marker='o', linestyle='-')
ax.set_xlabel("Date")
ax.set_ylabel("Total Sales")
ax.set_title("Sales Trend Over Time")
st.pyplot(fig)

# Sales by Category
if 'Category' in data.columns:
    st.subheader("Sales by Category")
    category_sales = data.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    sns.barplot(x=category_sales.values, y=category_sales.index, ax=ax)
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Category")
    ax.set_title("Sales by Category")
    st.pyplot(fig)

# Top Selling Products
if 'Product' in data.columns:
    st.subheader("Top 10 Selling Products")
    top_products = data.groupby('Product')['Sales'].sum().nlargest(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_products.values, y=top_products.index, ax=ax)
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Product")
    ax.set_title("Top 10 Selling Products")
    st.pyplot(fig)

st.sidebar.write("### Created by Jatin Choudhury")
