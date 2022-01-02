from wardrobe.service_layers import unit_of_work


def get_user(user_id, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        user = uow.users.get(user_id)

    return user
