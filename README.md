# latam_airlines

# El problema
El problema consiste en desplegar un modelo de machine learning.

# Desafío
Como ML Engineer, tu desafío consiste en tomar el trabajo de este Data Scientist y exponerlo para que sea explotado por un sistema:
1. Escoger el modelo que a tu criterio tenga un mejor performance, argumentando la decisión.
2. Implementar mejoras sobre el modelo escogiendo la o las técnicas que prefieras.
3. Exponer el modelo seleccionado como API REST para ser expuesto.
4. Hacer pruebas de estrés a la API con el modelo expuesto con al menos 50.000 requests durante 45 segundos. Para esto debes utilizar esta herramienta y presentar las métricas obtenidas.
5. ¿Cómo podrías mejorar el performance de las pruebas anteriores?

# Desarrollo del desafio
Con esta breve descripción buscamos dar una idea general de cómo abordaremos el problema de desplegar un modelo que ayude a predecir la probabilidad de atrasos de vuelos en el aeropuerto de Santiago de Chile (SCL):

1. Escoger el modelo que a tu criterio tenga un mejor performance, argumentando la decisión.
Seleccionaremos uno o varios algoritmos de aprendizaje automático del entrenamiento del modelo. Generaremos nuevas variables o combinaremos variables externas para mejorar la precisión del modelo. Realizaremos validación cruzada para evaluar la precisión del modelo y seleccionar los hiperparámetros adecuados.

2. Implementar mejoras sobre el modelo escogiendo la o las técnicas que prefieras.
Mediremos la precisión del modelo con métricas relevantes, como la exactitud, AUC-ROC, matriz de confusión, entre otras. Analizaremos qué variables tienen más impacto en la predicción. Identificaremos posibles áreas de mejora, como la inclusión de más variables o la modificación de la arquitectura del modelo.

3. Exponer el modelo seleccionado como API REST para ser expuesto.
Crearemos una api con Fastapi con la que se expondra el modelo para su consumo con los siguientes componentes:

- Un archivo principal, modelos y vistas para desplegar una API REST que devuelva el valor predicho por el modelo.
- Probaremos la API con pytest.
- Crearemos un contenedor para la API utilizando Docker.

4. Hacer pruebas de estrés a la API con el modelo expuesto con al menos 50.000 requests durante 45 segundos. Para esto debes utilizar esta herramienta y presentar las métricas obtenidas
Investigare esta herramienta para poder usarla

5. ¿Cómo podrías mejorar el performance de las pruebas anteriores?
archivo en md en el repositorio [4-5-Pruebas de estres](4-5-Pruebas_de_estres.md)

PD: Podemos utilizar Git para la creación de ramas y versionamiento. Si necesitas más información sobre cómo utilizar Git, puedes leer este artículo: [A modern branching strategy](https://martinfowler.com/articles/ship-show-ask.html)

## Mejoras

- Se puede desplegar esta api de forma serverless en aws usando S3 para almacenar el modelo pkl, lambda funtion para crear la api REST que retorne la prediccion y APIgateway para disponibilizar la api, de esta forma podemos escalar de forma automatizada en funcion de la demanda para la api. aca dejo un cloudformation que puede levantar la infraestructura y leer el repo

- Tambien podemos crear un un versionamiento de datos y modelos usando dvc que se almacenen aws(S3, Dynamo, ...) para la generacion del tracking de la informacion

- ademas podemos usar github action para la creacion del CI/CD o para el entrenamiento automatico del modelo cuando se detecte un nuevo PR.

## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for Data Scientist using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-fmh-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so latam_airlines can be imported.
    │
    └── latam_airlines               <- Source code for use in this project.
        ├── __init__.py    <- Makes latam_airlines a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

---
Project based on the [cookiecutter conda data science project template](https://github.com/frandak2/cookiecutter-personal).