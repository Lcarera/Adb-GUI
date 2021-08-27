from helper import * 

os.chdir(cd)
cmd = ""
app = input("package: ")

while cmd != "exit":
    cmd = input("")
    if cmd == "enter":
        enter()
    elif cmd == "tab":
        tabear(1)
    elif cmd == "app":
        open_app(app)
    elif cmd == "uni":
        uninstall(app)
    elif cmd == "text":
        input_text(input("text: "))
    elif cmd == "login":
        input_text("dmusach@networkbroadcast.net")
        tabear(1)
        input_text("SuperNB2021!!!")
        enter()
    elif cmd == "connect":
        connect(input("0/255: "),input("puerto: "))
    elif cmd == "help":
        print("""
        Lista de comandos:
        connect: Conecta al box, y hace root y remount
        tab
        enter
        text: Manda txt al box
        uni: uninstall
        reboot
        install:
        exit
        """)
    elif cmd == "exit":
        break
    elif cmd == "reboot":
        reboot()
    elif cmd == "install":
        install()
    elif cmd == "pack":
        app = input()
    elif cmd == "disc":
        disconn()
    elif cmd == "otro":
        os.system(input("comando: "))