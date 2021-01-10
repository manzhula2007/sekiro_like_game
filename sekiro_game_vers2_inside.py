import random
import sys


class Sekiro:
    def __init__(self, name, atac, block, blockgr, dob, life, conset):
        self.name = name
        self.atac = atac
        self.block = block
        self.blockgr = blockgr
        self.dob = dob
        self.life = life
        self.conset = conset


class Training(Sekiro):

    def training(self):
        print(f"Ну чтош {self.name}! Сегодня я научу тебя боевому искуству!")
        count = 0
        while True:
            if count == 0:
                if input(f"Нажми {self.atac} чтобы атаковать: ") == self.atac:
                    print("Отклично, теперь ты научисля бить!")
                    count += 1
                else:
                    continue
            elif count == 1:
                if input(f"Нажми {self.block} чтобы отразить атаку: ") == self.block:
                    print("Отлично, теперь ты научился отражать атаку!")
                    count += 1
                else:
                    continue
            elif count == 2:
                if input(f"Нажми {self.dob} чтобы добить, ведь это окончательно убъет твоего противника: ") == self.dob:
                    print("Отлично, теперь ты научился добивать")
                    print("Надеюсь, эти навыки помогут тебе в бою!")
                    print(
                        "Кстати, совсем забыл, чтобы победить, тебе нужно заполнить концитрацию врага")
                    print(
                        "И еще, когда ты убиваешь противника, ты забираешь его жызненную силу")
                    break
                else:
                    continue


class Just_Fight(Sekiro):

    def fight(self):
        print(f"Твое здоровъе: {self.life}")
        cons = 0
        print(f"Концитрация врага: {cons}")
        a_bl = ["atac", "block"]
        while True:
            random.shuffle(a_bl)
            if cons >= 5:
                print("Концитрация врага на приделе! Добей его!!")
                if input(": ") == self.dob:
                    print("Ты убил его")
                    break
                else:
                    print("Ало добивать надо!!!!")
                    print(f"Твое здоровъе: {self.life}")
                    cons = 3
                    print(f"Концитрация врага: {cons}")

            elif self.life == 0:
                print("Ты погиб!")
                sys.exit()

            elif a_bl[0] == "atac":
                print(f"Противник атакует")
                if input(": ") == self.block:
                    cons += self.conset
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")
                else:
                    self.life -= 1
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")

            elif a_bl[0] == "block":
                print(f"Противник стоит")
                if input(": ") == self.atac:
                    print(f"Твое здоровъе: {self.life}")
                    cons += self.conset
                    print(f"Концитрация врага: {cons}")
                else:
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")


class Just_Fight1(Sekiro):

    def fight(self):
        print(f"Твое здоровъе: {self.life}")
        cons = 0
        print(f"Концитрация врага: {cons}")
        a_bl = ["atac", "block"]
        while True:
            random.shuffle(a_bl)
            if cons >= 7:
                print("Концитрация врага на приделе! Добей его!!")
                if input(": ") == self.dob:
                    print("Ты убил его")
                    break
                else:
                    print("Ало добивать надо!!!!")
                    print(f"Твое здоровъе: {self.life}")
                    cons = 3
                    print(f"Концитрация врага: {cons}")

            elif self.life == 0:
                print("Ты погиб!")
                sys.exit()

            elif a_bl[0] == "atac":
                print(f"Противник атакует")
                if input(": ") == self.block:
                    cons += self.conset
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")
                else:
                    self.life -= 1
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")

            elif a_bl[0] == "block":
                print(f"Противник стоит")
                if input(": ") == self.atac:
                    print(f"Твое здоровъе: {self.life}")
                    cons += self.conset
                    print(f"Концитрация врага: {cons}")
                else:
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")


class Just_Fight2(Sekiro):

    def fight(self):
        print(f"Твое здоровъе: {self.life}")
        cons = 0
        print(f"Концитрация врага: {cons}")
        a_bl = ["atac", "block"]
        while True:
            random.shuffle(a_bl)
            if cons >= 10:
                print("Концитрация врага на приделе! Добей его!!")
                if input(": ") == self.dob:
                    print("Ты убил его")
                    break
                else:
                    print("Ало добивать надо!!!!")
                    print(f"Твое здоровъе: {self.life}")
                    cons = 3
                    print(f"Концитрация врага: {cons}")

            elif self.life == 0:
                print("Ты погиб!")
                sys.exit()

            elif a_bl[0] == "atac":
                print(f"Противник атакует")
                if input(": ") == self.block:
                    cons += self.conset
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")
                else:
                    self.life -= 1
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")

            elif a_bl[0] == "block":
                print(f"Противник стоит")
                if input(": ") == self.atac:
                    print(f"Твое здоровъе: {self.life}")
                    cons += self.conset
                    print(f"Концитрация врага: {cons}")
                else:
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")

class Secret_Fight(Sekiro):
    def fight(self):
        print(f"Твое здоровъе: {self.life}")
        cons = 0
        print(f"Концитрация врага: {cons}")
        a_bl = ["atac", "block"]
        while True:
            random.shuffle(a_bl)
            if cons >= 15:
                print("Концитрация врага на приделе! Добей его!!")
                if input(": ") == self.dob:
                    print("Молодец, ты убил его")
                    print("Победа!")
                    break
                else:
                    print("Ало добивать надо!!!!")
                    print(f"Твое здоровъе: {self.life}")
                    cons = 13
                    print(f"Концитрация врага: {cons}")

            elif self.life == 0:
                print("Ты погиб!")
                sys.exit()
            elif a_bl[0] == "atac":
                print(f"Противник атакует")
                if input(": ") == self.block:
                    cons += self.conset
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")
                else:
                    self.life -= 1
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")

            elif a_bl[0] == "block":
                print(f"Противник стоит")
                if input(": ") == self.atac:
                    print(f"Твое здоровъе: {self.life}")
                    cons += self.conset
                    print(f"Концитрация врага: {cons}")
                else:
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")


class Boss_fight(Sekiro):
    def fight(self):
        print(f"Твое здоровъе: {self.life}")
        cons = 0
        print(f"Концитрация врага: {cons}")
        print("Удачи")
        a_bl = ["atac", "block", "grom"]
        while True:
            random.shuffle(a_bl)
            if cons >= 20:
                print("Концитрация врага на приделе! Добей его!!")
                if input(": ") == self.dob:
                    print("Молодец, ты убил его")
                    print("Победа!")
                    break
                else:
                    print("Ало добивать надо!!!!")
                    print(f"Твое здоровъе: {self.life}")
                    cons -= 2
                    print(f"Концитрация врага: {cons}")

            elif self.life == 0:
                print("Ты погиб!")
                sys.exit()
            elif a_bl[0] == "atac":
                print(f"Противник атакует")
                if input(": ") == self.block:
                    cons += self.conset
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")
                else:
                    self.life -= 1
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")

            elif a_bl[0] == "block":
                print(f"Противник стоит")
                if input(": ") == self.atac:
                    print(f"Твое здоровъе: {self.life}")
                    cons += self.conset
                    print(f"Концитрация врага: {cons}")
                else:
                    print(f"Твое здоровъе: {self.life}")
                    print(f"Концитрация врага: {cons}")
            elif a_bl[0] == "grom":
                print("Молния!")
                if input(": ") == self.blockgr:
                    print(f"Твое здоровъе: {self.life}")
                    cons += self.conset
                    print(f"Концитрация врага: {cons}")
                else:
                    print("Ты погиб от молнии")
                    sys.exit
