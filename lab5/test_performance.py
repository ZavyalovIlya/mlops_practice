import pytest
import pickle
import numpy as np
from os import listdir
from sklearn.metrics import root_mean_squared_error as rmse


@pytest.fixture(scope='session')
def load_model():
    """
    фикстура для импорта модели. выполняется один раз за сеанс
    :return: модель
    """
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


@pytest.fixture(scope='function')
def prediction(request, load_model):
    """
    фикстура для чтения файла и предсказания таргетов по фичам
    :param request: переменная от тестирующей функции (путь к файлу с данными)
    :param load_model: обращение к фикстуре загрузки модели
    :return: словарь. predicted - значения предсказаний модели, actual - истинные значения
    """
    model = load_model

    data = np.loadtxt(request.param, delimiter=',')
    x = data[:, 0].reshape(-1, 1)
    y = data[:, 1].reshape(-1, 1)

    y_hat = model.predict(x)

    return {'predicted': y_hat,
            'actual': y}


@pytest.mark.parametrize(
    "prediction",
    ['datasets/' + file for file in listdir('datasets')],
    indirect=True)
def test_performance(prediction):
    """
    функция тестирования результатов предсказания модели.
    успешное прохождение теста при RMSE меньше 1.
    параметризирована по файлам в директории datasets
    :param prediction: обращение к фикстуре prediction
    """
    assert rmse(prediction['predicted'], prediction['actual']) < 1
