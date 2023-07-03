from pathlib import Path
import streamlit as st
from utils import txt, txt2

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV Edoardo Sezzi - tech.pdf"
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

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
            unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#portfolio">Portfolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#hobby">Hobby</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
st.markdown('''
## **Work Experience**
''')

txt('#### Data & Product, *Afiniti, Milan, Italy*',
    '#### 2019-Present')
st.info('**Product & Prototyping**')
st.markdown('''
- Prototypes development for new products, encompassing backend, data pipelines, and frontend components
- Opportunity spaces mapping and product requirements definition
''')
st.info('**Data, Analytics & Machine Learning**')
st.markdown('''
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


#####################
st.markdown('''
## **Skills**
''')
txt2('Programming', '`Python`, `Linux`')
txt2('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt2('Data testing',  '`great expectations`')
txt2('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt2('Automation', '`Selenium`')
txt2('Machine Learning', '`scikit-learn`')
txt2('Web development', '`Dash`, `Django`, `streamlit`, `HTML`, `CSS`')
txt2('Infra', '`Docker`, `GCP`')

#####################
st.markdown('''
## **Portfolio**
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


#####################
st.markdown('''
## **Hobby**
''')
st.info('**Sports**', icon='🏃‍♂️')
st.markdown('''Agonistic track and road runner
''')
st.info('**Hiking**', icon='⛰️')
st.markdown(
    '''My greatest accomplishment has been 
    completing the Tour of Mont Blanc in 8 days (180km and 12000m D+)
''')
st.info('**Trading**', icon='💹')
st.markdown('''
I am a self-taught trader, I have been trading for a couple years, mainly options on indexes and certificates. 
I have developed a Python bot which scraped and stored data from the web. I have developed a Python bot which scraped and stored data from the web.
The main goal was to create an optimization algorithm to find the strategy that would maximize expected payoff for options trading given a set of constraints (e.g. margin, number of options)
''')
            