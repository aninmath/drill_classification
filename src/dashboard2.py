# drill_classifier/dashboard.py

import streamlit as st
import pandas as pd
from main import chain  # Import the reusable chain

st.title("Drill Classification Dashboard")
drill_desc = st.text_area('write the drill description here', height= 200)


if st.button('Check drill type'):
    text = drill_desc
    result = chain.invoke({'text': text})
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('Is this a drill?')
        st.success(result.drill_or_not)
    
    with col2:
        st.markdown('drill type')

        if result.drill_or_not == 'Drill':
            st.info(result.drill_type)
        else:
            st.info('N/A')

