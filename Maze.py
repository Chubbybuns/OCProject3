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
        text = ""
        for line in self.array:

            for cell in line:
        # \n pour retour à la ligne
        pass