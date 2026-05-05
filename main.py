from electron import Electron
from shell import shell_loop

print("#############  Digital simulator of the famous Spaceships and Rockets  #############")
print("#############  Author: Zholdasbek Zhussip  #########################################")
print("#############  Choose your rocket  #################################################")
print("#############  1) Falcon 9  ########################################################")
print("#############  2) ZhuQue-2E ########################################################")
print("#############  3) Electron  ########################################################")



try: 
    choose = input("my rocket: ")
    rocket = ""
except:
    print("bye")

    quit()
if choose == "1" or choose[0] == "F" or choose[0] == "f":
    rocket = "Falcon 9"
    print(f"{rocket} is not available yet...")
elif choose == "2" or choose[0] == "Z" or choose == "z":
    rocket == "ZhuQue-2E"
    print(f"{rocket} is not available yet...")
elif choose == "3" or choose[0] == "E" or choose == "e":
    rocket == "Electron"
    shell_loop(rocket_c="Electron")


else:
    print("############# ERROR! #############")




    


