from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()

def test_successful_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа с невалидным паролем возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_successful_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    """ Проверяем что запрос api ключа с невалидным email возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

def test_successful_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа с невалидными email и паролем возвращает статус 403 """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_add_new_pet_with_non_existent_photo(name='Джун', animal_type='Хомяк', age='3', pet_photo='images/nonexistent.jpg'):
    """Проверяем, что несуществующий файл вызывают исключение"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    try:
        # Добавляем питомца с неверным путем к файлу или несуществующим файлом
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    except FileNotFoundError:
        # Проверяем, что исключение FileNotFoundError было вызвано
        assert True
    else:
        # Если исключение не было вызвано, то тест не прошел
        assert False

def test_unsuccessful_create_pet_simple_with_invalid_name(name='', animal_type='Лошадь',
                                     age='3'):
    """Проверяем что создание питомца без фото с некорректным именем возвращает статус 400"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    # Ожидался статус 400, возвращается статус 200

def test_unsuccessful_create_pet_simple_with_invalid_animal_type(name='Робби', animal_type='1234567',
                                     age='3'):
    """Проверяем что создание питомца без фото с некорректным типом животного возвращает статус 400"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    # Ожидался статус 400, возвращается статус 200


def test_unsuccessful_add_new_pet_with_invalid_photo(name='ИнБос', animal_type='Коза',
                                     age='2', pet_photo='images/inlos.tyt'):
    """Проверяем что создание питомца с некорректным форматом фото возвращает статус 400"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    # Ожидался статус 400, возвращается статус 200

def test_unsuccessful_create_pet_simple_with_float_age(name='Фил', animal_type='Кот',
                                     age='0.05'):
    """Проверяем что создание питомца без фото с дробным возрастом животного возвращает статус 400"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    # Ожидался статус 400, возвращается статус 200

def test_unsuccessful_create_pet_simple_with_invalid_age(name='Фил', animal_type='Кот',
                                     age='123432432443545564754675675675546456546456324234233453453'):
    """Проверяем что создание питомца без фото с некорректным возрастом животного возвращает статус 400"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    # Ожидался статус 400, возвращается статус 200

def test_unsuccessful_create_pet_simple_with_invalid_all_data(name='', animal_type='',
                                     age=''):
    """Проверяем что создание питомца без фото со всеми некорректными значениями возвращает статус 400"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    # Ожидался статус 400, возвращается статус 200