def validate_task_description(description):
    """
    Validate task description to ensure it's not empty and has reasonable length.
    
    Args:
        description (str): The task description to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not description:
        return False
    
    if not isinstance(description, str):
        return False
    
    # Check if description has at least 3 characters
    if len(description.strip()) < 3:
        return False
    
    # Check if description is not too long (max 200 characters)
    if len(description) > 200:
        return False
    
    return True


def validate_task_priority(priority):
    """
    Validate task priority to ensure it's one of the accepted values.
    
    Args:
        priority (str): The task priority to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    valid_priorities = ['low', 'medium', 'high']
    
    if not isinstance(priority, str):
        return False
    
    return priority.lower() in valid_priorities


def validate_task_id(task_id, tasks):
    """
    Validate task ID to ensure it exists in the tasks list.
    
    Args:
        task_id (int): The task ID to validate
        tasks (list): List of task dictionaries
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(task_id, int):
        return False
    
    if task_id < 0:
        return False
    
    # Check if task ID exists in the tasks list
    for task in tasks:
        if task.get('id') == task_id:
            return True
    
    return False
