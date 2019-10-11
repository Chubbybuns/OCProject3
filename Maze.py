from Wall import Wall
from Start import Start
from Finish import Finish
from Path import Path

class Maze:
    def __init__(self):  # constructeur
        self.array = []
        self.height = 0
        self.width = 0

    def load_maze_from_file(self):
        # lire le fichier .txt
        maze_file = open("Maze.txt", "r")

        # remplir l'array avec le .txt
        for line in maze_file:
            maze_line = []
            for character in line:
                if character != "\n":
                    if character == "S":
                        maze_start = Start()
                        maze_line.append(maze_start)
                    if character == "W":
                        maze_wall = Wall()
                        maze_line.append(maze_wall)
                    if character == "F":
                        maze_finish = Finish()
                        maze_line.append(maze_finish)
                    if character == "P":
                        maze_path = Path()
                        maze_line.append(maze_path)
            self.array.append(maze_line)



    def save_maze(self):
        # Création d'une variable text pour stocker les caractères
        text = ""
        # Remplir le texte à partir de l'array
        for line in self.array:
            for cell in line:
                if isinstance(cell, Finish):
                    text += "F"
                if isinstance(cell, Path):
                    text += "P"
                if isinstance(cell, Start):
                    text += "S"
                if isinstance(cell, Wall):
                    text += "W"
            text += "\n"
        # Création d'un fichier .txt qui écrase l'ancien .txt s'il existe
        maze_file = open("savedmaze.txt", "w")
        maze_file.write(text)
        maze_file.close()
