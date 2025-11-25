#Personal Fiance Tracker

#AI Auto-Categorization
#AI Monthly Summary Report

import streamlit as st
import pandas as pd

date_list = []
cate_list = []
amt_list = []
try: 
    with open("date.txt", "r") as f:
        for line in f:
            date_list.append(line.strip())
except FileNotFoundError:
    pass

try:
    with open("cate.txt", "r") as f:
        for line in f:
            cate_list.append(line.strip())
except FileNotFoundError:
    pass

try:
    with open("amt.txt", "r") as f:
        for line in f:
            amt_list.append(line.strip())
except FileNotFoundError:
    pass
    
# expense = {"Date": date_list,
#            "Category": cate_list,
#            "Amount": amt_list}

st.title("WELCOME TO YOUR PERSONAL AI FINANCE TRACKER")
st.subheader("List of task i can do for you")
st.write("I can categorize your expenses")
st.write("I can give you a summarize result of your expenses")

date = st.date_input("Enter date here:")

category = st.selectbox("Select category here:",
                        ["Food", "Transportation", "Education", "Entertainment", "Healthe & Fitness", "Others"])

amount = st.number_input("Enter amount here:", min_value=0.0)
        
if st.button("Done"):
    date_list.append(str(date))
    cate_list.append(category)
    amt_list.append(str(amount))
    
    with open("date.txt", "w") as f:
        for i in date_list:
            f.write(str(i) + "\n")
    
    with open("cate.txt", "w") as c:
        for i in cate_list:
            c.write(str(i) + "\n")
    
    with open("amt.txt", "w") as a:
        for i in amt_list:
            a.write(str(i) + "\n")

    st.success("Expense added successfully!")
        
if st.button("List of expenses"):
    st.success("Here are the list of expenses")

    expense = {"Date": date_list,
           "Category": cate_list,
           "Amount": amt_list}
    
    df = pd.DataFrame(expense)
    df.index = df.index + 1
    st.dataframe(df)

