# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
from collections import defaultdict

lines = [line.strip() for line in open('./input.txt', 'r')]

dir_dict = defaultdict(int)
path = []
for line in lines:
    words = line.split()
    if words[1] == 'ls':
        continue
    elif words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    else:
        size = words[0]
        if size.isnumeric():
            for i in range(len(path)):
                dir_dict[f"{'/'.join(path[:i+1])}"] += int(size)

            # dir_dict[f"{'/'.join(path)}"] += int(size)
            # print(f"{'/'.join(path)}, ls = {words}, {size=}")

    # print(words)
# print(dir_dict)

# 70000000
# 50822529
# --------
# 19177471

print(f"part 1 = {sum(v for k, v in dir_dict.items() if v <= 100000)}")

total_space = 70_000_000
used_space = dir_dict['/']
free_space = total_space - used_space
need_to_free_up = 30_000_000 - free_space

# print(f"{need_to_free_up = }")
print(f"part 2 = {min(v for k, v in dir_dict.items() if v >= need_to_free_up)}")

# for k, v in dir_dict.items():
#     if v >= need_to_free_up:
#         print(v)
