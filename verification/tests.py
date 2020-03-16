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
            "input": ['muchlonger'],
            "answer": False,
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
        }
    ],
    "Extra": [
        {
            "input": ['this is password'],
            "answer": False,
        }
    ]
}
