import sqlite3
import pandas as pd
import datetime



def total_workouts(date_from, date_to, conn):
    query = """
    SELECT COUNT(DISTINCT "WorkoutID") 
    FROM workouts
    WHERE Date between ? AND ?;
    """

    total_workouts = pd.read_sql_query(query,conn, params=(date_from, date_to))
    return total_workouts.iloc[0,0]

def total_sets(date_from, date_to, conn):
    query = """
    SELECT COUNT("Set Order") 
    FROM workouts
    WHERE Date between ? AND ?;
    """

    total_sets = pd.read_sql_query(query,conn, params=(date_from, date_to))
    return total_sets.iloc[0,0]

def total_volume(date_from, date_to, conn):
    query = """
    SELECT SUM(Volume) 
    FROM workouts
    WHERE Date between ? AND ?;
    """

    total_volume = pd.read_sql_query(query,conn, params=(date_from, date_to))
    return total_volume.iloc[0,0]

def workouts_this_week(conn, date_from=None, date_to=None):

    if date_to is None:
        date_to = datetime.date.today()

    if date_from is None:
        date_from = date_to - datetime.timedelta(days=7)

    query = """
    SELECT DISTINCT
        WorkoutID,
        Date,
        "Workout Name",
        Duration
    FROM workouts
    WHERE Date BETWEEN ? AND ?;
    """

    workouts_this_week_df = pd.read_sql_query(query,conn, params=(date_from, date_to))
    return workouts_this_week_df



