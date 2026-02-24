# Debug script to find the exact error
print("=== DEBUGGING START ===")

try:
    print("1. Testing imports...")
    from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
    print("   ✅ Validation imports work")
    
    from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, view_all_tasks
    print("   ✅ Task utils imports work")
    
    print("2. Testing basic validation...")
    result = validate_task_title("Test")
    print(f"   ✅ Title validation: {result}")
    
    print("3. Testing date validation...")
    # Use a future date that should work
    result = validate_due_date("2025-12-25")
    print(f"   ✅ Date validation: {result}")
    
    print("4. Testing task operations...")
    result = add_task("Test Task", "Test description", "2025-12-25")
    print(f"   ✅ Add task: {result}")
    
    print("=== ALL TESTS PASSED ===")
    
except Exception as e:
    print(f"❌ ERROR FOUND: {e}")
    print(f"❌ ERROR TYPE: {type(e).__name__}")
    import traceback
    print("❌ FULL TRACEBACK:")
    traceback.print_exc()

print("=== DEBUGGING END ===")
