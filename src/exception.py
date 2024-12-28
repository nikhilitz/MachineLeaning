import sys
import logging

def error_msg_detail(err, err_detail: sys):
    # This function formats and returns a detailed error message
    # It uses sys.exc_info() to get traceback details and format a custom error message
    _, _, exc_tb = err_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # File where the error occurred
    # Creating a custom error message with file, line number, and original error message
    err_msg = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(err))

    return err_msg

class CustomException(Exception):  # Inheriting from the built-in Exception class
    def __init__(self, err_msg, err_detail: sys):
        # Initialize the exception with the custom error message
        super().__init__(err_msg)  # Call parent class constructor with error message
        self.err_msg = error_msg_detail(err_msg, err_detail=err_detail)  # Format the detailed error message

    def __str__(self):
        # Return the detailed error message when the exception is printed
        return self.err_msg

# if __name__ == "__main__":
#     try:
#         a = 1 / 0  # Raise a ZeroDivisionError
#     except Exception as err:
#         logging.info("Error divide by zero")  # Log a simple message before raising the custom exception
#         raise CustomException(err, sys)  # Raise the custom exception with error and traceback details
