import pandas as pd

# Load your combined dataset
df = pd.read_csv('ai_job_dataset_combined.csv')

# Explode the skills column into one row per skill
df['skills_list'] = df['required_skills'].str.split(', ')
skills_long = df.explode('skills_list')
skills_long['skills_list'] = skills_long['skills_list'].str.strip()

# Top skills
skill_counts = skills_long['skills_list'].value_counts()
print("TOP 20 SKILLS:")
print(skill_counts.head(20))

# Programming languages
languages = ['Python', 'SQL', 'R', 'Java', 'C++', 'Scala', 'Julia', 'JavaScript', 'MATLAB', 'Go']
lang_df = skills_long[skills_long['skills_list'].isin(languages)]
lang_counts = lang_df['skills_list'].value_counts()
print("\nTOP LANGUAGES:")
print(lang_counts)

# Sanity checks
print("\nSALARY STATS:")
print(df['salary_usd'].describe())
print("\nEXPERIENCE LEVELS:", df['experience_level'].unique())
print("REMOTE RATIOS:", df['remote_ratio'].unique())

# Save outputs
skills_long.to_csv('skills_long.csv', index=False)
lang_df.to_csv('languages_long.csv', index=False)
df.to_csv('ai_jobs_final_cleaned.csv', index=False)
print("\nDone. Files saved.")