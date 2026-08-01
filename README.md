# AI Job Market Analysis (2024–2025)

End-to-end data analysis project exploring how AI is reshaping the job market — from raw job postings to an interactive Power BI dashboard.

## Problem

The AI job market is evolving fast: new roles, new required skills, and shifting salary and remote-work expectations. This project analyzes ~30,000 AI/tech job postings to answer:

- Which AI skills are most in demand?
- What are the highest-paying AI roles?
- How do remote, hybrid, and onsite jobs compare?
- How does experience level affect salary?
- Who are the top hiring companies?
- Which programming languages are most requested?

## Data Source

- **Kaggle: Global AI Job Market & Salary Trends 2025** — ~30,000 combined job postings , including job title, salary (USD), experience level, required skills, remote ratio, company info, and more.

## Tools & Pipeline

| Stage | Tool | Output |
|---|---|---|
| Data cleaning & transformation | Python (pandas) | `ai_jobs_final_cleaned.csv`, `skills_long.csv`, `languages_long.csv` |
| Querying & analysis | SQL (SQLite) | `ai_jobs.db` |
| Visualization | Power BI | `AI_Job_Market_Dashboard.pbix` |

**Workflow:** 
Raw CSVs → cleaned & reshaped in Python → loaded into SQLite for SQL analysis → visualized in an interactive Power BI dashboard.

## Project Files

```
├── ai_job_dataset.csv / ai_job_dataset1.csv   # Raw source data (Kaggle)
├── clean_data.py                              # Cleans data, explodes skills into long format
├── ai_jobs_final_cleaned.csv                  # Cleaned master dataset
├── skills_long.csv / languages_long.csv       # One row per job-skill pair (for demand analysis)
├── load_sql.py                                # Loads cleaned data into SQLite, runs analysis queries
├── ai_jobs.db                                 # SQLite database
└── AI_Job_Market_Dashboard.pbix                # Interactive Power BI dashboard
```

## Dashboard

The Power BI dashboard includes:
- **KPI summary cards** — total postings, average salary, % remote
- **Top AI Skills in Demand** — most requested skills across all postings
- **Highest Paying AI Roles** — top 10 job titles by average salary
- **Remote vs Onsite Distribution** — breakdown by work type
- **Average Salary by Experience Level** — entry to executive
- **Top Hiring Companies** — most active employers
- **Interactive slicers** — filter the entire dashboard by experience level, work type, and company location

## Key Findings

- **Python and SQL dominate** required skills, followed by Scala, Java, and R.
- **Executive-level roles pay roughly 2x** entry-level roles on average.
- Work arrangements are **nearly evenly split** across Onsite, Hybrid, and Remote (~33% each).
- Highest-paying titles skew toward specialized/senior roles such as Data Engineer, AI Specialist, and Head of AI.
- Hiring is spread across many companies rather than concentrated in a few — no single employer dominates postings.

## How to Reproduce

1. Download the dataset from Kaggle (linked above).
2. Run `clean_data.py` to clean and reshape the data.
3. Run `load_sql.py` to load the cleaned data into SQLite and view the analysis query results.
4. Open `AI_Job_Market_Dashboard.pbix` in Power BI Desktop to explore the interactive dashboard.
