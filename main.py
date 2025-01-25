import pandas as pd

# read data into a pandas dataframe
df = pd.read_csv("./jobs_in_data.csv") 

# Analyze data to find the top three jobs in data science
top_jobs = pd.Series(df['job_title'].value_counts())  
print(f"The top three jobs in data science are: {top_jobs.head(3)}.")

# Analyze data to find the top three entry level position in data science
entry_positions = df[df['experience_level'] == 'Entry-level']
top_entry_jobs = pd.Series(entry_positions['job_title'].value_counts())
print(f"The top three entry level jobs in data science are: {top_entry_jobs.head(3)}.\n")

# find the average salary
avg_salary = df['salary'].mean()
print(f"The average salary in data science is: ${avg_salary:,.2f}")

# The average salary of just entry level positions
avg_entry_salary = entry_positions['salary'].mean()
print(f"The average salary for an entry level position is: ${avg_entry_salary:,.2f}\n")

# calculate the percentage of growth of data science jobs from 2020 to 2024
df_workyear_2020 = df[df['work_year'] == 2020] 
num_jobs_2020 = len(df_workyear_2020)
print(f"Number of data science jobs in 2020: {num_jobs_2020}")

df_workyear_2023 = df[df['work_year'] == 2023] 
num_jobs_2023 = len(df_workyear_2023)
print(f"Number of data science jobs in 202: {num_jobs_2023}")

percentage_growth = ((num_jobs_2023-num_jobs_2020)/num_jobs_2020)*100
print(f"Job growth from 2020 to 2023 was {percentage_growth:,.0f}%\n")