import pickle

"""
A class for saving and loading pickle files.
"""
class SaveLoad:
    """
    A method for saving data to a pickle file.

    @param data what to save to the file
    @param name what to name the file
    """
    @staticmethod
    def save_game(data, name):
        data_file = open("LoadGame/"+name+".pickle", "wb")
        pickle.dump(data, data_file)

    """
    A method for loading data from a pickle file.
    
    @param name the name of the file to load
    """
    @staticmethod
    def load_game(name):
        data_file = open("LoadGame/"+name+".pickle", "rb")
        data = pickle.load(data_file)
        return data
