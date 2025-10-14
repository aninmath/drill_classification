# drill_classifier/dashboard.py

import streamlit as st
import pandas as pd
from main import chain  # Import the reusable chain

st.title("Drill Classification Dashboard")
uploaded_file = st.file_uploader("Upload Drill Log CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    results = []
    for _, row in df.iterrows():
        text = {row['Description']}
        result = chain.invoke({'text': text})
        results.append({
            'Serial No': row['Serial No'],
            'Drill or Not': result.drill_or_not,
            'Drill Type': result.drill_type if result.drill_or_not == 'Drill' else 'N/A'
        })
    st.dataframe(pd.DataFrame(results))