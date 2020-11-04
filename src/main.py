import os
import keyboard
import pyperclip
from tkinter import (
    Tk,
    Frame,
    Button,
    Label,
    Text,
    LEFT,
    RIGHT,
    PhotoImage
)


class App:
    def __init__(self, main):
        self.slots = 1
        self.text_areas = {}
        self.contents = {}
        dirname = os.path.dirname(__file__)
        icon_path = os.path.join(dirname, "icon", "clipboard.png")
        main.title("Multi Paste")
        root.iconphoto(False, PhotoImage(file=icon_path))
        main.resizable(0,0)
        self.main_frame = Frame(main).pack()
        button_add_slot = Button(
            self.main_frame,
            text="Add slot",
            command=self.add_slot,
            width=10,
            height=10
        ).pack(side=LEFT)
        button_exit = Button(
            self.main_frame,
            text="Exit",
            command=root.quit,
            width=10,
            height=10
        ).pack(side=RIGHT)

    def add_slot(self):
        frame_slot = Frame(self.main_frame)
        key_label = Label(
            frame_slot,
            text=f"Ctrl + {self.slots}",
            width=10
        ).pack()
        text_area = Text(
            frame_slot,
            name=f"slot-{self.slots}",
            height=8,
            width=30
        )
        text_area.bind(
            "<FocusOut>",
            lambda x: self.callback_text_area(str(text_area))
        )
        text_area.pack()
        frame_slot.pack(side=LEFT)
        self.text_areas[str(text_area)] = text_area
        self.contents[str(text_area)] = ""
        keyboard.add_hotkey(
            f'ctrl+{self.slots}',
            lambda: self.keyboard_callback(str(text_area))
        )
        self.slots += 1

    def callback_text_area(self, slot):
        content = self.text_areas[slot].get('1.0', 'end')
        pyperclip.copy(content)
        self.contents[slot] = content

    def keyboard_callback(self, slot):
        content = self.contents[slot]
        keyboard.write(content)


if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()
