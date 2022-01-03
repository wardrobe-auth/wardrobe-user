from flask import current_app
from werkzeug.local import LocalProxy

from wardrobe import bootstrap
from wardrobe.adaptors.repository.mem import MemUserRepository
from wardrobe.service_layers.unit_of_work import MemUnitOfWork

_bus = None


def get_message_bus():
    global _bus

    if _bus is None:
        users = MemUserRepository(
            [
                dict(
                    id=1,
                    email="john@example.com",
                    name="John",
                    password="secret",
                ),
                dict(
                    id=2,
                    email="jane@example.com",
                    name="Jane",
                    password="secret",
                ),
            ]
        )
        uow = MemUnitOfWork(users=users)
        _bus = bootstrap.bootstrap(uow=uow, logger=current_app.logger)

    return _bus


bus = LocalProxy(get_message_bus)
