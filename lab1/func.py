import pickle

def pkl_dump(path, model):
    with open(path, 'wb') as file:
        pickle.dump(model, file)

def pkl_read(path):
    with open(path, 'rb') as file:
        return pickle.load(file)
