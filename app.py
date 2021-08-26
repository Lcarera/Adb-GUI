from tkinter import *
from helper import *

root = Tk()

root.title("Adb GUI")


# e = Entry(root, width=35, borderwidth=5, )
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=50)

button_enter = Button(root, text="Enter", padx=40, pady=20,
                  command= enter).grid(row=0, column=3)

button_tab = Button(root, text="Tab", padx=40, pady=20,
                  command= tabear).grid(row=0, column=4)

button_open_app = Button(root, text="Open App", padx=40, pady=20,
                  command= open_app).grid(row=1, column=3)

button_input_text = Button(root, text="Input Text", padx=40, pady=20,
                  command= input_text).grid(row=1, column=4)

button_new_pack = Button(root, text="New Pack", padx=40, pady=20,
                  command= new_pack).grid(row=2, column=3)

button_uninstall_app = Button(root, text="Uninstall App", padx=40, pady=20,
                  command= uninstall).grid(row=2, column=4)

button_connect_stb = Button(root, text="Connect", padx=40, pady=20,
                  command= connect).grid(row=3, column=3)

button_reboot_stb = Button(root, text="Reboot", padx=40, pady=20,
                  command= reboot).grid(row=3, column=4)

button_install_apk = Button(root, text="Install", padx=40, pady=20,
                  command= install).grid(row=4, column=3)

button_disconnect_all = Button(root, text="Disconnect", padx=91, pady=20,
                  command= disconn).grid(row=4, column=4)

button_packages_list = Button(root, text="Show Packs List", padx=39, pady=20,
                    command= disconn).grid(row=5, column=3)


root.mainloop()