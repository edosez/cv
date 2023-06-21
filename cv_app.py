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
PAGE_ICON = ":wave:"
NAME = "Edoardo Sezzi"

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
Experienced data professional, with a strong background in data analysis, data visualization, data management and machine learning.
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
## Work Experience
''')

txt('**Data & Product**, *Afiniti, Milan, Italy*', 
    '2019-Present')
st.info('**Product & Prototyping**')
st.markdown('''
- Designed and developed an internal product: Led the end-to-end design and development of an internal product that revolutionized the client discovery process. This product facilitated seamless access to a centralized repository of critical data points required for Afiniti modeling. Implemented a robust data pipeline that efficiently handled user inputs, stored data in a Relational Database, and monitored activity and data quality. Successfully integrated the application into the enterprise portal, enabling real-time monitoring of company KPIs.
- Development of an omnichannel recommendation prototype, nudging customers from one touchpoint to another. Responsible for data pipeline, EDA and offline unsupervised clustering algorithm (k-modes) modules.
- Design and development of a prototype assessing fairness in a Contact Center environment through the use of a Discrete Event Simulation model, which involves the generation of counterfactuals and hypotheses tests.
''')
st.info('**Data & Analytics**')
st.markdown('''
- Design and development of a Customer Lifetime Value model for improving existing revenue metric. This metric has been then optimized by Afiniti proprietary algorithms, returning a `+30%` increase in performance compared to previous metric.
- Deployed Afiniti data integration solution for clients in the EMEA region. The activity required discovery activities (explore clients' data environment), data transfer, validation and transformation. Constant client exposure and communication, both setting expectations and managing internal requests to improve the deployment outcome.
''')


txt('**Data Scientist**, Customer Vale Management, *Nexi, Milan, Italy*',
    '2017-2019')
st.markdown('''
- Development of an Attribution Model to assess economic impact of the engagement program on CVM revenues
- First deployment into production of a machine learning algorithm
- Definition of Nexi Personas through a mixed approach:
    - Data Driven Segmentation - a view from the inside through internal data
    - Market Research Segmentation - a view from the outside through market research data
    - Final synthesis and personas through a combination of Segmentations
- Development of a mobile payer inactivity score to trigger campaign communications
- Design, development and prototyping of a data monetization service exposed to partner banks - focus on backend datamarts
''')
            
txt('**Analytics Consultant**, *Jakala, Milan, Italy*',
'2015-2017')
st.markdown('''
- Data analyses for a variety of clients in different industries across Italy and Europe. Development of predictive and descriptive models through data mining techniques in order to provide valuable insights and impactful results. Some example:
- Behavioral segmentation (k-means) and deterministic segmentation (RFM)
- Development of churn model for a leading European shoes retailer
- Development of predictive model to assess the probability of repurchase for new clients
- Comprehensive CRM support: structured reporting and spot analyses necessary to assess business performance through KPIs and trends
- Integration of statistical analyses with geographical data (elaborated with ArcGis)
''')
            
#####################
st.markdown('''
## Education
''')

txt('**Master of Science** Economics, *Bocconi University*, Milan, Italy',
'2012-2015')
txt('**Exchange** Economics, *Nova School of Business & Economics*, Lisbon, Portugal',
'2014')
txt('**Bachelors of Science** Economics, *Bocconi University*, Milan, Italy',
'2009-2012')


#####################
st.markdown('''
## Skills
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
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/edoardo-sezzi')
txt2('GitHub', 'https://github.com/edosez')

#####################
st.markdown('''
## Hobby
''')
st.info('**Sports**')
st.markdown('''Agonistic track and road runner
''')
st.info('**Hiking**')
st.markdown('''My greatest accomplishment has been completing the Tour of Mont Blanc by myself (180km and 12000m D+)
''')
st.info('**Trading**')
st.markdown('''I am a self-taught trader, I have been trading for a couple years, mainly options on indexes and certificates. I have developed a Python bot which scraped and store data from investing.com. The main goal was to create an optimization algorithm to find the strategy that would maximize expected payoff for options trading given a set of constraints (e.g. margin, number of options). 
''')