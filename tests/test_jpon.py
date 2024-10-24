import jpon


def test_loads():  # Define a jpon string using Python syntax
    jpon_str = """
    {
        'name': 'Alice',
        'age': 30,
        'is_student': False,
        'hobbies': ['reading', 'hiking', 'coding']
    }
    """

    # Convert jpon to Python dict
    data = jpon.loads(jpon_str)
    assert data is not None
    print("Parsed jpon to Python object:")
    print(data)


def test_dumps():
    data = {
        "name": "Alice",
        "age": 30,
        "is_student": False,
        "hobbies": ["reading", "hiking", "coding"],
    }
    # Convert Python dict back to jpon
    jpon_str_converted = jpon.dumps(data)
    print("\nConverted Python object to jpon string:")
    print(jpon_str_converted)
    assert jpon_str_converted is not None
