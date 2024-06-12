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
st.header("""Coffee Journey: From the farm to your cup""")
st.subheader("""In this project we will give insights into interesting facts that will raise awareness about economic factors of the coffee industry, as well as discuss certain preconceptions about coffee and lifestyle from a multinational perspective.""") 

st.write("""Starting, for a bit of context, we talk about coffee and tea. They have been historical competitors, dividing occidental and oriental societies, with some exceptions, for example, Turkey and the UK blurring the line. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/CoffeevsTeaConsumption' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1200, height=700
)
st.write("""Now, we’re going to proceed establishing a difference among producers and consumers of coffee. In the first half of the project, we are going to focus on the producer side and how their so-called ”economy of coffee” functions. To begin with, it is important to see how much difference in wealth is perceived between the main importers, on the left side and the main exporters on the right side. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/GDPpercapita' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=1100
)
st.write("""The sankey diagram represents the imports and exports between countries in 2022, with Brazil, Columbia and Vietnam being the biggest exporters (hover over these countries names while you say this) and US and Germany being the biggest importers (again hover over their names). Fun fact, there is almost a 50% chance that the coffee that you drink comes from Brazil! """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/Sankey' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=1200
)
st.write("""Our 2021 coffee map reveals a global coffee price rollercoaster! South Korea's cup averaged a whopping 7.71 dollars, while Albania offered the cheapest at 1.17 dollars. This geographic price gap highlights how economics and culture brew different coffee experience worldwide. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/AveragePriceofaCupofCoffeeinthrWorld' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1200, height=700
)
st.write("""The production of coffee has changed significantly over the last 20 years. This bar graph represents how the production has changed from 2000/2001 to 2019/2020. As the dark blue bar shows in comparison to the thicker light blue bar, the production has increased and almost doubled over 20 years for almost all the countries except India and Mexico. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/CoffeeProd_Evolution' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=1100
)
st.write("""How does that translate to the real people involved in coffee production? The income of coffee growers differs substantially from the prices paid for coffee. To have a better idea of what that means within their specific cost of living, we compare the estimated income of a producer with the minimum wage and Big mac index in those countries. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/Dashboard1' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1800, height=1100
)
st.write("""Unfortunately, increasing certified coffee production is not the solution for everything. Less than half of the coffee produced as certified is actually sold as certified. The rest is sold as normal coffee, at lower prices and lower margins for producers. Colombia is the country that produces, proportionally, the most certified coffee, probably due to its high percentage of small growers. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/Comparison2' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=1100
)
st.write("""Here, the idea is to have a first overview of the reasons why people could want to stop drinking coffee; we’ll treat some of these deeper in other visualizations but we can already see which reason is true in green and which is just a myth, in red.  """)
st.write("""The bigger, the more commonly evoked the reason is, so here we see that many people stop drinking coffee for scientifically unproved reasons that they believe are true: anxiety and weight gain to name them. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/Factchecker' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=700
)
st.write("""This visualization deepens our word cloud that we saw before; we saw that many people stop drinking coffee to lose weight; but here, our graph shows first with the height of the yellow circles how much calories do coffee or the common additions we put in it actually represent. Then, the insight comes from linking it with the height of the brown circles, which shows us how many of the respondents drink coffee alone or with a sweetener, milk etc. Thus, it highlights that the real culprit in weight gain is not coffee in itself but what we put in it. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/WeightGain' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=1100
)
st.write("""Do coffee lover nations suffer from high anxiety rates? Our visualization explores this question, and interestingly, the data reveals no clear correlation between the two. This suggests a more nuanced relationship, potentially influenced by factors like genetics and social pressures. Further investigation is needed to untangle these complexities. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/Anxiety' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=1100
)
st.write("""Forget diamonds, coffee might be the real key to happiness! This dashboard suggests coffee consumption and happiness might be linked, but with some regional differences. The data explores the connection of coffee consumption per capita and the score that each country’s population rate their lives from 0 to 10. For hardcore coffee consumers such as Europe and the Americas, a cup of coffee might be a daily source of happiness.  Africa does not show a correlation, as happiness is highly affected by economic conditions. Meanwhile countries in Asia and Oceania are indifferent to this trend as well, probably because they opt for tea instead, (pause) except Lebanon. Maybe finding happiness in coffee is mostly a western habit. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/Consumption_HappinessCorrelation' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=2000
)
st.write("""This graph compares the top 10 coffee consumers with the bottom 10, in terms of heart disease deaths. While high coffee consumption might appear risky for the heart, the twist is smoking! (hover at Lebanon) The data suggests smoking habits play a big role, urging us to consider the bigger picture of health, while actually suggesting that consuming coffee might lead to a smaller risk of heart diseases. """)
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/V3_CleanVisualizations/CoffeeConsumption-HeartDiseaseDeathsRelationshipSmokingFilter' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1100, height=1100
)
st.write("""Thank you for your attention! We hope to have inspired you to go for a coffee today ;)""")
