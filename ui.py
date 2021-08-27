from tkinter import *
from data1 import Data
Data()
BACKGROUND = "#DDF3F5"
TITLE_FONT = "Book Antigua"
BUTTON_COLOR = "#FF7171"


class UserInterface:

    def __init__(self, data1):

        self.root = Tk()
        self.root.title("Weather App")
        self.root.config(height=400, width=800, padx=20, pady=20, bg=BACKGROUND)
        self.root.minsize(height=400, width=800)
        self.title = Label(text="Current Weather Search",
                           font=(TITLE_FONT, 17), bg=BACKGROUND, pady=25
                           )
        self.zip_entry = Entry(width=40, highlightthickness=0, fg="gray")
        self.zip_entry.insert(0, "Enter a US Zip-Code")
        self.zip_entry.focus()
        self.zip_entry.icursor(0)
        self.zip_entry.bind("<Key>", self.clear_widget)
        self.submit = Button(text="submit",
            font=("Times", 10, "bold"), fg="black", bg=BUTTON_COLOR, command=self.button_press
        )
        self.result_label = Label(text="", bg=BACKGROUND, fg="black", pady=25,
            font=("Terminal", 17, "bold")
        )
        self.title.pack()
        self.zip_entry.pack(ipady=4)
        self.submit.pack()
        self.result_label.pack()
        self.root.mainloop()

    def clear_widget(self, event):
        self.widget_text = self.zip_entry.get()
        if self.widget_text == "Enter a US Zip-Code":
            self.zip_entry.delete(0, END)
            self.zip_entry.config(fg="black")
    def button_press(self):
        self.widget_text = self.zip_entry.get()
        self.result_label.config(text=self.widget_text)
        z = Data()
        t = z.fetch_temp(zc=self.widget_text)
        c = z.fetch_name(zc=self.widget_text)
        d = z.fetch_condition(zc=self.widget_text)
        s= z.fetch_state(zc=self.widget_text)
        self.result_label.config(text=f"The current temp is {t} C° in {c},{s}\n "
                                      f"The current condition is {d}")



