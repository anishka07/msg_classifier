import os

root = os.getcwd()


def get_vectorizer_path():
    return os.path.join(root, "/pkls/vectorizer.pkl")


def get_model_path():
    return os.path.join(root, "/pkls/model.pkl")


class Settings:
    MODEL_PATH = get_model_path()
    VECTORIZER_PATH = get_vectorizer_path()
