import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# streamlit_app.py

import streamlit as st
import tableauserverclient as TSC


# Set up connection.
tableau_auth = TSC.PersonalAccessTokenAuth(
    st.secrets["tableau"]["token_name"],
    st.secrets["tableau"]["token_secret"],
    st.secrets["tableau"]["site_id"],
)
server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)
print(server)

# Get various data.
# Explore the tableauserverclient library for more options.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def fetch_workbooks_and_views():
    with server.auth.sign_in(tableau_auth):
        workbooks_data = {}
        workbooks, pagination_item = server.workbooks.get()

        for workbook in workbooks:
            server.workbooks.populate_views(workbook)
            views = workbook.views
            workbooks_data[workbook.name] = views
        
        return workbooks_data
    
workbooks_data = fetch_workbooks_and_views()
print(workbooks_data)
workbook_names = list(workbooks_data.keys())

# User selects a workbook.
st.sidebar.subheader("Select Workbook")
selected_workbook_name = st.sidebar.selectbox("Workbook", workbook_names)

# Get views for the selected workbook.
selected_views = workbooks_data['']
view_names = [view.name for view in selected_views]

# User selects a view.
st.sidebar.subheader("Select View")
selected_view_name = st.sidebar.selectbox("View", view_names)

# Fetch selected view details.
@st.cache_data(ttl=600)
def fetch_view_details(selected_workbook_name, selected_view_name):
    with server.auth.sign_in(tableau_auth):
        selected_view = next(
            view for view in workbooks_data[selected_workbook_name] if view.name == selected_view_name
        )
        
        server.views.populate_image(selected_view)
        server.views.populate_csv(selected_view)

        view_image = selected_view.image
        view_csv = b"".join(selected_view.csv).decode("utf-8")
        
        return view_image, view_csv

view_image, view_csv = fetch_view_details(selected_workbook_name, selected_view_name)

# Display the results.
st.subheader("📓 Workbooks")
st.write("Available workbooks:", ", ".join(workbook_names))

st.subheader("👁️ Views")
st.write(f"Workbook *{selected_workbook_name}* has the following views:", ", ".join(view_names))

st.subheader("🖼️ Image")
st.write(f"Here's what view *{selected_view_name}* looks like:")
st.image(view_image, width=600)
