import os

root = os.path.dirname(os.path.abspath(__file__))


def get_vectorizer_path():
    vectorizer_abs_path = os.path.join(root, "pkls/vec.pkl")
    return vectorizer_abs_path


def get_model_path():
    model_abs_path = os.path.join(root, "pkls/model.pkl")
    return model_abs_path


class Settings:
    MODEL_PATH = get_model_path()
    VECTORIZER_PATH = get_vectorizer_path()


print(root)
print(Settings.MODEL_PATH)
print(Settings.VECTORIZER_PATH)