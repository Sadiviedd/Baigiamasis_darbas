from tkinter import *
from projektai_con import *
import datetime


class App:
    def __init__(self, master):
        # SET LEFT AND RIGHT FRAMES
        self.left_frame = Frame(master)
        self.right_frame = Frame(master)
        self.left_frame.pack(side="left", fill="both", expand=True)
        self.right_frame.config(highlightbackground="black", highlightthickness=1.2)
        # SET IMAGES
        self.img_start = PhotoImage(file=r"C:\Users\LENOVO\PycharmProjects\Baigiamasis_\button_pradeti.png")
        self.img_pause = PhotoImage(file=r"C:\Users\LENOVO\PycharmProjects\Baigiamasis_\button_sustabdyti.png")
        self.img_end = PhotoImage(file=r"C:\Users\LENOVO\PycharmProjects\Baigiamasis_\button_baigti.png")
        self.img_submit = PhotoImage(file=r"C:\Users\LENOVO\PycharmProjects\Baigiamasis_\button_patvirtinti.png")
        # SET TIMER
        self.timer_time = ''
        self.running = False
        self.datetime = ""
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # ----------------LEFT FRAME----------------

        # TIMER INFO (INIT AND VIS)
        self.timer_label = Label(self.left_frame, text="00:00:00", font=("Segoe UI", 40, "bold"))
        self.timer_label.pack()
        # OPERATION LABEL (INIT AND VIS)
        self.operation_label = Label(self.left_frame,
                                     text="PASPAUSKITE 'PRADĖTI' NORĖDAMI PRADĖTI DARBĄ",
                                     font=("Segoe UI", 14, "bold"))
        self.operation_label.place(relx=0.5, rely=0.37, anchor=CENTER)
        # START, STOP, END BUTTONS (INIT AND VIS)
        self.start_button = Button(self.left_frame,
                                   text="PRADĖTI",
                                   bd=0,
                                   image=self.img_start,
                                   command=self.start_timer)
        self.pause_button = Button(self.left_frame,
                                   text="SUSTABDYTI",
                                   state=DISABLED,
                                   bd=0,
                                   image=self.img_pause,
                                   command=self.pause_timer)
        self.end_button = Button(self.left_frame,
                                 text="BAIGTI",
                                 state=DISABLED,
                                 bd=0,
                                 image=self.img_end,
                                 command=lambda: self.show_frame(1))
        self.start_button.place(relx=0.2, rely=0.6, anchor=CENTER)
        self.pause_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.end_button.place(relx=0.8, rely=0.6, anchor=CENTER)

        # ----------------RIGHT FRAME----------------

        # INFORMATION LABEL (INIT AND VIS)
        self.information_label = Label(self.right_frame, text="SUVESKITE DUOMENIS", font=("Segoe UI", 14, "bold"))
        self.information_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        # PROJECT NAME: LABEL, ENTRY (INIT AND VIS)
        self.project_label = Label(self.right_frame, text="Projektas", font=("Segoe UI", 11, "bold"))
        self.project_entry = Entry(self.right_frame)
        self.project_label.place(relx=0.05, rely=0.2)
        self.project_entry.place(relx=0.42, rely=0.21)
        # PROJECT ISSUE: LABEL, ENTRY (INIT AND VIS)
        self.issue_label = Label(self.right_frame, text="Užduotis", font=("Segoe UI", 11, "bold"))
        self.issue_entry = Entry(self.right_frame)
        self.issue_label.place(relx=0.05, rely=0.33)
        self.issue_entry.place(relx=0.42, rely=0.34)
        # WORKER NAME: LABEL, ENTRY (INIT AND VIS)
        self.worker_label = Label(self.right_frame, text="Darbuotojas", font=("Segoe UI", 11, "bold"))
        self.worker_entry = Entry(self.right_frame)
        self.worker_label.place(relx=0.05, rely=0.46)
        self.worker_entry.place(relx=0.42, rely=0.47)
        # SUBMIT BUTTON (INIT AND VIS)
        self.submit_button = Button(self.right_frame, text="Patvirtinti", command=self.submit_record)
        self.submit_button.place(relx=0.1, rely=0.65)
        # NEW ISSUE BUTTON (INIT AND VIS)
        self.new_issue_button = Button(self.right_frame, text="Nauja užduotis", command=lambda: self.show_frame(2))
        self.new_issue_button.place(relx=0.37, rely=0.65)
        # END PROGRAM BUTTON (INIT AND VIS)
        self.end_program_button = Button(self.right_frame, text="Išeiti", command=master.destroy)
        self.end_program_button.place(relx=0.1, rely=0.80)
        # ALL RECORDS LIST
        self.records_list = Listbox(self.left_frame,
                                    selectmode=SINGLE,
                                    bg="#f0f0f0",
                                    highlightthickness=0.5,
                                    highlightbackground="black")
        self.records_list.insert(END, *all_records())
        self.records_list.place_forget()
        # DELETE RECORDS (INIT AND VIS)
        self.delete_button = Button(self.right_frame, text="Ištrinti", command=self.delete_record)
        self.delete_button.place(relx=0.75, rely=0.65)

    def show_frame(self, num):
         if num == 1:
            self.right_frame.pack(side="right", fill="both", expand=True)
            self.left_frame.config(highlightbackground="black", highlightthickness=1.2)
            self.start_button.place_forget()
            self.pause_button.place_forget()
            self.end_button.place_forget()
            self.timer_label.pack_forget()
            self.operation_label.config(text=f"DARBAS BAIGTAS. PRADIRBTA LAIKO: {self.timer_label['text']}")
            self.operation_label.place(relx=0.5, rely=0.1)
            self.start_button.config(text="PRADĖTI")
            self.timer_label.after_cancel(self.timer_time)
            self.running = False
            self.end_button.config(text="DARBAS BAIGTAS")
            self.start_end_dates(2)
            self.records_list.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.75)
            self.submit_button.config(state=NORMAL)
         if num == 2:
            self.right_frame.pack_forget()
            self.left_frame.config(highlightbackground="black", highlightthickness=0)
            self.start_button.place(relx=0.2, rely=0.6, anchor=CENTER)
            self.pause_button.place(relx=0.5, rely=0.6, anchor=CENTER)
            self.end_button.place(relx=0.8, rely=0.6, anchor=CENTER)
            self.start_button.config(state=NORMAL)
            self.pause_button.config(state=DISABLED)
            self.end_button.config(state=DISABLED)
            self.operation_label.config(text="PASPAUSKITE 'PRADĖTI' NORĖDAMI PRADĖTI DARBĄ")
            self.operation_label.place(relx=0.5, rely=0.37, anchor=CENTER)
            self.timer_label.config(text="00:00:00")
            self.timer_label.pack()
            self.hours, self.minutes, self.seconds = 0, 0, 0
            self.records_list.place_forget()

    def start_end_dates(self, num):
        datetime_now = datetime.datetime.now().replace(microsecond=0)
        if num == 1:
            if self.operation_label["text"] == "DARBAS PRADĖTAS":
                self.datetime = datetime_now
            return self.datetime
        if num == 2:
            if self.operation_label["text"] == f"DARBAS BAIGTAS. PRADIRBTA LAIKO: {self.timer_label['text']}":
                self.datetime = datetime_now
            return self.datetime

    def submit_record(self):
        time_worked = self.timer_label["text"]
        add_record(self.project_entry.get(),
                   self.issue_entry.get(),
                   self.worker_entry.get(),
                   self.start_end_dates(1),
                   time_worked,
                   self.start_end_dates(2))
        self.project_entry.delete(0, END)
        self.issue_entry.delete(0, END)
        self.worker_entry.delete(0, END)
        self.records_list.delete(0, END)
        self.records_list.insert(0, *all_records())
        self.submit_button.config(state=DISABLED)

    def delete_record(self):
        index = all_records()[self.records_list.curselection()[0]]
        delete_record(index.id)
        self.records_list.delete(0, END)
        self.records_list.insert(0, *all_records())

    def start_timer(self):
        if not self.running:
            self.timer_label.after(1000)
            self.timer()
            self.running = True
        if self.start_button["text"] == "PRADĖTI":
            self.operation_label.config(text="DARBAS PRADĖTAS")
            self.pause_button.config(state=NORMAL)
            self.start_button.config(state=DISABLED)
            self.end_button.config(state=NORMAL)
        if self.start_button["text"] == "PRATĘSTI":
            self.operation_label.config(text="DARBAS TOLIAU TĘSIAMAS")
            self.start_button.config(state=DISABLED)
            self.pause_button.config(state=NORMAL)
        self.start_end_dates(1)

    def pause_timer(self):
        if self.running:
            self.timer_label.after_cancel(self.timer_time)
            self.running = False
        self.operation_label.config(text="DARBAS SUSTABDYTAS")
        self.start_button.config(text="PRATĘSTI", state=NORMAL)
        self.pause_button.config(state=DISABLED)

    def timer(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        hours_string = f'{self.hours}' if self.hours > 9 else f'0{self.hours}'
        minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
        seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        self.timer_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        self.timer_time = self.timer_label.after(1000, self.timer)


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.minsize(740, 250)
    root.title("Projekto registravimo forma")
    root.iconbitmap(r'C:\Users\LENOVO\PycharmProjects\Baigiamasis_\icon.ico')
    root.mainloop()