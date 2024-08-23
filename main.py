import tkinter
from tkinter import ttk

import sv_ttk
import pywinstyles
import darkdetect


class Main(tkinter.Tk):
    def __init__(self, w: int = 300, h: int = 100) -> None:
        super().__init__()

        # Set the window attributes
        self.title('Modern Tkinter Template')

        self.geometry(f'{w}x{h}')
        self.minsize(w, h)

        self.resizable(True, True)

        # Style the window
        self.center_window()
        sv_ttk.set_theme(darkdetect.theme())
        self.apply_theme_to_titlebar()

        # Add the widgets
        self.create_widgets()

    def hello_world(self) -> None:
        print(f'Hello, World!')

    # WIDGET FUNCTIONS #
    def create_widgets(self) -> None:
        button = ttk.Button(self, text='Button', command=self.hello_world)
        button.pack(padx=10, pady=10)

    # THEMING FUNCTIONS #
    def center_window(self) -> None:
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()

    def apply_theme_to_titlebar(self) -> None:
        import sys
        version = sys.getwindowsversion()

        if version.major == 10 and version.build >= 22000:
            # Set the title bar color to the background color on Windows 11 for better appearance
            pywinstyles.change_header_color(self, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
        elif version.major == 10:
            pywinstyles.apply_style(self, "dark" if sv_ttk.get_theme() == "dark" else "normal")

            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            self.wm_attributes("-alpha", 0.99)
            self.wm_attributes("-alpha", 1)


def start() -> None:
    app = Main()
    app.mainloop()


if __name__ == '__main__':
    start()