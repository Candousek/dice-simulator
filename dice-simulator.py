from random import randint

def getPercentage(data, number):
    result = data[number] / data["total"] * 100
    return f"{result:.2f}%"

data = {
    "total": 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

SIDES = {
    1: """
    [     ]
    [  X  ]
    [     ]
    """,
    2: """
    [X    ]
    [     ]
    [    X]
    """,
    3: """
    [X    ]
    [  X  ]
    [    X]
    """,
    4: """
    [X   X]
    [     ]
    [X   X]
    """,
    5: """
    [X   X]
    [  X  ]
    [X   X]
    """,
    6: """
    [X   X]
    [X   X]
    [X   X]
    """
}

while True:
    
    decision = input("""
    [B] Stop Rolling
    [S] Show statistics 
    [Enter] Roll
    >> Your choice: """).lower()

    match decision:
        case "b":
            break
        case "s":
            result = "\n>> Showing statistics:\n"
            for key in data:
                result += f"You rolled {key}: {data[key]} time{'s' if data[key] != 1 else ''} ({getPercentage(data, key)})\n"
            print(result)            
        case _:
            roll = randint(1, 6)
            data[roll] += 1
            data["total"] += 1
            print(f"{SIDES[roll]}Your rolled {roll}!")
