# specify a datalog program here
relations = ["alloc", "assign", "load", "store", "vpt", "alias"]

# rules
rules = [
        [("vpt", "a", "b"), ("alloc", "a", "b")],
        [("vpt", "a", "o"), ("assign", "a", "b"), ("vpt", "b", "o")],
        [("vpt", "v", "o"), ("load", "v", "y", "f"), ("store", "p", "f", "q"), ("vpt", "q", "o"), ("vpt", "p", "al"), ("vpt", "y", "al")],
        [("alias", "v1", "v2"), ("vpt", "v1", "o"), ("vpt", "v2", "o")]
        ]

