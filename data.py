class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"
    CREATE_COURIER = f"{BASE_URL}/courier"
    LOGIN_COURIER = f"{BASE_URL}/courier/login"
    DELETE_COURIER = f"{BASE_URL}/courier/"
    ORDERS = f"{BASE_URL}/orders"
    CANCEL_ORDER = f"{BASE_URL}/orders/cancel"


class OrderData:
    DEFAULT_ORDER = {
        "firstName": "Наруто",
        "lastName": "Узумаки",
        "address": "Коноха, 142",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2026-12-01",
        "comment": "Саске, вернись в Коноху"
    }

    COLOR_OPTIONS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]


class ResponseMessages:
    COURIER_CREATED = {"ok": True}
    COURIER_ALREADY_EXISTS = "Этот логин уже используется"
    COURIER_NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
    COURIER_NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"
    COURIER_NOT_FOUND = "Учетная запись не найдена"
