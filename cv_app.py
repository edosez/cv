from pathlib import Path
import streamlit as st
from utils import txt, txt2

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV Edoardo Sezzi.pdf"
profile_pic = current_dir / "assets" / "foto.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Edoardo Sezzi"
PAGE_ICON = ":computer:"
NAME = "Edoardo Sezzi"

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file, encoding='utf-8') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#####################
# Navigation

st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">',
            unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <div class="container-fluid">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
          >
          <span class="navbar-toggler-icon"></span>
        </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" href="#edoardo-sezzi">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#work-experience">Work Experience</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#education">Education</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#skills">Skills</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#portfolio">Portfolio</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#hobby">Hobby</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)

# set streamlit header z-index to 0
st.markdown('''<style>.stApp header {
  z-index: 0;}</style>''',
  unsafe_allow_html=True)


# Remove anchor across all document
st.markdown("""
    <style>
    .css-15zrgzn {display: none}
    .css-eczf16 {display: none}
    .css-jn99sy {display: none}
    </style>
    """, unsafe_allow_html=True)

#####################
# Header
st.write('''
# Edoardo Sezzi
##### *Resume* 
''')
st.markdown('''## **Summary**''', unsafe_allow_html=True)
st.info('''
Experienced data professional with a diverse skillset, combining expertise in data analysis with software engineering practices. 
I actively engage in client conversations and pre-sales activities.
''')

with st.container():
    st.markdown('''
    ## **Info**
    ''')
    st.info('**+39-3341115868**', icon='📲')
    st.info('**edoardo.sezzi@hotmail.it**', icon='✉️')

  #####################
    st.markdown('<a href="https://www.linkedin.com/in/edoardo-sezzi"><img src="./app/static/linkedin_logo_blue.png" height="50" width="50" class="center">',
                unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/edosez"><img src="./app/static/github_logo.png" height="50" width="50" class="center">',
                unsafe_allow_html=True)
    st.download_button(label=':red[Download the CV]', data=PDFbyte, file_name='CV Edoardo Sezzi.pdf', mime='application/pdf', key=None, use_container_width=True)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#16A2CB;" /> """,
            unsafe_allow_html=True)

#####################
st.markdown('''
## **Work Experience**
''')
txt('#### Data, *Habacus SRL, Milan, Italy*', 
    '#### 2024-Present')
st.info('**Data, Analytics & Machine Learning**')
st.markdown('''
- Systematic data collection through web scraping + GenAI API models
- DWH design: revisit the whole data process and designed data pipelines to assess and reduce data bottlenecks and outages. 30% improvement and still ongoing
- Served new data assets to BI and CRM marketing automation
''')

txt('#### Data & Product, *Afiniti, Milan, Italy*', 
    '#### 2019-2023')
st.info('**Product & Prototyping**')
st.markdown('''
- Prototypes development for new products, encompassing backend, data pipelines, and frontend components
- Opportunity spaces mapping and product requirements definition
''')
st.info('**Data, Analytics & Machine Learning**')
st.markdown('''
- Expanded responsibilities from Italian clients to UK and US clients
- Responsible for data integration and data architecture design
- Responsible for client data engagement - data requirements and data integration/architecture proposal
- Lead client conversations about optimization metric
- Design, development and implementation of ML-based optimization metrics
''')

txt('#### Data Scientist, CVM, *Nexi, Milan, Italy*',
    '#### 2017-2019')
st.info('**Data, Analytics & Machine Learning**')
st.markdown('''
- First data person in the Customer Value Management team
- Responsible for design and implementation of data-driven solutions to improve customer experience and increase customer value
- Close collaboration with centralized Data team to collect, organize and develop new data source integration
''')

txt('#### Analytics Consultant, *Jakala, Milan, Italy*',
'#### 2015-2017')
st.info('**Data, Analytics & Machine Learning**')
st.markdown('''
- Data analyses for clients across different industries and geographies
- Development of predictive models and ad-hoc analysis, alongside usage of geographical information systems (GIS) to provide actionable insights to clients
''')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#16A2CB;" /> """,
            unsafe_allow_html=True)

#####################
st.markdown('''
## **Education**
''')

txt('**Master of Science** Economics, *Bocconi University*, Milan, Italy',
'2012-2015')
txt('**Exchange** Economics, *Nova School of Business & Economics*, Lisbon, Portugal',
'2014')
txt('**Bachelors of Science** Economics, *Bocconi University*, Milan, Italy',
'2009-2012')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#16A2CB;" /> """,
            unsafe_allow_html=True)

#####################
st.markdown('''
## **Skills**
''')
txt2('Programming', '`Python`, `Linux`')
txt2('OS', '`MacOS`, `Linux`')
txt2('ELT', '`SQL`, `dbt`, `polars`, `airbyte`, `pandas`, `numpy`')
txt2('Data testing', '`great expectations`')
txt2('Data visualization', '`Looker`, `matplotlib`, `seaborn`, `plotly`')
txt2('Machine Learning', '`scikit-learn`')
txt2('Web development', '`Dash`, `Django`, `streamlit`, `HTML`, `CSS`, `Selenium`')
txt2('Cloud & DevOps', '`Docker`, `GCP`, `Kestra`')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#16A2CB;" /> """,
            unsafe_allow_html=True)

