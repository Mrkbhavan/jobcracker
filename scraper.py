import json
import datetime

# Keyword-based Categorization Logic (Group A, B, C, D)
def categorize_job(title):
    title = title.lower()
    if any(word in title for word in ['ias', 'ips', 'scientist', 'director', 'commissioner', 'group a']):
        return "Group A (Gazetted)"
    elif any(word in title for word in ['inspector', 'section officer', 'manager', 'group b']):
        return "Group B (Mid-Level)"
    elif any(word in title for word in ['clerk', 'assistant', 'constable', 'technician', 'typist', 'group c']):
        return "Group C (Clerical)"
    elif any(word in title for word in ['mts', 'driver', 'peon', 'sweeper', 'helper', 'group d']):
        return "Group D (Support Staff)"
    return "Others"

# Central & State Govt Job Links (Simulated fetch from official sources)
def fetch_official_jobs():
    return

today = datetime.datetime.now().date()
raw_jobs = fetch_official_jobs()

active_jobs =
archived_jobs =

# Expiry Filter & Auto-Categorization
for job in raw_jobs:
    # Assign category based on title
    job['category'] = categorize_job(job['title'])
    
    expiry_date = datetime.datetime.strptime(job['last_date'], '%Y-%m-%d').date()
    
    if expiry_date >= today:
        active_jobs.append(job)
    else:
        archived_jobs.append(job)

# Save to JSON (Zero-Database Architecture)
with open('jobs.json', 'w') as f:
    json.dump(active_jobs, f, indent=4)

with open('archive.json', 'w') as f:
    json.dump(archived_jobs, f, indent=4)

print(f"Update Success! Active Jobs: {len(active_jobs)}, Archived: {len(archived_jobs)}")
