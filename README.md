# Todo List Application

A simple Django-based Todo List application to manage tasks efficiently.

## Features
- Add, edit, and delete tasks
- Mark tasks as completed
- User-friendly interface
- SQLite database support

## Installation

### Prerequisites
- Python 3.x installed
- Django installed (`pip install django`)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/TodoList.git
   cd TodoList-main/to_do_list/todo_main

2. install dependencies:
   ```sh
    pip install -r requirements.txt
   
3. Apply database migrations:
   ```sh
   python manage.py migrate

3. run server:
   ```sh
   python manage.py runserver

5.Open your browser and visit: http://127.0.0.1:8000/

### Project Structure
```sh
TodoList-main/
│-- to_do_list/
│   ├── todo_main/  # Main Django project folder
│   │   ├── templates/  # HTML templates
│   │   ├── todo/  # App containing models and views
│   │   ├── manage.py  # Django management script
│   │   ├── db.sqlite3  # SQLite database file

    
  

