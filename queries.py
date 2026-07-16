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


# function below is used to show recent activity between two dates
# displays latest 5 workouts between two dates


def recent_activity(conn, date_from=None, date_to=None):

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
    WHERE Date BETWEEN ? AND ?
    ORDER BY Date DESC
    LIMIT 5

    """

    recent_activity_df = pd.read_sql_query(query,conn, params=(date_from, date_to))
    return recent_activity_df

def workout_details(query, conn, workoutid):

    query = """
    SELECT * 
    FROM workouts
    WHERE WorkoutID = ?


    """

    workout_details_df = pd.read_sql_query(query, conn, params=(workoutid,))
    return workout_details_df

def total_volume_per_muscle_group(query, conn, workoutid):
    query = """
    SELECT 
        "Muscle Group",
        SUM(Volume) AS TotalVolume
    FROM workouts
    WHERE WorkoutID = ?
    GROUP BY "Muscle Group"
    ORDER BY TotalVolume DESC;

    """

    total_volume_per_muscle_group = pd.read_sql_query(query, conn, params=(workoutid,))
    return total_volume_per_muscle_group

def total_sets_per_muscle_group(query, conn, workoutid):
    query = """
    SELECT 
        "Muscle Group",
        COUNT(*) AS TotalSets
    FROM workouts
    WHERE WorkoutID = ?
    GROUP BY "Muscle Group"
    ORDER BY TotalSets DESC;

    """

    total_sets_per_muscle_group = pd.read_sql_query(query, conn, params=(workoutid,))
    return total_sets_per_muscle_group


def workouts_per_week_between_dates(query,conn,workoutid):

    query = """

    

    """
    










