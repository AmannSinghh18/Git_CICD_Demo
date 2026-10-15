def predict_label(value):
    """A tiny example function for CI testing."""
    return "positive" if value >= 0.5 else "negative"


def prediction_message(value):
    """Return a clear message describing the prediction."""
    return f"Prediction result: {predict_label(value)}"


if __name__ == "__main__":
    print(prediction_message(0.8))
