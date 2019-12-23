from Maze.Wall import Wall
from Maze.Start import Start
from Maze.Finish import Finish
from Maze.Path import Path


class Maze:
    def __init__(self):  # constructeur
        self.array = []

    def load_maze_from_file(self):
        maze_file = open("Maze/Maze.txt", "r")
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
                initial = cell.initial()
                text += initial
            text += "\n"
        maze_file = open("savedmaze.txt", "w")
        maze_file.write(text)
        maze_file.close()
