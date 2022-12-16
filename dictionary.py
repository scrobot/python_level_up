import json

def save_dict(dict: dict, file: str) -> None:
    """Save dictionary to file"""
    with open(file, "w") as f:
        json.dump(dict, f)

def load_dict(file: str) -> dict:
    """Load dictionary from file"""
    with open(file, "r") as f:
        return json.load(f)

if __name__ == '__main__':
    save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
    print(load_dict('test.pickle'))
