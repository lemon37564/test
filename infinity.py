for i in range(10):
    with open(f"inf{i}.py", "w") as f:
        for i in range(100000000):
            f.write("\n")
        f.write("print(\"hello world\")")
