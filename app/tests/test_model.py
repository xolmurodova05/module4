from model import load_model, make_prediction

def test_model_output():
    model = load_model()
    prediction = make_prediction(model, "USA")
    assert prediction > 0
