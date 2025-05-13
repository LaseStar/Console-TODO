import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def main():
    tasks = load_tasks()
    while True:
        print('\nTODO List:')
        print('1. Add task')
        print('2. Show list of tasks')
        print('3. Remove task')
        print('4. Check if task is done')
        print('5. Exit')


        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter your task: ')
            tasks.append({'task': task, 'done': False})
            print('Task added!')
        elif choice == '2':
            print('\nList of tasks:')
            for idx, task in enumerate(tasks, 1):
                status = '✓' if task['done'] else ''
                print(f'{idx}. [{status}] {task["task"]}')
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
                print('No tasks added.')
                continue

            print('List of tasks:')
            for idx, task in enumerate(tasks, 1):
                print(f'{idx}. {task["task"]}')

            try:
                task_num = int(input('\nNumber of task for remove: ')) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]['done'] = not tasks[task_num]['done']
                    status = 'done' if tasks[task_num]['done'] else ''
                    print(f'Task {status}')
                else:
                    print('Invalid number.')
            except ValueError:
                print('Invalid number.')
        else:
            save_tasks(tasks)
            break

if __name__ == '__main__':
    main()