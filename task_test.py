# Quick test to verify improvements
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
from task_manager.task_utils import add_task, mark_task_as_complete, calculate_progress, get_tasks

print("=== QUICK VALIDATION TEST ===")

# Test 1: Valid inputs
print("\n1. Testing valid inputs:")
print(f"Valid title 'Homework': {validate_task_title('Homework')}")
print(f"Valid description: {validate_task_description('Complete math homework chapter 5')}")
print(f"Valid future date: {validate_due_date('2025-12-25')}")

# Test 2: Invalid inputs with better error messages
print("\n2. Testing invalid inputs:")
print(f"Empty title: {validate_task_title('')}")
print(f"Short title: {validate_task_title('Hi')}")
print(f"Number as title: {validate_task_title(123)}")

print(f"Empty description: {validate_task_description('')}")
print(f"Short description: {validate_task_description('Hey')}")
print(f"Number as description: {validate_task_description(456)}")

print(f"Empty date: {validate_due_date('')}")
print(f"Invalid date format: {validate_due_date('invalid')}")
print(f"Number as date: {validate_due_date(789)}")

# Test 3: Task operations
print("\n=== QUICK TASK TEST ===")

# Clear tasks
from task_manager.task_utils import tasks
tasks.clear()

# Add valid task
print("\n3. Testing task operations:")
result = add_task("Test Task", "This is a test task description", "2025-01-01")
print(f"Add valid task: {result}")

# Try to add invalid task
result = add_task("", "Short desc", "2025-01-01")
print(f"Add task with empty title: {result}")

# Show tasks
print(f"\nCurrent tasks: {len(get_tasks())}")
for i, task in enumerate(get_tasks()):
    print(f"  [{i}] {task['title']} - Completed: {task['completed']}")

# Mark complete
result = mark_task_as_complete(0)
print(f"Mark task 0 complete: {result}")

# Show progress
progress = calculate_progress()
print(f"Progress: {progress}")

print("\n=== TEST COMPLETE ===")
