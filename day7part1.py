class folder:
    def __init__(self, name, parent, contents):
        self.name = name
        self.parent = parent
        self.contents = contents  # should be int


sizes = {}

prev_folder = None
curr_folder = None

f = open("day7test.txt", "r")
for line in f.readlines():
    if line[0:4] == "$ cd":
        curr_folder = folder()
        if curr_folder.name in sizes:
            sizes[prev_folder.name] += prev_folder.contents
        else:
            sizes[prev_folder.name] = prev_folder.contents
