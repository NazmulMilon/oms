from enum import Enum


class BaseEnum(Enum):
    """
     Let's allow using an Enum class in model Field choices and make code more simple and modular.
     Ref: https://code.djangoproject.com/ticket/27910
     Ref: https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model
    """

    def __init__(self, *args):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name

            raise ValueError("aliases not allowed in DuplicateFreeEnum:  %r --> %r" % (a, e))

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class DiscountType(BaseEnum):
    AMOUNT = 1
    PERCENTAGE = 2


class AddressType(BaseEnum):
    SHIPPING_ADDRESS = "shipping"
    BILLING_ADDRESS = "billing"
    # SHIPPING_ADDRESS = 1
    # BILLING_ADDRESS = 2


class TaskStatusType(BaseEnum):
    ASSIGNED = "assigned"
    NOT_ASSIGN = "not_assigned"
    COMPLETED = "completed"
    RUNNING = "running"
    PAUSE = "pause"

