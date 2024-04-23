from Models.main import Model
from Models.Customer import Customer
from Views.main import View


class SignInController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def signin_handler(self,event):
        self.signin()
        
    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signin_btn.config(command=self.signin)
        self.frame.username_input.bind('<Return>', self.signin_handler)


    def signin(self) -> None:
        username = self.frame.username_input.get()
        data = {"username": username}
        print(data)
        user: Customer = {"username": data["username"]}
        self.model.auth.login(user)
        self.model.rentalAgency.initCustomers(username)