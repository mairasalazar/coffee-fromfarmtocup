import streamlit as st
import tableauserverclient as TSC
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Additional Insights",
    page_icon="☕",
    layout="wide")

st.header("""Coffee Journey: Additional Insights""")
st.subheader("""There are so many more things to discover and explore about coffee! Although we couldn't fit all our insights in our project, here we present some more opportunities to discover why and how the choices we make about coffee matter.""") 


st.write("If you are looking for the home of the overall best coffee according to the Coffee Quality Institute, you can't go wrong with Ethiopian coffee. Curiously enough, it is in this same country that most type 2 defects are found. ")
st.write("Type 2 defects are subtle defects that can only be detected through tasting, and include staleness, over-fermentation and rancidness. Type One defects, meanwhile, are more obvious, as they can be perceived through visual inspection. These defects include black beans, insect-damaged or fungus-damaged beans, etc.")
st.write("What about Brazil, the largest coffee exporter in the world? In this ranking, it doesn't look or taste so good. Maybe it has something to do with its average lower altitude than some of the other producing countries? It does seem that altitude influences coffee profile, and although studies are not definitive and many factors interact to make good coffee, [this study](https://pubmed.ncbi.nlm.nih.gov/29433216/) indicates that sucrose content may be affected by altitude.")
        
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/CleanVisualizations/Characteristics' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1200, height=790
)

st.write("""Now, if you are interested in knowing if your coffee comes from a country with a lot of deforestation, here is a graph for you. Coffee is not one of the main drivers for deforestation, but it does have an impact.
         The EUropean Union will implement the The European Deforestation Regulation in December 2024, which will require companies to prove that products like coffee are[ not linked with deforestation](https://apnews.com/article/vietnam-coffee-deforestation-eu-20e3fac82a42beb38013980fa7a760e6).
         This graph looks at the rate of tree cover loss, the percentage of certified coffee over all produced coffee in a country, and total production. There seems to be no relation between certification and deforestation, but given coffee's relatively small role in deforestation, that is to be expected. If you are looking for the home of the overall best coffee according to the Coffee Quality Institute, you can't go wrong with Ethiopian coffee. Curiously enough, it is in this same country that most type 2 defects are found. 
""")
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/CertificationDeforestation/Deforestation' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1200, height=790
)

st.write("""In case you are curious, this is how big exporters rank in terms of forest area.""")
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/CleanVisualizations/ExportsVsForestArea' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1200, height=790
)

st.write("""This brings us to our final visualization, on a more personal level. In many cultures, annedoctally, there seems to be a correlation between coffee and tobacco consumption. Is that really the case? And is it a cultural correlation? case you are curious, this is how big exporters rank in terms of forest area.
         This graph shows us that it seems there isn't a correlation when you account for the whole world, however in some regions, the combo coffee+cigarrete is more prevalent - especially in Europe!""")
components.html(
    f"""<script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/romanrodriguezperez3440ff744c/views/CleanVisualizations/Coffee-TobaccoConsumptionCorr' width='1024' height='808' hide-tabs toolbar='bottom' ></tableau-viz>""",
    width=1200, height=790
)
