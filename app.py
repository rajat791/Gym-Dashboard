from queries import total_volume, total_workouts, total_sets
from utils.ui import load_css, render_splash, page_header
import streamlit as st
import sqlite3
import datetime
import os

st.set_page_config(page_title="Gym Dashboard", page_icon="⚔️", layout="wide")

# ---- Theme + splash (call these first, before any other content) ----
load_css()
render_splash(title="WELCOME BACK", subtitle="SYSTEM ONLINE")

# ---- Connection (cached so it isn't reopened on every rerun) ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "workouts.db")

@st.cache_resource
def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

conn = get_connection()

# ---- Sidebar navigation ----
# st.page_link only works for pages that actually exist. "app.py" (this file)
# is always safe. Once you add files under pages/, uncomment the matching
# line below — the icons will show collapsed, labels appear on hover.
with st.sidebar:
    st.page_link("app.py", label="Home", icon="🏠")
    # st.page_link("pages/1_Exercises.py", label="Exercises", icon="💪")
    # st.page_link("pages/2_Muscle_Groups.py", label="Muscle Groups", icon="🧠")
    # st.page_link("pages/3_History.py", label="History", icon="📜")

# ---- Constraints on the date range ----
FIRST_WORKOUT_DATE = datetime.date(2021, 8, 11)
TODAY = datetime.date.today()

page_header("Gym Dashboard", "Hunter status report")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3>Workout Summary</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    date_from = st.date_input(
        "Date from",
        value=FIRST_WORKOUT_DATE,
        min_value=FIRST_WORKOUT_DATE,
        max_value=TODAY,
    )

with col2:
    date_to = st.date_input(
        "Date to",
        value=TODAY,
        min_value=FIRST_WORKOUT_DATE,
        max_value=TODAY,
    )

if date_from > date_to:
    st.error("'Date from' can't be after 'Date to'. Adjust one of the dates above.")
else:
    workouts = total_workouts(date_from, date_to, conn)
    sets_count = total_sets(date_from, date_to, conn)
    volume = total_volume(date_from, date_to, conn)

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Workouts", workouts or 0)
    m2.metric("Total Sets", sets_count or 0)
    m3.metric("Total Volume (kg)", f"{volume:,.0f}" if volume else 0)