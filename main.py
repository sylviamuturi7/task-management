from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, view_all_tasks

def show_menu():
    # Display the main menu options
    print("\n" + "="*50)
    print("TASK MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add a new task")
    print("2. Mark task as complete")
    print("3. View pending tasks")
    print("4. View all tasks")
    print("5. View progress")
    print("6. Exit")
    print("="*50)


def get_user_choice():
    # Get and validate user menu choice
    while True:
        try:
            choice = input("Enter your choice (1-6): ").strip()
            choice_num = int(choice)
            
            if 1 <= choice_num <= 6:
                return choice_num
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


def add_new_task():
    # Handle adding a new task
    print("\n--- Add New Task ---")
    
    # Get task title
    while True:
        title = input("Enter task title: ").strip()
        if title:
            break
        print("Task title cannot be empty.")
    
    # Get task description
    while True:
        description = input("Enter task description: ").strip()
        if description:
            break
        print("Task description cannot be empty.")
    
    # Get due date
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        if due_date:
            break
        print("Due date cannot be empty.")
    
    # Add the task
    add_task(title, description, due_date)


def complete_task():
    # Handle marking a task as complete
    print("\n--- Mark Task as Complete ---")
    
    # Show pending tasks first
    view_pending_tasks()
    
    # Get task index
    while True:
        try:
            task_index = input("Enter task index to mark complete (or 'cancel' to go back): ").strip()
            
            if task_index.lower() == 'cancel':
                return
            
            task_index_num = int(task_index)
            mark_task_as_complete(task_index_num)
            break
                
        except ValueError:
            print("Invalid input. Please enter a valid task number (0, 1, 2, etc.).")


def view_pending():
    # Handle viewing pending tasks
    view_pending_tasks()


def view_all():
    # Handle viewing all tasks
    view_all_tasks()


def view_progress():
    # Handle viewing task progress
    print("\n--- Task Progress ---")
    progress = calculate_progress()
    
    # Get detailed stats for display
    from task_manager.task_utils import get_tasks
    all_tasks = get_tasks()
    total_tasks = len(all_tasks)
    completed_tasks = sum(1 for task in all_tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Completion rate: {progress}%")
    
    if total_tasks > 0:
        bar_length = 20
        filled_length = int(progress / 5)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        print(f"\nProgress: {bar}")
        print(f"         {progress}%")


def main():
    # Main function to run the task management system
    print("Welcome to the Task Management System!")
    
    # Main program loop
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == 1:
            add_new_task()
        elif choice == 2:
            complete_task()
        elif choice == 3:
            view_pending()
        elif choice == 4:
            view_all()
        elif choice == 5:
            view_progress()
        elif choice == 6:
            print("\nThank you for using the Task Management System!")
            print("Goodbye!")
            break
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
