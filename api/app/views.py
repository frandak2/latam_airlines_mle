from .models import PredictionRequest
from .utils import get_model, transform_to_dataframe

model = get_model()

def get_prediction(request: PredictionRequest) -> float:
    # if all(val == 0 for val in request.values()):
    #     prediction = 'error'
    # else:
    #     data_to_predict = transform_to_dataframe(request)
    #     prediction = model.predict(data_to_predict)[0]
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return prediction