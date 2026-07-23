# Learning SQL

- i have little experience in SQL
- to learn more i will document notes here


so far i have this understanding

so after select, you write in columns to want to add, perform oprations on, then you have your conditional, then how you want this to look and be presented so like structure and organisation.

this is for this query

```sql
SELECT strftime('%W', Date) AS Week, COUNT(DISTINCT WorkoutID) AS Workouts FROM workouts WHERE Date BETWEEN ? AND ?  GROUP BY Week;
```



# Pages

## Home Page
- has an option to select between dates
- shows total workouts, total volume, total sets between those sets
- shows last 5 workouts (recent activity)
- workout frequency bar chart between workouts

for now i think this page has enough content, if i think it needs more i will add.

## Exercise Page
- have all exercises i have done
- select one i can see data for it 
