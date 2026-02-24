from validation import validate_task_description, validate_task_priority, validate_task_id
import datetime

def create_task(description, priority='medium'):
    
    # Args:
    #     description (str): Task description
    #     priority (str): Task priority ('low', 'medium', 'high')
    #
    # Returns:
    #     dict: Task dictionary or None if validation fails
    # Validate inputs
    if not validate_task_description(description):
        print("Error: Invalid task description. Must be at least 3 characters and max 200 characters.")
        return None
    
    if not validate_task_priority(priority):
        print("Error: Invalid priority. Must be 'low', 'medium', or 'high'.")
        return None
    
    # Create task dictionary
    task = {
        'id': None,  # Will be set when added to tasks list
        'description': description.strip(),
        'priority': priority.lower(),
        'completed': False,
        'created_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'completed_date': None
    }
    
    return task


def add_task(tasks, description, priority='medium'):
    # Add a new task to the tasks list.
    #
    # Args:
    #     tasks (list): List of task dictionaries
    #     description (str): Task description
    #     priority (str): Task priority
    #
    # Returns:
    #     bool: True if task added successfully, False otherwise
    # Create new task
    new_task = create_task(description, priority)
    
    if new_task is None:
        return False
    
    # Assign ID (incremental)
    if tasks:
        max_id = max(task.get('id', 0) for task in tasks)
        new_task['id'] = max_id + 1
    else:
        new_task['id'] = 1
    
    # Add to tasks list
    tasks.append(new_task)
    return True


def mark_task_complete(tasks, task_id):
    # Mark a task as complete.
    #
    # Args:
    #     tasks (list): List of task dictionaries
    #     task_id (int): ID of task to mark complete
    #
    # Returns:
    #     bool: True if task marked complete successfully, False otherwise
    # Validate task ID
    if not validate_task_id(task_id, tasks):
        print(f"Error: Task with ID {task_id} not found.")
        return False
    
    # Find and update task
    for task in tasks:
        if task.get('id') == task_id:
            if task.get('completed', False):
                print(f"Task {task_id} is already completed.")
                return False
            
            task['completed'] = True
            task['completed_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
    
    return False


def get_pending_tasks(tasks):
    # Get list of pending (incomplete) tasks.
    #
    # Args:
    #     tasks (list): List of task dictionaries
    #
    # Returns:
    #     list: List of pending task dictionaries
    pending_tasks = []
    
    for task in tasks:
        if not task.get('completed', False):
            pending_tasks.append(task)
    
    return pending_tasks


def get_completed_tasks(tasks):
    # Get list of completed tasks.
    #
    # Args:
    #     tasks (list): List of task dictionaries
    #
    # Returns:
    #     list: List of completed task dictionaries
    completed_tasks = []
    
    for task in tasks:
        if task.get('completed', False):
            completed_tasks.append(task)
    
    return completed_tasks


def display_tasks(tasks, show_completed=False):
    # Display tasks in a formatted way.
    #
    # Args:
    #     tasks (list): List of task dictionaries
    #     show_completed (bool): Whether to show completed tasks
    if not tasks:
        print("No tasks to display.")
        return
    
    print("\n" + "="*60)
    if show_completed:
        print("COMPLETED TASKS")
    else:
        print("PENDING TASKS")
    print("="*60)
    
    for task in tasks:
        status = "✓" if task.get('completed', False) else "○"
        priority = task.get('priority', 'medium').upper()
        description = task.get('description', 'No description')
        task_id = task.get('id', 'N/A')
        
        print(f"[{task_id}] {status} [{priority}] {description}")
        
        if task.get('completed', False) and task.get('completed_date'):
            print(f"    Completed: {task['completed_date']}")
        elif task.get('created_date'):
            print(f"    Created: {task['created_date']}")
    
    print("="*60)


def get_task_stats(tasks):
    # Get task statistics.
    #
    # Args:
    #     tasks (list): List of task dictionaries
    #
    # Returns:
    #     dict: Dictionary with task statistics
    total_tasks = len(tasks)
    completed_count = len(get_completed_tasks(tasks))
    pending_count = len(get_pending_tasks(tasks))
    
    completion_rate = 0
    if total_tasks > 0:
        completion_rate = (completed_count / total_tasks) * 100
    
    stats = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_count,
        'pending_tasks': pending_count,
        'completion_rate': round(completion_rate, 2)
    }
    
    return stats
