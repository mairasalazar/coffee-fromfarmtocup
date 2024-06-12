# streamlit_app.py

import streamlit as st
import tableauserverclient as TSC
import streamlit.components.v1 as components
import re

# Set up connection.
tableau_auth = TSC.PersonalAccessTokenAuth(
    st.secrets["tableau"]["token_name"],
    st.secrets["tableau"]["token_secret"],
    st.secrets["tableau"]["site_id"],
)
server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)

# Cache function to fetch workbooks and their views.
def fetch_workbooks_and_views():
    with server.auth.sign_in(tableau_auth):
        workbooks_data = {}
        workbooks, pagination_item = server.workbooks.get()
        
        workbook = workbooks[27]
        server.workbooks.populate_views(workbook)
        views = workbook.views
        workbooks_data[workbook.content_url] = views
        
        return workbooks_data

workbooks_data = fetch_workbooks_and_views()
workbook_names = list(workbooks_data.keys())

# User selects a workbook.
st.sidebar.subheader("Select Workbook")
selected_workbook_name = st.sidebar.selectbox("Workbook", workbook_names)

# Get views for the selected workbook.
selected_views = workbooks_data[workbook_names[0]]
view_names = [view.name for view in selected_views]

# User selects a view.
st.sidebar.subheader("Select View")
selected_view_name = st.sidebar.selectbox("View", view_names)

# Get the selected view item.
selected_view = next(
    view for view in workbooks_data[selected_workbook_name] if view.name == selected_view_name
)
match = re.search(r"contentUrl='[^']+/([^']+)'", str(selected_view))
comparison_view = match.group(1)

# Create the Tableau embed URL.

# Embed the interactive Tableau view.
st.subheader(f"Interactive View: {selected_view_name}")
st.write("""THis is a dashboard""")
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/{workbook_names[0]}/{comparison_view}' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=1100
)

