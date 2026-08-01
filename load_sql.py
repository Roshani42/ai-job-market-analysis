import pandas as pd
import sqlite3

# Connect to (or create) a SQLite database file
conn = sqlite3.connect('ai_jobs.db')

# Load your cleaned CSVs into SQL tables
df = pd.read_csv('ai_jobs_final_cleaned.csv')
skills_long = pd.read_csv('skills_long.csv')
lang_df = pd.read_csv('languages_long.csv')

df.to_sql('jobs', conn, if_exists='replace', index=False)
skills_long.to_sql('skills_long', conn, if_exists='replace', index=False)
lang_df.to_sql('languages_long', conn, if_exists='replace', index=False)

print("Tables loaded into ai_jobs.db\n")

# ---- QUERY 1: Top 15 most demanded skills ----
q1 = """
SELECT skills_list AS skill, COUNT(*) AS demand_count
FROM skills_long
GROUP BY skills_list
ORDER BY demand_count DESC
LIMIT 15;
"""
print("TOP 15 SKILLS:")
print(pd.read_sql(q1, conn))

# ---- QUERY 2: Highest paying roles (avg salary by job title) ----
q2 = """
SELECT job_title, ROUND(AVG(salary_usd),0) AS avg_salary, COUNT(*) AS num_postings
FROM jobs
GROUP BY job_title
HAVING num_postings >= 20
ORDER BY avg_salary DESC
LIMIT 15;
"""
print("\nTOP 15 HIGHEST PAYING ROLES:")
print(pd.read_sql(q2, conn))

# ---- QUERY 3: Remote vs Onsite ----
q3 = """
SELECT 
  CASE 
    WHEN remote_ratio = 0 THEN 'Onsite'
    WHEN remote_ratio = 50 THEN 'Hybrid'
    WHEN remote_ratio = 100 THEN 'Remote'
  END AS work_type,
  COUNT(*) AS num_postings,
  ROUND(AVG(salary_usd),0) AS avg_salary
FROM jobs
GROUP BY work_type
ORDER BY num_postings DESC;
"""
print("\nREMOTE VS ONSITE:")
print(pd.read_sql(q3, conn))

# ---- QUERY 4: Experience level distribution + salary ----
q4 = """
SELECT experience_level, COUNT(*) AS num_postings, ROUND(AVG(salary_usd),0) AS avg_salary
FROM jobs
GROUP BY experience_level
ORDER BY avg_salary DESC;
"""
print("\nEXPERIENCE LEVEL BREAKDOWN:")
print(pd.read_sql(q4, conn))

# ---- QUERY 5: Top hiring companies ----
q5 = """
SELECT company_name, COUNT(*) AS num_postings
FROM jobs
GROUP BY company_name
ORDER BY num_postings DESC
LIMIT 15;
"""
print("\nTOP 15 HIRING COMPANIES:")
print(pd.read_sql(q5, conn))

# ---- QUERY 6: Top programming languages ----
q6 = """
SELECT skills_list AS language, COUNT(*) AS demand_count
FROM languages_long
GROUP BY skills_list
ORDER BY demand_count DESC;
"""
print("\nTOP PROGRAMMING LANGUAGES:")
print(pd.read_sql(q6, conn))

conn.close()
print("\nDone.")