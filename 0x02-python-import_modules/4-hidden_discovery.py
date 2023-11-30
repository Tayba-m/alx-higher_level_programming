#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for t in dir(hidden_4):
        if t[:2] != "__":
            print(t)
