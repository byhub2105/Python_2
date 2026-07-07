from django.shortcuts import render

vacancies = [
    {
        "id": 1,
        "salary":1000,
        "title": "Frontend React Developer",
        "company": "WebCraft Studio",
        "city": "Львів",
        "experience": "2 роки",
        "employment_type": "Повна зайнятість",
        "work_format": "Гібридний",
        "skills": ["JavaScript", "React", "Redux", "HTML5", "CSS3", "Git", "TypeScript"]
    },
    {
        "id": 2,
        "salary":1300,
        "title": "Python Backend Developer",
        "company": "DataByte Solutions",
        "city": "Київ",
        "experience": "4 роки",
        "employment_type": "Повна зайнятість",
        "work_format": "Віддалено",
        "skills": ["Python", "Django", "FastAPI", "PostgreSQL", "Docker", "REST API", "AWS"]
    },
    {
        "id": 3,
        "salary":900,
        "title": "QA Automation Engineer",
        "company": "QualityFirst",
        "city": "Харків",
        "experience": "1.5 року",
        "employment_type": "Повна зайнятість",
        "work_format": "В офісі",
        "skills": ["Java", "Selenium", "TestNG", "Maven", "Git", "Jira", "SQL"]
    },
    {
        "id": 4,
        "salary":1000,
        "title": "DevOps Engineer",
        "company": "CloudSystems Corp",
        "city": "Одеса",
        "experience": "5 років",
        "employment_type": "Повна зайнятість",
        "work_format": "Віддалено",
        "skills": ["Linux", "Kubernetes", "Docker", "Terraform", "CI/CD (Jenkins/GitHub Actions)", "Ansible"]
    },
    {
        "id": 5,
        "salary":1000,
        "title": "Data Scientist",
        "company": "AI Innovations",
        "city": "Дніпро",
        "experience": "3 роки",
        "employment_type": "Часткова зайнятість",
        "work_format": "Гібридний",
        "skills": ["Python", "Machine Learning", "Pandas", "NumPy", "SQL", "Scikit-Learn", "Tableau"]
    },
    {
        "id": 6,
        "salary":1300,
        "title": "iOS Developer",
        "company": "AppStudio Mobile",
        "city": "Івано-Франківськ",
        "experience": "2.5 роки",
        "employment_type": "Повна зайнятість",
        "work_format": "Віддалено",
        "skills": ["Swift", "UIKit", "SwiftUI", "CoreData", "Git", "Xcode", "REST API"]
    }

]
def home(request):
    context = {
        'vacancies':vacancies,
        'title':'Сайт пошуку роботи',
        'vacancies_count':len(vacancies)
    }
    return render(request,'app1/index.html',context)
def about(request, vacancy_id):

    vacancy = next(
        (item for item in vacancies if item['id'] == vacancy_id),
        None
        )
    context = {
        'vacancy':vacancy
    }
    return render(request,'app1/about.html',context)
