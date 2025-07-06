# 🧠 SQL Practice Problems – HackerRank Challenge Solutions

Welcome to my SQL practice repository! This collection contains well-structured solutions to common SQL problems from platforms like **HackerRank**. Each query is designed to reinforce a specific concept — perfect for interview prep or honing your SQL skills.

---

## 📚 Topics Covered

| Concept | Description |
|--------|-------------|
| `SELECT`, `WHERE`, `JOIN` | Basic querying and combining multiple tables |
| Aggregate functions | `MAX()`, `MIN()`, `COUNT()`, `SUM()` |
| Grouping & Filtering | `GROUP BY`, `HAVING`, `DISTINCT` |
| Sorting & Formatting | `ORDER BY`, `ROUND()`, `ASC/DESC` |
| Conditional logic | `IF()`, `CASE` |
| Subqueries | Nested & correlated subqueries |
| Window functions | `RANK() OVER (...)` |
| String & Math functions | `SUBSTR()`, `LOWER()`, `SQRT()`, `POWER()` |

---

## ✅ Problem Summaries & Key Learnings

### 1. City Names with Vowels
> Find city names starting and ending with vowels.
- **Skills**: `SUBSTR()`, `LOWER()`, filtering

### 2. Cities in Africa
> Join `CITY` and `COUNTRY` to filter cities in the African continent.
- **Skills**: `JOIN`, `WHERE`

### 3. Euclidean Distance
> Calculate distance between max/min latitude and longitude.
- **Skills**: `MAX()`, `MIN()`, `SQRT()`, `POWER()`, `ROUND()`

### 4. Student Grades Report
> Show names only for students with grades >= 8.
- **Skills**: `JOIN`, `IF()`, `ORDER BY` with multiple rules

### 5. Population Difference
> Find the difference between highest and lowest city populations.
- **Skills**: `MAX()`, `MIN()`

### 6. Median Latitude
> Compute the median value of latitude from `STATION`.
- **Skills**: Window function `RANK()`, `ROUND()`

### 7. Hacker Leaderboard – Full Scores
> List hackers with full scores in more than one challenge.
- **Skills**: `JOIN`, `GROUP BY`, `HAVING`, `COUNT(DISTINCT ...)`

### 8. Ron’s Wand Selection
> Find the cheapest non-evil wand for each (age, power).
- **Skills**: Correlated subqueries, filtering minimums

### 9. Hacker Leaderboard – Total Scores
> Get total score per hacker using their best scores per challenge.
- **Skills**: Subqueries with `MAX()`, aggregation with `SUM()`, `HAVING`

---

## 📁 How to Use

You can browse each SQL query in the source `.sql` files or copy them to test in your own database. They’re written to be beginner-friendly while demonstrating best practices.

---

## 🚀 Why This Project?

This repository helps you:

- 🧩 Understand real-world SQL query patterns  
- 🧪 Practice common SQL interview questions  
- 💡 Learn different ways to join, group, and filter data  
- 🎓 Strengthen both simple and advanced SQL skills

---

## 🧑‍💻 Author

**Ananya Pal**  




