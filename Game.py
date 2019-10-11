import pygame
from Maze import Maze
maze = Maze() #création de l'objet
# Appel des méthodes
maze.load_maze_from_file()

# jeu

maze.save_maze()


print(len(maze.array))
print(maze.array)
print(maze.array[0][0])
print(maze.array[0][1])

# Exporter maze en .txt
# revoir les indentations
# git, créer repo et faire des push, commits

