vacancies = [
    {"name": "Python Developer",
      "city": "Київ",
      'position':'remote',
        "salary": 60000 },
      {"name": "Frontend Engineer",
        "city": "Львів",
        'position':'Office',
          "salary": 55000},
    {"name": "Data Scientist",
      "city": "Одеса",
      'position':'remote',
        "salary": 75000},
    {"name": "UX/UI Designer",
      "city": "Харків",
      'position':'Office',
        "salary": 45000},
    {"name": "Project Manager",
      "city": "Київ",
      'position':'remote',
        "salary": 65000},
    {"name": "QA Manual Tester",
      "city": "Дніпро",
      'position':'remote',
        "salary": 35000},
    {"name": "DevOps Engineer",
      "city": "Львів",
      'position': 'Office',
        "salary": 80000},
    {"name": "Digital Marketer",
      "city": "Вінниця",
      'position':'remote',
        "salary": 30000},
    {"name": "Technical Writer",
      "city": "Київ",
      'position':'Office',
        "salary": 40000},
    {"name": "System Administrator",
      "city": "Запоріжжя",
      'position':'remote',
        "salary": 32000}
]
def menu():
  print('1.Всі вакансії')
  print('2.Вакансії за містом')
  print('3.Вакансії за зарплатою')
  print('4.Тільки Remote')
  print('5.Середня зарплата')
  print('6.Найдорожча вакансія')
  print('7.Вийти')
def choise():
  while True:
    menu()
    choose = int(input('Виберіть дію '))
    if choose == 7:
      break
    elif choose == 1:
        for i in vacancies:
          print(f'Посада: {i['name']}, місто: {i['city']} , розміщення: {i['position']} , зарплата: {i['salary']}')
    elif choose == 2:
      country = input('Вкажіть місто: ')
      country = country.lower()
      for i in vacancies:
          i["city"] = i["city"].lower()
          if country in i["city"]:
            print(f'Посада: {i['name']}, місто: {i['city'].capitalize()} , розміщення: {i['position']} , зарплата: {i['salary']}')
    elif choose == 3:
        salary_amount = int(input('Вкажіть зарплату(від): '))
        for i in vacancies:
          if i["salary"] >= salary_amount:
            print(f'Посада: {i['name']}, місто: {i['city']} , розміщення: {i['position']} , зарплата: {i['salary']}')
    elif choose == 4:
        for i in vacancies:
          if 'remote' in i["position"]:
            print(f'Посада: {i['name']}, місто: {i['city']} , зарплата: {i['salary']}')
    elif choose == 5:
       summary = sum(i['salary'] for i in vacancies)
       number = sum(1 for i in vacancies if 'salary' in i)
       print(f'Середня зарплата {summary//number}')
    elif choose == 6:
      highest_ = vacancies[0]
      for i in vacancies:
         if i["salary"] > highest_['salary']:
            highest_ = i
      print(f'Посада: {highest_['name']}, місто: {highest_['city'].capitalize()} , розміщення: {highest_['position']} , зарплата: {highest_['salary']}')
    else:
        print('Невірне значення!')
choise()