#####################
st.markdown('''
## **Portfolio**
''')
txt('#### **Data engineering**',
    '#### *Habacus*')
st.info('**DWH**')
st.markdown('''
- Overview: 
  - Designed from scratch a DWH ingesting data from multiple sources (e.g. web scraping, internal databases, CRM)
  - Implemented a data test validation framework to ensure data quality
  - Developed a data pipeline to serve data to BI and CRM marketing automation through API
  - Orchestrated the whole pipeline through Kestra
- Stack: `dbt`, `airbyte`, `BigQuery`, `API`, `Docker`
- Keywords: `data governance`, `data pipeline`, `ELT`, `data quality`
''')

txt('#### **Data enrichment**',
    '#### *Habacus*')
st.info('**Web scraping**')
st.markdown('''
- Overview: 
  - Designed a data model to enrich existing data with external data sources coming from academic institutions
  - Scraped data from hundreds of websites and extracted relevant data through OpenAI API
  - Ingested data in the DWH
- Stack: `selenium`, `OpenAI`, `BigQuery`, `API`, `Docker`
- Keywords: `web scraping`, `data enrichment`, `GenAI`
''')

txt('#### **Software and data engineering**',
    '#### *Afiniti*')
st.info('**Data discovery app**')
st.markdown('''
- Overview: 
  - Developed and led the design of an internal data governance product to support account teams across Afiniti during discovery phase.
  - Integrated the application into the enterprise portal as an enterprise KPI.
- Stack: `Python`, `Django`, `Docker`, `Linux`, `HTML`, `CSS`
- Keywords: `data governance`, `data pipeline`
''')
st.info('**Channel recommendation prototype**')
st.markdown('''
- Overview: 
  - Development of an omnichannel recommendation prototype, nudging customers from one touchpoint to another (e.g. from web to call center)
  - Responsible for data pipeline, EDA and offline unsupervised clustering algorithm (k-modes) modules
  - Simulated web traffic data to generate synthetic data
- Stack: `Python`, `Selenium`, `Docker`, `GCP` 
- Keywords: `omnichannel`, `clustering`, `web simulation`
''')
st.info('**Fairness in Contact Center**')
st.markdown('''
- Overview:
  - Design and development of a prototype assessing fairness in a Contact Center environment through the use of a Discrete Event Simulation for counterfactuals generation
  - Fairness is assessed through the use of counterfactuals and hypothesis tests
- Stack: `Python`, `Docker`, `Linux`
- Keywords: `fairness`, `counterfactuals`, `causal inference`, `hypotheses tests`
''')
txt('#### **Data, Analytics & Machine Learning**',
    '#### *Afiniti*')
st.info('**Customer Lifetime Value**')
st.markdown('''
- Overview: 
  - Design and development of a Customer Lifetime Value model for improving existing revenue metric
  - Collaboration with both internal (ML and data engineers) and external (Finance team) stakeholders
  - The metric has been optimized using Afiniti proprietary algorithms, returning a `+30%` increase in performance compared to previous metric
- Stack: `Python`, `SQL`, `R`, `Docker`, `Linux`
- Keywords: `customer lifetime value`, `revenue`, `optimization`
''')
txt('#### **Data, Analytics & Machine Learning**',
    '#### *Nexi*')
st.info('**Attribution Model**')
st.markdown('''
- Overview: 
  - Development of an Attribution Model to assess economic impact of the engagement program on customer payment behavior
- Stack: `SAS`, `SQL`, `Python`
- Keywords: `attribution model`, `forecasting`
''')
st.info('**Clustering**')
st.markdown('''
- Overview: definition of Nexi Personas through a mixed approach:
    - Data Driven Segmentation - a view from the inside through internal data
    - Market Research Segmentation - a view from the outside through market research data
    - Combination of inside-in and inside-out views through inference on the market research data
- The results helped informing the digital strategy of the company (which clients to target, which digital products to develop, etc.)
- Stack: `SAS`, `SQL`, `Python`
- Keywords: `clustering`, `market research`
''')
st.info('**Business intelligence**')
st.markdown('''
- Overview: design and development of a data monetization service exposed to partner banks - focus on backend datamarts
- Stack: `SAS`, `SQL`
- Keywords: `business intelligence`, `data modelling`
''')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#16A2CB;" /> """,
            unsafe_allow_html=True)

#####################
st.markdown('''
## **Hobby**
''')
st.info('**Sports**', icon='🏃‍♂️')
st.markdown('''Agonistic track and road runner
''')
st.info('**Hiking**', icon='⛰️')
st.markdown(
    '''My greatest accomplishments have been 
    completing the Tour of Mont Blanc in 8 days (180km and 12000m D+).
    In August 2023, I've summited Mount Kilimanjaro (5.895m above sea level).
''')
            