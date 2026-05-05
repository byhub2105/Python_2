from task import Task
from storage import save_tasks,load_tasks

def show_tasks(tasks):
    if not tasks:
        print('Задач ще немає')
        return
    for i,task in enumerate(tasks,1):
        status = '✅' if task.done else '❌'
        print(f'{i}.[{status}] {task.title} - {task.description}')
def add_tasks(tasks):
    title = input('Назва: ')
    description = input('Опис: ')
    tasks.append(Task(title,description))
    print('Задачу додано')
def mark_done(tasks):
    show_tasks(tasks)
    index = int(input('Номер задачі: ')) - 1
    if 0 <= index < len(tasks):
        tasks[index].done = True
def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("номер задачі: ")) -1
    if 0<= index < len(tasks):
        tasks.pop(index)
def main():
    tasks = load_tasks()
    while True:
        print('1.Показати задачі')
        print('2.Додати задачу')
        print('3.Виконати задачу')
        print('4.Видалити задачу')
        print('5.Вийти')
        choise = input('')
        if choise == '1':
            show_tasks(tasks)
        elif choise == '2':
            add_tasks(tasks)
        elif choise == '3':
            mark_done(tasks)
        elif choise == '4':
            delete_task(tasks)
        elif choise == '5':
            break
        else:
            print('введіть ще раз')
main()