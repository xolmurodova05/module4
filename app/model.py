import pickle

def load_model():
    with open('models/final_model.pkl', 'rb') as f:
        return pickle.load(f)

def make_prediction(model, country):
    # Placeholder logic for demo
    if country == "ALL":
        return 123456
    elif country:
        return 1234
    else:
        raise ValueError("Invalid input")
