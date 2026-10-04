items = ["red", "blue", "green", "red", "yellow"]

seen = []

for item in items:
    if item in seen:
        print("Duplicate found:", item)
        break

    seen.append(item)