import re
import html
import requests
from django.conf import settings
from .models import Vacancies

def clean_html(text):
    if not text:
        return ''
    text = str(text)
    text = re.sub(r'<[^>]+>','',text)
    text = html.unescape(text)
    text = text.replace("\r\n"," ")
    text = text.replace("\r",' ')
    text = text.replace('\n',' ')
    text = re.sub(r'\s+','',text).strip()
    return text

def parse_jooble():
    API_KEY = settings.JOOBLE_API_KEY
    url = f"https://jooble.org/api/{API_KEY}"

    added = 0

    LOCATIONS = ['Ukraine','Львів','Київ','Харків','Херсон']
    for location in LOCATIONS:
        for page in range(1,6):
            try:
                response = requests.post(
                    url,
                    json={
                        'keywords':'Python',
                        'location':location,
                        "page":page
                    },
                    timeout = 10
                )
            except requests.RequestException:
                continue
            if response.status_code != 200:
                continue

            data = response.json()
            jobs = data.get('jobs',[])
            if not jobs:
                break
            for job in jobs:
                title = clean_html(job.get('title',''))
                if not title:
                    continue
                company = clean_html(job.get('company','')) or 'Не вказано'
                location_name = clean_html(job.get('location','')) or 'Не вказано'
                source_url = job.get('link','')
                description = clean_html(job.get('snippet',''))
                description = description[:1500]
                salary = 0
                salary_text= str(job.get('salary',''))
                numbers = re.findall(r'\d+',salary_text)
                if numbers:
                    try:
                        salary = float(numbers[0])
                    except ValueError:
                        salary = 0
                if source_url and Vacancies.objects.filter(
                    source_url = source_url
                ).exists():
                    continue
                Vacancies.objects.create(
                    title = title,
                    description = description,
                    salary = salary,
                    company = company,
                    location = location_name,
                    source_url=source_url
                )
                added += 1
    return added
