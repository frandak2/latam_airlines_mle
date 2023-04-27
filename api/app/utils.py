from joblib import load
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame

def get_model() -> Pipeline:
    model = load('models/model_balanced_over.pkl')
    return model

def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key:[value] for key, value in class_model.dict().items()}
    data_frame = DataFrame(transition_dictionary)
    return data_frame