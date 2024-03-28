import tkinter as tk
from tkinter import ttk

class CollapsiblePane(ttk.Frame):
    """
    -----USAGE-----
    collapsiblePane = CollapsiblePane(parent,
                          expanded_text =[string],
                          collapsed_text =[string])

    collapsiblePane.pack()
    button = Button(collapsiblePane.frame).pack()
    """

    def __init__(self, parent, expanded_text="Collapse <<",
                 collapsed_text="Expand >>"):

        ttk.Frame.__init__(self, parent)
        self.parent = parent
        # parent.configure(background="light grey")  # Set parent container background color
        self._expanded_text = expanded_text
        self._collapsed_text = collapsed_text

        self.columnconfigure(1, weight=1)

        self._variable = tk.IntVar()

        self._button = ttk.Checkbutton(self, variable=self._variable,
                                        command=self._activate, style="Toolbutton")
        self._button.grid(row=0, column=0)

        self._separator = ttk.Separator(self, orient="horizontal")
        self._separator.grid(row=0, column=1, sticky="we")

        self.frame = LeftAlignedFrame(self)
        self.frame.configure(background="light grey", padx=10, pady = 10)  # Set frame background color
        self._activate()

    def _activate(self):
        if not self._variable.get():
            self.frame.grid_forget()
            self._button.configure(text=self._collapsed_text)

        elif self._variable.get():
            self.frame.grid(row=1, column=0, columnspan=2)
            self._button.configure(text=self._expanded_text)

    def toggle(self):
        self._variable.set(not self._variable.get())
        self._activate()


class LeftAlignedFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

    def grid(self, **kwargs):
        kwargs.setdefault('sticky', 'w')
        tk.Frame.grid(self, **kwargs)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    collapsiblePane = CollapsiblePane(root)
    collapsiblePane.pack(fill="both", expand=True)
    button = tk.Button(collapsiblePane.frame, text="Button")
    button.pack()
    root.mainloop()