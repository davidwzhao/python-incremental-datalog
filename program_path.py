relations = ["edge", "path"]

rules = [
        [("path", "x", "y"), ("edge", "x", "y")],
        [("path", "x", "z"), ("edge", "x", "y"), ("path", "y", "z")]
        ]
