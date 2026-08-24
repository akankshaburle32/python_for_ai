## Student marks should be in between 0 - 100 in number format.

class InvalidMarksError(Exception):
    """Raised when the marks are not in between 0-100"""
    pass

class InSufficientBalanceError(Exception):
    """Raised when the balance is less than exam fee"""
    pass

def get_valid_marks(subject_name : str) -> float:

    while True:
        
        try:
            raw_marks = input(f"Enter the marks for {subject_name} is between 0-100 : ")
            marks = float(raw_marks)

            if marks < 0 or marks > 100:
                raise InvalidMarksError(f"Invalid marks for {subject_name}, must be in between 0-100")

            return marks

        except ValueError as e:        
            print(f"Error : {e}")
        except InSufficientBalanceError as e:
            print(f"Error : {e}") 


if __name__ == "__main__":
    (get_valid_marks("Physics"))
    (get_valid_marks("Chemistry"))
    (get_valid_marks("Maths"))