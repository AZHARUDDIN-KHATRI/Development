import re
from collections import Counter

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def calculate_match_score(resume_text, job_description):
    resume_words = set(clean_text(resume_text).split())
    job_words = set(clean_text(job_description).split())
    
    # Common stop words to exclude
    stop_words = {'the', 'and', 'a', 'of', 'to', 'in', 'is', 'for', 'with', 'on', 'at', 'by', 'an', 'be'}
    important_job_keywords = job_words - stop_words
    
    matched_keywords = resume_words.intersection(important_job_keywords)
    
    if not important_job_keywords:
        return 0, []
        
    match_percentage = (len(matched_keywords) / len(important_job_keywords)) * 100
    return round(match_percentage, 2), list(matched_keywords)

# Mock Data
sample_resume = """
Experienced Python Developer skilled in Django, Flask, and SQLite. 
Strong focus on writing clean code, building RESTful APIs, and using Git for version control.
"""

sample_job_desc = """
Looking for a Backend Software Engineer with expertise in Python, Flask, and SQL databases. 
Must understand REST APIs, software architecture, and Git workflows.
"""

if __name__ == "__main__":
    score, keywords = calculate_match_score(sample_resume, sample_job_desc)
    print(f"--- Resume Matching System Results ---")
    print(f"Match Score: {score}%")
    print(f"Matched Core Keywords: {keywords}")
