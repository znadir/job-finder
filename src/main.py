import os
import docx
from utils import add_hyperlink
from searchJobs import searchJobs

location = input("Ou habitez-vous? (Laval): ") or "Laval"
query = input("Search emplois (Stage programmation informatique): ") or "Stage programmation informatique"
must_keywords = input("Must include (stage): ") or "stage"
must_keywords = must_keywords.replace(" ", "").split(",")

my_jobs = []

my_jobs += searchJobs("https://emplois.ca.indeed.com/jobs?q=", '.jobsearch-ResultsList > li', '.jobTitle span', '.jobTitle > a', '.job-snippet', query, must_keywords)
my_jobs += searchJobs(f"https://ca.jooble.org/SearchResult?rgns={location}%2C%20QC&ukw=", "div > article", "a", "a", "section > div > div", query, must_keywords)
my_jobs += searchJobs(f"https://www.option-carriere.ca/recherche/emplois?l={location}&radius=10&sort=relevance&s=", "ul.jobs li", "header h2 a", "header h2 a", "div.desc", query, must_keywords)

doc = docx.Document()
doc.add_heading(f"Recherche d'emploi: {query}", 0)

for job in my_jobs:
    p = doc.add_paragraph()
    p.add_run(job['title']).bold = True
    doc.add_paragraph(job['snippet'])
    p = doc.add_paragraph()
    add_hyperlink(p, "Voir l'offre emploi", job['link'])
    doc.add_paragraph()

file_path = os.path.join(os.path.dirname(__file__), "../files/jobs.docx")
doc.save(file_path)