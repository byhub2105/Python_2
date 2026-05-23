from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Home</h2> <a href="/about">About</a> <a href="/contacts"> Contacts</a> <a href="/products">Products</a> <a href="/students">Students</a> <a href="/profile">Profile</a>')
def about(request):
    return HttpResponse('<h2>About</h2> <a href="/">Return</a>')
def contacts(request):
    return HttpResponse('<h2>Contacts</h2> <a href="/">Return</a>')
def products(request):
    return HttpResponse('<h2>Наші товари</h2> <ul><li>Ноутбук</li><li>Миша</li><li>Клавіатура</li></ul> <a href="/">Return</a>')
def students(request):
    return HttpResponse('<table border="1">'
    '<thead>'
    '        <tr>'
    '           <th>Імя</th><th>Вік</th>'
    '<th>Курс</th>'
    '       </tr>'
    '   </thead>'
    '   <tbody>'
    '       <tr>'
    '           <td>Іван</td>'
    '           <td>18</td>'
    '           <td>Python</td>'
    '       </tr>'
    '       <tr>'
    '           <td>Марія</td>'
    '           <td>20</td>'
    '           <td>Django</td>'
    '       </tr>'
    '   </tbody>'
    '</table>' \
    '<a href="/">Return</a>')
def profile(request):
    name = 'Іван'
    age = 18
    city = 'Київ'
    return HttpResponse(f'''<h2>Профіль користувача</h2> <p>Ім\'я: {name}</p><p>Вік: {age}</p><p>Місто: {city}</p> <a href="/">Return</a>''')