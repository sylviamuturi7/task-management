# Test script for task management system
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, get_tasks

def test_validation_functions():
    print("=== TESTING VALIDATION FUNCTIONS ===")
    
    # Test validate_task_title
    print("\n1. Testing validate_task_title:")
    
    # Valid titles
    valid_titles = ["Groceries", "Study for exam", "Call mom"]
    for title in valid_titles:
        result = validate_task_title(title)
        print(f"  '{title}' -> {result}")
    
    # Invalid titles
    invalid_titles = ["", "Hi", "A" * 101, None, 123]
    for title in invalid_titles:
        result = validate_task_title(title)
        print(f"  '{title}' -> {result}")
    
    # Test validate_task_description
    print("\n2. Testing validate_task_description:")
    
    # Valid descriptions
    valid_descs = ["Buy groceries at store", "Study Python for 2 hours", "Call mom about weekend plans"]
    for desc in valid_descs:
        result = validate_task_description(desc)
        print(f"  '{desc}' -> {result}")
    
    # Invalid descriptions
    invalid_descs = ["", "Hi", "A" * 501, None, 123]
    for desc in invalid_descs:
        result = validate_task_description(desc)
        print(f"  '{desc}' -> {result}")
    
    # Test validate_due_date
    print("\n3. Testing validate_due_date:")
    
    # Valid dates (future dates)
    valid_dates = ["2024-12-25", "2025-01-01", "2024-07-04"]
    for date in valid_dates:
        result = validate_due_date(date)
        print(f"  '{date}' -> {result}")
    
    # Invalid dates
    invalid_dates = ["", "2024-01-01", "invalid-date", "2024-13-01", None, 123]
    for date in invalid_dates:
        result = validate_due_date(date)
        print(f"  '{date}' -> {result}")

def test_task_functions():
    print("\n=== TESTING TASK FUNCTIONS ===")
    
    # Clear any existing tasks
    global tasks
    from task_manager.task_utils import tasks
    tasks.clear()
    
    # Test add_task with valid data
    print("\n1. Testing add_task with valid data:")
    result1 = add_task("Groceries", "Buy groceries at Market Basket", "2024-12-25")
    result2 = add_task("Study", "Study Python for final exam", "2024-12-30")
    print(f"  Added task 1: {result1}")
    print(f"  Added task 2: {result2}")
    
    # Test add_task with invalid data
    print("\n2. Testing add_task with invalid data:")
    result3 = add_task("", "Invalid title", "2024-12-25")
    result4 = add_task("Valid title", "Hi", "2024-12-25")
    result5 = add_task("Valid title", "Valid description", "2024-01-01")
    print(f"  Empty title: {result3}")
    print(f"  Short description: {result4}")
    print(f"  Past date: {result5}")
    
    # Show current tasks
    print("\n3. Current tasks:")
    current_tasks = get_tasks()
    for i, task in enumerate(current_tasks):
        print(f"  [{i}] {task['title']} - {task['completed']}")
    
    # Test mark_task_as_complete
    print("\n4. Testing mark_task_as_complete:")
    result6 = mark_task_as_complete(0)  # Valid index
    result7 = mark_task_as_complete(5)  # Invalid index
    result8 = mark_task_as_complete(0)  # Already completed
    print(f"  Mark index 0 complete: {result6}")
    print(f"  Mark index 5 complete: {result7}")
    print(f"  Mark index 0 complete again: {result8}")
    
    # Test view_pending_tasks
    print("\n5. Testing view_pending_tasks:")
    pending = view_pending_tasks()
    print(f"  Pending tasks returned: {len(pending)}")
    
    # Test calculate_progress
    print("\n6. Testing calculate_progress:")
    progress = calculate_progress()
    print(f"  Progress: {progress}")

def test_edge_cases():
    print("\n=== TESTING EDGE CASES ===")
    
    # Clear tasks
    from task_manager.task_utils import tasks
    tasks.clear()
    
    # Test empty task list
    print("\n1. Testing with empty task list:")
    progress = calculate_progress()
    pending = view_pending_tasks()
    print(f"  Progress with no tasks: {progress}")
    print(f"  Pending tasks with no tasks: {len(pending)}")
    
    # Test mark complete on empty list
    result = mark_task_as_complete(0)
    print(f"  Mark complete on empty list: {result}")
    
    # Add one task and test
    add_task("Single Task", "Only one task", "2024-12-25")
    print("\n2. Testing with single task:")
    progress = calculate_progress()
    print(f"  Progress with 1 incomplete task: {progress}")
    
    # Complete the single task
    mark_task_as_complete(0)
    progress = calculate_progress()
    print(f"  Progress with 1 complete task: {progress}")

if __name__ == "__main__":
    test_validation_functions()
    test_task_functions()
    test_edge_cases()
    print("\n=== TESTING COMPLETE ===")
