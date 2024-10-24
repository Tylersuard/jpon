import ast


class JPONDecodeError(Exception):
    def __init__(self, message, expression=None):
        super().__init__(message)
        self.expression = expression


def dumps(py_obj):
    """
    Converts a Python object to a JPON-formatted string.

    Args:
        py_obj (dict or list): The Python object to be converted.

    Returns:
        str: A string of the object
    """
    return str(py_obj)


def loads(jpon_string):
    """
    Converts a JPON-formatted string (using Python syntax) to a Python object.

    Args:
        jpon_string (str): The JPON string to be parsed.

    Returns:
        dict or list: The resulting Python object.
    """
    try:
        # Strip leading/trailing whitespace to handle multiline strings
        jpon_string = jpon_string.strip()
        # Use ast.literal_eval to safely evaluate Python-like expressions
        py_obj = ast.literal_eval(jpon_string)
        if not isinstance(py_obj, (dict, list)):
            raise JPONDecodeError("JPON should be a dictionary or list format.")
        return py_obj
    except (SyntaxError, ValueError) as e:
        raise JPONDecodeError(
            "Error parsing JPON: Invalid syntax. Please check for proper Python-style formatting.",
            expression=jpon_string,
        ) from e
    except Exception as e:
        raise JPONDecodeError(f"Error parsing JPON: {e}", expression=jpon_string) from e


# Example Usage
if __name__ == "__main__":
    # Define a JPON string using Python syntax
    jpon_str = """
    {
        'name': 'Alice',
        'age': 30,
        'is_student': False,
        'hobbies': ['reading', 'hiking', 'coding']
    }
    """

    try:
        # Convert JPON to Python dict
        data = loads(jpon_str)
        print("Parsed JPON to Python object:")
        print(data)

        # Convert Python dict back to JPON
        jpon_str_converted = dumps(data)
        print("\nConverted Python object to JPON string:")
        print(jpon_str_converted)
    except JPONDecodeError as e:
        print("\nJPON Decode Error:")
        print(e)
        if e.expression:
            print("Problematic expression:")
            print(e.expression)
