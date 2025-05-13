import json
from datetime import datetime
from colorama import Fore, init
from unicodedata import category

init(autoreset=True)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, default=str)

def main():
    tasks = load_tasks()
    categories = ['Work', 'Home', 'Family', 'Other']

    while True:
        print(Fore.CYAN + '\n===TODO List ===')
        print('1. Add task')
        print('2. Show list of tasks')
        print('3. Remove task')
        print('4. Change category')
        print('5. Show by category')
        print('6. Change status')
        print('7. Change deadline')
        print('8. Exit')


        choice = input(Fore.YELLOW + 'Enter your choice: ')

        if choice == '1':
            task = input('Enter your task: ')

            print('\nCategories:')
            for idx, cat in enumerate(categories,1):
                print(f'{idx}. {cat}')
            cat_choice = int(input('Number of category: ')) - 1
            category = categories[cat_choice] if 0 <= cat_choice < len(categories) else 'Other'

            # Enter the time of deadline
            deadline = input('Deadline (dd.mm.yyyy or Enter): ')
            try:
                deadline = datetime.strptime(deadline, '%d.%m.%Y') if deadline else None
            except ValueError:
                print(Fore.RED + 'Invalid deadline')
                deadline = None

            tasks.append({
                "task" : task,
                "done" : False,
                "category" : category,
                "deadline" : deadline
            })

            save_tasks(tasks)
            print('Task added!')
        elif choice == '2':
            # Sorted by deadline (first overdue)
            sorted_tasks = sorted(tasks, key=lambda k: k['deadline'] or datetime.max)

            print(Fore.MAGENTA +'\nList of tasks:')
            for idx, task in enumerate(tasks, 1):
                status = Fore.GREEN + '✓' if task['done'] else Fore.RED + ''
                category = Fore.BLUE + f"({task['category']})"
                deadline = ""
                if task['deadline']:
                    if task['deadline'] < datetime.now():
                        deadline = Fore.RED +"[OVERDUE]"
                    else:
                        deadline = Fore.YELLOW + f" [before {task['deadline'].strftime('%d.%m.%Y')}]"
                print(f'{idx}. [{status}] {task["task"]} {category}{deadline}')
        elif choice == '3':
            if not tasks:
                print('No tasks added.')
                continue

            print('List of tasks:')
            for idx, task in enumerate(tasks, 1):
                print(f'{idx}. {task["task"]}')

            try:
                task_num = int(input('\nNumber of task for remove: ')) - 1
                if 0 <= task_num < len(tasks):
                    deleted_task = tasks.pop(task_num)
                    print(f'Task "{deleted_task['task']}" removed!')
                else:
                    print('Invalid numer of task.')
            except ValueError:
                print('Invalid number.')
        elif choice == '4':
            if not tasks:
                print(Fore.RED +'No tasks added.')
                continue

            print('List of tasks:')
            for idx, task in enumerate(tasks, 1):
                print(f'{idx}. {task["task"]} ({task["category"]})')

            try:
                task_num = int(input('\nNumber of task for change: ')) - 1
                if 0 <= task_num < len(tasks):
                    # Choose new category
                    print("\nNew category:")
                    for idx, cat in enumerate(categories, 1):
                        print(f'{idx}. {cat}')
                    new_cat = int(input('\nNew category number: ')) - 1
                    tasks[task_num]['category'] = categories[new_cat]
                    save_tasks(tasks)
                    print(Fore.GREEN+'Task changed.!')
                else:
                    print(Fore.RED +'Invalid number.')
            except (ValueError, IndexError):
                print(Fore.RED +'Invalid number.')
        elif choice == '5':
            print('\nCategories:')
            for idx, cat in enumerate(categories,1):
                print(f'{idx}. {cat}')
            cat_choice = int(input('Number of category')) - 1

            if 0 <= cat_choice < len(categories):
                filtered = [t for t in tasks if t["category"] == categories[cat_choice]]
                print(f'Categories filtered: {len(filtered)}')
                for idx, task in enumerate(filtered, 1):
                    print(f'{idx}. {task["task"]}')
            else:
                print(Fore.RED + 'Invalid category.')
        elif choice == '6':
            if not tasks:
                print(Fore.RED +'No tasks added.')
                continue
            print('List of tasks:')
            for idx, task in enumerate(tasks, 1):
                print(f'{idx}. {task["task"]}')
            try:
                task_num = int(input('\nNumber of task for change: ')) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]['done'] = not tasks[task_num]['done']
                    status = 'done' if tasks[task_num]['done'] else ''
                    print(Fore.GREEN +f'Task {status}')
                else:
                    print(Fore.RED +'Invalid number.')
            except ValueError:
                print(Fore.RED +'Invalid number.')
        elif choice == '7':
            if not tasks:
                print(Fore.RED + 'No tasks added.')
                continue
            print('List of tasks:')
            for idx, task in enumerate(tasks, 1):
                print(f'{idx}. {task["task"]}')

            try:
                task_num = int(input('\nNumber of task for change: ')) - 1
                if 0 <= task_num < len(tasks):
                    deadline = input('Deadline (dd.mm.yyyy or Enter): ')
                    deadline = datetime.strptime(deadline, '%d.%m.%Y') if deadline else None
                    tasks[task_num]['deadline'] = deadline
                else:
                    print(Fore.RED +"Invalid deadline.")
            except ValueError:
                print(Fore.RED+"Invalid deadline.")
        else:
            save_tasks(tasks)
            break

if __name__ == '__main__':
    main()