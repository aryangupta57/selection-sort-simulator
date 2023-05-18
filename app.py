from tkinter import *
from random import *


# window
def window():
    global main_window
    main_window = Tk()
    main_window.title("simulator_beta")
    main_window.configure(background="white")
    main_window.geometry("1280x720")

    def simulate():
        number_of_elements = int(i1.get())
        choice = int(i2.get())

        def sort(l):
            for i in range(len(l)):
                min = i
                passb = Label(
                    main_window,
                    text="Pass {}".format(i + 1),
                    fg="white",
                    bg="#007AFF",
                    width=7,
                    height=1,
                    font=20,
                )
                passb.place(x=8, y=190 + (60 * (i + 1)))
                for k in range(0, i):
                    bw = Label(
                        main_window,
                        text=l[k],
                        fg="white",
                        bg="snow4",
                        width=7,
                        height=1,
                        font=20,
                    )
                    bw.place(x=100 + (70 * (k)), y=190 + (60 * (i + 1)))
                for j in range(i + 1, len(l)):
                    if l[min] > l[j]:
                        min = j
                    bw1 = Label(
                        main_window,
                        text=l[j - 1],
                        fg="white",
                        bg="snow3",
                        width=7,
                        height=1,
                        font=20,
                    )
                    bw1.place(x=50 + (70 * (j)), y=190 + (60 * (i + 1)))
                bw2 = Label(
                    main_window,
                    text=l[j],
                    fg="white",
                    bg="snow3",
                    width=7,
                    height=1,
                    font=20,
                )
                bw2.place(x=120 + (70 * (j)), y=190 + (60 * (i + 1)))
                l[i], l[min] = l[min], l[i]
                if (l[i]) != (l[min]):
                    passb1 = Label(
                        main_window,
                        text="SWAP of element {} and {}".format(l[i], l[min]),
                        fg="white",
                        bg="lime",
                        font=20,
                    )
                    passb1.place(x=8, y=215 + (60 * (i + 1)))
                else:
                    passb1 = Label(
                        main_window,
                        text="NO SWAP".format(l[i], l[min]),
                        fg="white",
                        bg="red",
                        font=20,
                    )
                    passb1.place(x=8, y=215 + (60 * (i + 1)))
            return l

        l = []
        random_number = int(random() * 10000)
        # Ascending
        if choice == 1:
            for x in range(number_of_elements):
                l.append(random_number)
                random_number += 1
        # Descending
        elif choice == 2:
            for x in range(number_of_elements):
                l.append(random_number)
                random_number -= 1
        # Random
        elif choice == 3:
            for x in range(number_of_elements):
                element = int(random() * 1000)
                l.append(element)
        else:
            print("Invalid Choice")
        sort(l)

    Button(
        text="RUN",
        relief=RAISED,
        cursor="hand2",
        fg="black",
        bg="white",
        activebackground="blue",
        activeforeground="white",
        command=simulate,
        height=1,
        width=7,
    ).place(x=850 + 190, y=30)
    Button(
        text="RESET",
        relief=RAISED,
        cursor="hand2",
        fg="black",
        bg="white",
        activebackground="blue",
        activeforeground="white",
        command=reset,
        height=1,
        width=7,
    ).place(x=790 + 180, y=30)
    Label(text="SELECTION SORT", fg="white", bg="black", width=200, height=1).place(
        x=0, y=0
    )
    Label(text="No of Element", fg="grey50").place(x=0, y=30)
    Label(text="Type of Array", fg="grey50").place(x=0, y=60)
    i1 = StringVar()
    i2 = StringVar()
    # entries
    # dropdown
    menu_button = Menubutton(main_window, text="Select")
    menu_button.menu = Menu(menu_button)
    menu_button["menu"] = menu_button.menu

    menu_button.menu.add_radiobutton(
        label="Sorted", variable=i2, value="1", command=lambda: print(i2.get())
    )
    menu_button.menu.add_radiobutton(
        label="Reversely Sorted",
        variable=i2,
        value="2",
        command=lambda: print(i2.get()),
    )
    menu_button.menu.add_radiobutton(
        label="Random ", variable=i2, value="3", command=lambda: print(i2.get())
    )
    Entry(textvariable=i1).place(x=110, y=30)
    menu_button.place(x=110, y=60)
    main_window.mainloop()


# refresh
if __name__ == "__main__":

    def reset():
        main_window.destroy()
        window()

    window()
