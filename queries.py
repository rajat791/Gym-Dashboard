import sqlite3
import pandas as pd
import datetime
from helper import ordinal, format_pretty_date

def total_workouts(date_from, date_to, conn):
    query = """
    SELECT COUNT(DISTINCT WorkoutID)
    FROM workouts
    WHERE Date BETWEEN ? AND ?;
    """

    df = pd.read_sql_query(query, conn, params=(date_from, date_to))
    return df.iloc[0, 0]


def total_sets(date_from, date_to, conn):
    query = """
    SELECT COUNT("Set Order")
    FROM workouts
    WHERE Date BETWEEN ? AND ?;
    """

    df = pd.read_sql_query(query, conn, params=(date_from, date_to))
    return df.iloc[0, 0]


def total_volume(date_from, date_to, conn):
    query = """
    SELECT SUM(Volume)
    FROM workouts
    WHERE Date BETWEEN ? AND ?;
    """

    df = pd.read_sql_query(query, conn, params=(date_from, date_to))
    return df.iloc[0, 0]


# -------------------------------------------------------------------
# Home Page
# -------------------------------------------------------------------

def get_recent_activity(conn, date_from=None, date_to=None):

    if date_to is None:
        date_to = datetime.date.today()

    if date_from is None:
        date_from = date_to - datetime.timedelta(days=7)

    query = """
    SELECT
        w.WorkoutID,
        w.Date,
        w."Workout Name",
        w.Duration,
        mg."Muscle Groups"
    FROM (
        SELECT DISTINCT WorkoutID, Date, "Workout Name", Duration
        FROM workouts
    ) w
    JOIN (
        SELECT WorkoutID, GROUP_CONCAT(DISTINCT "Muscle Group") AS "Muscle Groups"
        FROM workouts
        GROUP BY WorkoutID
    ) mg ON w.WorkoutID = mg.WorkoutID
    WHERE w.Date BETWEEN ? AND ?
    ORDER BY w.Date DESC
    LIMIT 5;
    """

    df = pd.read_sql_query(query, conn, params=(date_from, date_to))
    df["Muscle Groups"] = df["Muscle Groups"].str.replace(",", ", ")
    return df


def workouts_per_week_between_dates(conn, date_from=None, date_to=None):

    if date_to is None:
        date_to = datetime.date.today()

    if date_from is None:
        date_from = date_to - datetime.timedelta(days=60)

    query = """
    SELECT
        strftime('%Y-%W', Date) AS Week,
        COUNT(DISTINCT WorkoutID) AS Workouts
    FROM workouts
    WHERE Date BETWEEN ? AND ?
    GROUP BY strftime('%Y-%W', Date)
    ORDER BY Week;
    """

    return pd.read_sql_query(query, conn, params=(date_from, date_to))


# -------------------------------------------------------------------
# Workout Details Page
# -------------------------------------------------------------------

def workout_details(conn, workoutid):

    query = """
    SELECT *
    FROM workouts
    WHERE WorkoutID = ?;
    """

    return pd.read_sql_query(query, conn, params=(workoutid,))


def total_volume_per_muscle_group(conn, workoutid):

    query = """
    SELECT
        "Muscle Group",
        SUM(Volume) AS TotalVolume
    FROM workouts
    WHERE WorkoutID = ?
    GROUP BY "Muscle Group"
    ORDER BY TotalVolume DESC;
    """

    return pd.read_sql_query(query, conn, params=(workoutid,))


def total_sets_per_muscle_group(conn, workoutid):

    query = """
    SELECT
        "Muscle Group",
        COUNT(*) AS TotalSets
    FROM workouts
    WHERE WorkoutID = ?
    GROUP BY "Muscle Group"
    ORDER BY TotalSets DESC;
    """

    return pd.read_sql_query(query, conn, params=(workoutid,))


