from .validation import validate_task_title, validate_task_description, validate_due_date

# Global list to store tasks
tasks = []

def add_task(title, description, due_date):
    # Add a new task to the tasks list after validation
    # Validate all inputs
    if not validate_task_title(title):
        return False
    
    if not validate_task_description(description):
        return False
    
    if not validate_due_date(due_date):
        return False
    
    # Create task dictionary with specified structure
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }
    
    # Add to tasks list
    tasks.append(task)
    print(f"Task '{title}' added successfully!")
    return True


def mark_task_as_complete(task_index):
    # Mark a task as complete by its index
    if not isinstance(task_index, int):
        print("Error: Please enter a valid number for task index.")
        return False
    
    if task_index < 0 or task_index >= len(tasks):
        print(f"Error: Task index {task_index} is out of range. Valid range: 0-{len(tasks)-1}")
        return False
    
    if tasks[task_index]["completed"]:
        print(f"Task '{tasks[task_index]['title']}' is already completed.")
        return False
    
    tasks[task_index]["completed"] = True
    print(f"Task '{tasks[task_index]['title']}' marked as complete!")
    return True


def view_pending_tasks():
    # Display all pending (incomplete) tasks
    pending_tasks = []
    
    print("\n--- PENDING TASKS ---")
    
    if not tasks:
        print("No tasks found.")
        return pending_tasks
    
    found_pending = False
    
    for i, task in enumerate(tasks):
        if not task["completed"]:
            pending_tasks.append(task)
            status = "○" if not task["completed"] else "✓"
            print(f"[{i}] {status} {task['title']}")
            print(f"    Description: {task['description']}")
            print(f"    Due Date: {task['due_date']}")
            print()
            found_pending = True
    
    if not found_pending:
        print("No pending tasks found.")
    
    return pending_tasks


def calculate_progress():
    # Calculate and return the progress of task completion
    total_tasks = len(tasks)
    
    if total_tasks == 0:
        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_percentage": 0.0
        }
    
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    completion_percentage = (completed_tasks / total_tasks) * 100
    
    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_percentage": round(completion_percentage, 2)
    }


def view_all_tasks():
    # Display all tasks with their completion status
    print("\n--- ALL TASKS ---")
    
    if not tasks:
        print("No tasks found.")
        return tasks
    
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "○"
        completion_status = "Completed" if task["completed"] else "Pending"
        print(f"[{i}] {status} {task['title']} ({completion_status})")
        print(f"    Description: {task['description']}")
        print(f"    Due Date: {task['due_date']}")
        print()
    
    return tasks


def get_tasks():
    # Get the list of all tasks
    return tasks
