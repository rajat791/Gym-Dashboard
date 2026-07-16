# Learning SQL

- i have little experience in SQL
- to learn more i will document notes here


so far i have this understanding

so after select, you write in columns to want to add, perform oprations on, then you have your conditional, then how you want this to look and be presented so like structure and organisation.

this is for this query

```sql
SELECT strftime('%W', Date) AS Week, COUNT(DISTINCT WorkoutID) AS Workouts FROM workouts WHERE Date BETWEEN ? AND ?  GROUP BY Week;
```

