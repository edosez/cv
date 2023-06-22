import streamlit as st
from PIL import Image
from pathlib import Path

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
with open(css_file) as f:
  st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
  PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#####################
# Header 
st.write('''
# Edoardo Sezzi
##### *Resume* 
''')

#image = Image.open('dp.png')
st.image(profile_pic, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Experienced data professional with cross-field skillset, combining data expertise with software engineering practices. Involved in client-related conversations and pre-sales engagement.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

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
        <a class="nav-link" href="#hobbies">Hobby</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## **Work Experience**
''')

txt('#### Data & Product, *Afiniti, Milan, Italy*', 
    '#### 2019-Present')
st.info('**Product & Prototyping**')
st.markdown('''
As part of the Product team, I am responsible for developing prototypes and proofs of concept for new products and features. This activity requires a deep understanding of prospect clients pain points combined with a solid technological understanding and a quick iteration process.
''')
st.info('**Data, Analytics & Machine Learning**')
st.markdown('''
As part of the Data team, I am responsible for the data engagement with the client, leading optimization metric conversations and closely collaborating with client's data team to ensure a smooth integration of Afiniti into the client's data ecosystem.
''')

txt('#### Data Scientist, CVM, *Nexi, Milan, Italy*',
    '#### 2017-2019')
st.info('**Data, Analytics & Machine Learning**')
st.markdown('''
As the first data person in the Customer Value Management team, I was responsible for the implementation of data-driven solutions to improve customer experience and increase customer value. I was also the business point of contact with centralizwed Data team to collect and organize new data requests.
''')
            
txt('#### Analytics Consultant, *Jakala, Milan, Italy*',
'#### 2015-2017')
st.info('**Data, Analytics & Machine Learning**')
st.markdown('''
Data analyses for several clients across different industries and geographies. Development of predictive models and ad-hoc analysis, alongside usage of geographical information systems (GIS) to provide actionable insights to clients.
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
txt3('Programming', '`Python`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data testing',  '`great expectations`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Automation', '`Selenium`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Web development', '`Dash`, `Django`, `streamlit`, `HTML`, `CSS`')
txt3('Infra', '`Docker`, `GCP`')

#####################
st.markdown('''
## **Portfolio**
''')
            
txt('#### **Software and data engineering**', 
    '#### *Afiniti*')
st.info('**Data discovery app**')
st.markdown('''
- Overview: developed and led the design of an internal data governance product that transformed client discovery. Simplified access to critical data for Afiniti modeling through a centralized repository. Implemented an efficient data pipeline, ensuring data quality and user input handling. Integrated the application into the enterprise portal for real-time monitoring of company KPIs.
- Stack: `Python`, `Django`, `Docker`, `Linux`
- Keywords: `data governance`, `data pipeline`, `product roadmap`
''')
st.info('**Channel recommendation prototype**')
st.markdown('''
- Overview: evelopment of an omnichannel recommendation prototype, nudging customers from one touchpoint to another. Responsible for data pipeline, EDA and offline unsupervised clustering algorithm (k-modes) modules.
- Stack: `Python`, `Selenium`, `Docker`, `GCP` 
- Keywords: `omnichannel`, `recommendation`, `clustering`
''')
st.info('**Fairness in Contact Center**')
st.markdown('''
- Overview: design and development of a prototype assessing fairness in a Contact Center environment through the use of a Discrete Event Simulation model, which involves the generation of counterfactuals and hypotheses tests.
- Stack: `Python`, `Docker`, `Linux`
- Keywords: `fairness`, `counterfactuals`, `causal inference`, `hypotheses tests`
''')
txt('#### **Data, Analytics & Machine Learning**', 
    '#### *Afiniti*')
st.info('**Customer Lifetime Value**')
st.markdown('''
- Overview: design and development of a Customer Lifetime Value model for improving existing revenue metric. This metric has been then optimized by Afiniti proprietary algorithms, returning a `+30%` increase in performance compared to previous metric.
- Stack: `Python`, `SQL`, `Docker`, `Linux`
- Keywords: `customer lifetime value`, `revenue`, `optimization`
''')
txt('#### **Data, Analytics & Machine Learning**', 
    '#### *Nexi*')
st.info('**Attribution Model**')
st.markdown('''
- Overview: development of an Attribution Model to assess economic impact of the engagement program on CVM revenues
- Stack: `SAS`, `SQL`, `Python`
- Keywords: `attribution model`, `revenue`
''')
st.info('**Clustering**')
st.markdown('''
- Overview: definition of Nexi Personas through a mixed approach:
    - Data Driven Segmentation - a view from the inside through internal data
    - Market Research Segmentation - a view from the outside through market research data
    - Final synthesis and personas through a combination of Segmentations used for defining digital strategy
- Stack: `SAS`, `SQL`, `Python`
- Keywords: `personas`, `clustering`
''')
st.info('**Business intelligence**')
st.markdown('''
- Overview: design and development of a data monetization service exposed to partner banks - focus on backend datamarts
- Stack: `SAS`, `SQL`
- Keywords: `business intelligence`, `data modelling`
''')


#####################
st.markdown('''
## **Social Media**
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/edoardo-sezzi')
txt2('GitHub', 'https://github.com/edosez')

#####################
st.markdown('''
## **Hobby**
''')
st.info('**Sports**', icon='🏃‍♂️')
st.markdown('''Agonistic track and road runner
''')
st.info('**Hiking**', icon='⛰️')
st.markdown('''My greatest accomplishment has been completing the Tour of Mont Blanc by myself (180km and 12000m D+)
''')
st.info('**Trading**', icon='💹')
st.markdown('''I am a self-taught trader, I have been trading for a couple years, mainly options on indexes and certificates. I have developed a Python bot which scraped and store data from the web. The main goal was to create an optimization algorithm to find the strategy that would maximize expected payoff for options trading given a set of constraints (e.g. margin, number of options). 
''')