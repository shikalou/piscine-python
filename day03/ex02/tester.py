from DiamondTrap import King


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.eyes = "blue"
    Joffrey.hairs = "light"
    print(Joffrey.eyes)
    print(Joffrey.hairs)
    print(Joffrey.__dict__)

# from DiamondTrap import King


# def main():
#     Joffrey = King("Joffrey")
#     print(Joffrey.__dict__)
#     Joffrey.set_eyes("blue")
#     Joffrey.set_hairs("light")
#     print(Joffrey.get_eyes())
#     print(Joffrey.get_hairs())
#     print(Joffrey.__dict__)

if __name__ == "__main__":
    main()
