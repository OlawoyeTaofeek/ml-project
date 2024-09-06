import sys

def error_message_detail(error, error_detail: sys):
    """
    Custom error handler to display the error message, 
    the line where the error occurred, and the file name.

    Args:
        error (Exception): The exception that was raised.
        error_detail (sys): The sys module to extract error details.

    Returns: 
        str: Custom error message containing file name, line number, and error message.
    """
    _, _, exc_traceback = error_detail.exc_info()  # Retrieves exception type, value, and traceback.
    
    # Extract file name and line number from traceback.
    file_name = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno
    error_message = (
        f"Error occurred in python script: {file_name.split('/')[-1]} \n"
        f"Line number: {line_number} \n"
        f"Error message: {str(error)}"
    )

    return error_message


try:
    1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    message = error_message_detail(e, sys)
    print(message)