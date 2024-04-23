from typing import TypedDict

from .root import Root
from .RentalView import RentalView
from .SignInView import SignInView


class Frames(TypedDict):
    signin: SignInView
    home: RentalView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(SignInView, "signin")
        self._add_frame(RentalView, "home")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
