from typing import TypedDict, Union
from .base import ObservableModel
from Models.Customer import Customer

class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.current_user = None

    def login(self, user: Customer) -> None:
        self.is_logged_in = True
        self.current_user = user
        self.trigger_event("auth_changed")

