import sqlite3
import requests
from  bs4 import BeautifulSoup
import csv

create_table="""
CREATE TABLE IF NOT EXISTS Jobs(
job_title TEXT,
company_name TEXT,
location TEXT,
job_description TEXT,
job_link TEXT,
PRIMARY KEY(job_title, company_name, location)
)"""

url='https://realpython.github.io/fake-jobs'
res=requests.get(url)
soup=BeautifulSoup(res.text, 'html.parser')


file_name='jobs.db'
with sqlite3.Connection(file_name) as con:
    cursor=con.cursor()
    cursor.execute(create_table)
    job_cards=soup.find_all('div',class_='card-content')

    for job in job_cards:
        job_title=job.find('h2',class_='title is-5').text.strip()
        company_name=job.find('h3',class_='subtitle is-6 company').text.strip()
        location=job.find('p',class_='location').text.strip()
        job_description=job.find('a', string='Learn')["href"]
        job_link=job.find('a', string='Apply')["href"]
         # Insert job details into the database
        cursor.execute('''
        INSERT INTO jobs (job_title, company_name, location, job_description, job_link)
        VALUES (?, ?, ?, ?, ?)
        ''', (job_title, company_name, location, job_description, job_link))
        cursor.execute('''
            SELECT job_description, job_link FROM Jobs
            WHERE job_title = ? AND company_name = ? AND location = ?
        ''', (job_title, company_name, location))
        
        existing_job = cursor.fetchone()  # Fetch stored job details
        
        if existing_job:
            stored_description, stored_link = existing_job

            # If the description or job link has changed, update the record
            if stored_description != job_description or stored_link != job_link:
                cursor.execute('''
                    UPDATE Jobs
                    SET job_description = ?, job_link = ?
                    WHERE job_title = ? AND company_name = ? AND location = ?
                ''', (job_description, job_link, job_title, company_name, location))
                print(f"Updated job: {job_title} at {company_name}, {location}")
            else:
                print(f"No changes for: {job_title} at {company_name}, {location}")

        else:
            # Insert new job details into the database
            cursor.execute('''
                INSERT INTO Jobs (job_title, company_name, location, job_description, job_link)
                VALUES (?, ?, ?, ?, ?)
            ''', (job_title, company_name, location, job_description, job_link))
            print(f"Added new job: {job_title} at {company_name}, {location}")

    con.commit()  # Save changes to the database

print("Job listings have been successfully updated in jobs.db")


def filter_jobs(filter_by, value):
    """
    Filter job listings by location or company name.
    :param filter_by: 'location' or 'company_name'
    :param value: The value to filter by (e.g., 'New York' or 'Google')
    """
    with sqlite3.connect(file_name) as con:
        cursor = con.cursor()
        
        query = f"SELECT * FROM Jobs WHERE {filter_by} = ?"
        cursor.execute(query, (value,))
        
        results = cursor.fetchall()
        
        if results:
            print(f"\n🔎 Found {len(results)} job(s) for {filter_by}: {value}")
            for job in results:
                print(job)
        else:
            print(f"\n⚠ No jobs found for {filter_by}: {value}")
        
        return results

def export_jobs_to_csv(filter_by, value, filename="filtered_jobs.csv"):

    jobs = filter_jobs(filter_by, value)
    
    if not jobs:
        print(" No jobs to export.")
        return
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Job Description", "Job Link"])  # Header
        
        for job in jobs:
            writer.writerow(job)
    
    print(f" Jobs exported successfully to {filename}")



# Example: Filter jobs in 'New York' and export to CSV
filter_jobs('location', 'New York')  
export_jobs_to_csv('location', 'New York', 'new_york_jobs.csv')

# Example: Filter jobs at 'Google' and export to CSV
filter_jobs('company_name', 'Google')
export_jobs_to_csv('company_name', 'Google', 'google_jobs.csv')