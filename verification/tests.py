"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['short'],
            "answer": False,
        },
        {
            "input": ['short54'],
            "answer": True,
        },
        {
            "input": ['muchlonger'],
            "answer": True,
        },
        {
            "input": ['ashort'],
            "answer": False,
        },
        {
            "input": ['muchlonger5'],
            "answer": True,
        },
        {
            "input": ['sh5'],
            "answer": False,
        },
        {
            "input": ['1234567'],
            "answer": False,
        },
        {
            "input": ['12345678910'],
            "answer": True,
        },
        {
            "input": ['password12345'],
            "answer": False,
        },
        {
            "input": ['PASSWORD12345'],
            "answer": False,
        },
        {
            "input": ['pass1234word'],
            "answer": True,
        },
    ],
    "Extra": [
        {
            "input": ['this is password'],
            "answer": False,
        }
    ]
}
