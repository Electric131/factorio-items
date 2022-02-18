import os

path = "./raw_data.txt"

data = []

if __name__ == "__main__":
    # Read Raw Data and trim any repeating values
    with open(path, "r") as f:
        rawData = f.read()

    for tempData in rawData.split("\n"):
        if not tempData in data:
            data.append(tempData)

    with open("unique_data.txt", "w") as f:
        f.write("\n".join(data))