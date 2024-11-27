import pickle

# Open the pickle file in binary read mode
with open("data.pickle", "rb") as file:
    # Unpickle the python object and save it to loaded_data
    loaded_data = pickle.load(file)

# Print the deserialized data
print("Deserialized data:", loaded_data)
