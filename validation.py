from datetime import datetime

def validate_task_title(title):
    # Validate task title to ensure it's not empty and has reasonable length
    if not title:
        print("Error: Task title cannot be empty.")
        return False
    
    if not isinstance(title, str):
        print("Error: Task title must be text.")
        return False
    
    # Check if title has at least 3 characters
    if len(title.strip()) < 3:
        print("Error: Task title must be at least 3 characters long.")
        return False
    
    # Check if title is not too long (max 100 characters)
    if len(title) > 100:
        print("Error: Task title cannot exceed 100 characters.")
        return False
    
    return True


def validate_task_description(description):
    # Validate task description to ensure it's not empty and has reasonable length
    if not description:
        print("Error: Task description cannot be empty.")
        return False
    
    if not isinstance(description, str):
        print("Error: Task description must be text.")
        return False
    
    # Check if description has at least 5 characters
    if len(description.strip()) < 5:
        print("Error: Task description must be at least 5 characters long.")
        return False
    
    # Check if description is not too long (max 500 characters)
    if len(description) > 500:
        print("Error: Task description cannot exceed 500 characters.")
        return False
    
    return True


def validate_due_date(due_date):
    # Validate due date to ensure it's in proper format and not in the past
    if not due_date:
        print("Error: Due date cannot be empty.")
        return False
    
    if not isinstance(due_date, str):
        print("Error: Due date must be text.")
        return False
    
    try:
        # Try to parse the date
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        
        # Accept any valid date format (no past date restriction)
        return True
        
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
        return False
