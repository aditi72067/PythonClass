file_name = "data.csv"

def read_csv(file_name):
    with open(file_name, "r") as fileHandle:
        data = fileHandle.read()

    # Split by lines
    l1 = data.strip().split('\n')

    # Split each line by commas
    l2 = [line.split(",") for line in l1]

    return l2

receivedData = read_csv(file_name)
print(receivedData)
