from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    DIA: int = Field(default=1, ge=1, le=31)
    MES: int = Field(default=1, ge=1, le=12)
    HORA: int = Field(default=0, ge=0, le=23)
    MIN: int = Field(default=15, ge=0, le=59)
    temporada_alta: int = Field(default=1, ge=0, le=1)
    periodo_dia: str = Field(min_length=5, max_length=6)
    DIANOM: str = Field(min_length=5, max_length=9)
    Des_I: str = Field(min_length=3, max_length=5)
    TIPOVUELO: str = Field(min_length=1)
    OPERA: str = Field(min_length=3, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "DIA": 1,
                "MES": 1,
                "HORA": 0,
                "MIN": 15,
                "temporada_alta": 1,
                "periodo_dia": "noche",
                "DIANOM": "Domingo",
                "Des_I": "MMMX",
                "TIPOVUELO": "I",
                "OPERA": "Aeromexico"
            }
        }

class PredictionResponse(BaseModel):
    atraso_15: int