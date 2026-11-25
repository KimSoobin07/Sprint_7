import pytest
from helpers import (
    generate_courier_payload,
    register_new_courier_and_return_login_password,
    delete_courier_by_credentials,
    cancel_order_by_track
)


@pytest.fixture
def courier_payload():
    """Генерирует данные для нового курьера и удаляет его после теста, если он был создан."""
    payload = generate_courier_payload()
    yield payload
    delete_courier_by_credentials(payload["login"], payload["password"])


@pytest.fixture
def created_courier():
    """Создаёт нового курьера перед тестом и удаляет его после завершения теста."""
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data
    if courier_data:
        delete_courier_by_credentials(courier_data[0], courier_data[1])


@pytest.fixture
def order_track_cleaner():
    """Сохраняет track созданного заказа и отменяет заказ после теста."""
    tracks = []
    yield tracks
    for track in tracks:
        cancel_order_by_track(track)
