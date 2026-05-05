from electron import Electron
import physics

def shell_loop(rocket_c: str):
    print("Welcome to the main shell!")
    if rocket_c == "Electron":
        rocket = Electron(name = rocket_c)

    while True:
        action = input()

        if action == "info":
            rocket.get_info()

        elif action == "change name":            
            rocket.change_name()

        elif action == "q":
            print("Bye!")
            break

        elif action == "start engine 1":
            physics.r_time()

        else:
            print("error") 
            