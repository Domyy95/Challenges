import os

DIRPATH = os.path.dirname(os.path.realpath(__file__))


class Demon:
    def __init__(self,index, Sc, Tr, Sr, Na):
        self.index = index
        self.Sc = Sc
        self.Tr = Tr
        self.Sr = Sr
        self.Na = Na

    def remainNa(self, t):
        return sum(self.Na[:t])

class Solver:
    def __init__(self, file_name):
        self.file_name = file_name
        self.demons = []

        with open(f"{DIRPATH}/data/{file_name}.txt", 'r') as f:
            file_content = f.read().split("\n")

            # First line
            self.Si = int(file_content[0].split(" ")[0])
            self.Smax = int(file_content[0].split(" ")[1])
            self.T = int(file_content[0].split(" ")[2])
            self.D = int(file_content[0].split(" ")[3])

            # Demons
            for i in range(1, self.D+1):
                demons_string = file_content[i].split(" ")
                sc, tr, sr, na = int(demons_string[0]), int(demons_string[1]), int(demons_string[2]), int(demons_string[3])
                na_list = [int(demons_string[j]) for j in range(4,4+na)]
                self.demons.append(Demon(i-1,sc,tr,sr,na_list))

            self.actual_stamina = self.Si
            self.to_choose = set(range(self.D))
            self.stamina_up = {}
            self.solution = []

    def print_global_status(self,t, choosen, heuristic_d):
        print("--- --- --- --- ---")
        print(f"Time {t} Choosen: {choosen}\nStamina: {self.actual_stamina} \nStamina Ups: {self.stamina_up} \nDemons H: {heuristic_d}")


    def choose_demon(self, n, t):
        if n in self.to_choose:
            if self.demons[n].Tr + t in self.stamina_up:
                self.stamina_up[self.demons[n].Tr + t] += self.demons[n].Sr
            else:
                self.stamina_up[self.demons[n].Tr + t] = self.demons[n].Sr

            self.solution.append(n)
            self.to_choose.remove(n)
        else:
            raise Exception("DEMON GIA ASSEGNATO") 


    def stamina_lamda(self):
        return 1 - self.actual_stamina/self.Smax


    def logic_formula(self, demon, t):
        # return (self.actual_stamina/demon.Sc) * demon.remainNa(self.T - t) + self.stamina_lamda() * (demon.Sr/demon.Tr) # BEST ONE
        
        # return demon.remainNa(self.T - t)
        # return  (1/demon.Sc) * demon.remainNa(self.T - t) + self.stamina_lamda() * (demon.Sr/demon.Tr)
        # return demon.remainNa(self.T - t) + self.stamina_lamda() * (self.actual_stamina - demon.Sc + demon.Sr/demon.Tr)
        # return demon.remainNa(self.T - t) + self.stamina_lamda() * (self.actual_stamina - demon.Sc) * demon.Sr/demon.Tr


    def solve(self):
        for t in range(0,self.T):
            self.actual_stamina += self.stamina_up[t] if t in self.stamina_up else 0
            max = -1
            choosen = -1
            heuristic_d = []
            # Demons
            for d in self.demons:
                if d.index in self.to_choose and d.Sc <= self.actual_stamina:
                    temp = self.logic_formula(d,t)
                    # heuristic_d.append(f'{d.index}: {temp}')
                    if temp > max:
                        max = temp  
                        choosen = d.index


            if choosen != -1:
                self.choose_demon(choosen, t)

            # self.print_global_status(t, choosen, heuristic_d)


    def to_output(self):
        with open(f"./out/{self.file_name}_out.txt", "w") as file:
            for demon in self.solution:
                file.write(f"{demon}\n")

            for demon_remain in list(self.to_choose):
                file.write(f"{demon_remain}\n")                






