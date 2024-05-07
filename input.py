while True:
    nname = input("Geben Sie Ihren Nachnamen ein!\n")
    if nname != "":
        print(f"Sie heißen {nname}!")
    else:
        break
    vname = input("Geben Sie Ihren Vornamen ein!\n")
    if vname != "":
        print(f"Sie heißen {vname} {nname}!")
    else:
        break