import pickle

import config


def prediction_price(data):

    try:
        area = float(data["area"])
        bedrooms = float(data['bedrooms'])
        age = int(data['age'])

        with open(config.MODEL_PATH, 'rb') as f:
            model = pickle.load(f)

        response = model.predict([[area, bedrooms, age]])
        return response[0]
    except ValueError:
        return -1


