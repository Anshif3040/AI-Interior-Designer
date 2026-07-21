import numpy as np

def predict_room(model, img_array, classes):

    pred = model.predict(img_array)

    prediction = classes[np.argmax(pred)]

    confidence = float(np.max(pred) * 100)

    top_indices = np.argsort(pred[0])[-3:][::-1]

    top_predictions = []

    for idx in top_indices:

        top_predictions.append(
            (
                classes[idx],
                round(float(pred[0][idx] * 100), 2)
            )
        )

    return prediction, confidence, top_predictions