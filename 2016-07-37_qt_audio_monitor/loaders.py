import pickle
import os

def load_model_pararms(model_class, folder, param_file):
    with open(param_file, 'rb') as f:
        params = pickle.load(f)

    model = model_class(*params)

    model.load_weights(os.path.join(folder, 'weights/weights.h5'))

    return model