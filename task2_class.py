# Importing libary for plotting
import matplotlib.pyplot as plt
import cvs

#class represents a simple point in 2D
class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def translate(self, dx, dy):
    """
    Moves the point by dx units in the x-direction and dy units in the y-direction.
    """
    self.x += dx
    self.y += dy

  def __str__(self):
    """
    Defines how the Point object is represented as a string.
    """
    return f"({self.x}, {self.y})"

def read_and_plot_points(filename, color):
  """
  Reads X and Y coordinates from a text file, creates a list of Point objects,
  and plots them on a scatterplot with a specified colour.
  
  """
  points = []
  with open("coordinates_file.csv", 'r') as file:
    for line in file:
      x, y = map(float, line.strip().split())
      points.append(Point(x, y))

  x_coords = [point.x for point in points]
  y_coords = [point.y for point in points]
  plt.scatter(x_coords, y_coords, color=color)
  plt.xlabel("X-coordinate")
  plt.ylabel("Y-coordinate")
  plt.title("Points before translation" if color == 'blue' else "Translated Points")
  plt.grid(True)
  plt.show()


def main():
  filename = "coordinates_file.csv"

  # Plot initial points
  read_and_plot_points(filename, 'blue')

  # Move (translate) the points
  for point in points:
    point.translate(2, 3)

  # Replot translated points in a different color
  read_and_plot_points(filename, 'red')


if __name__ == "__main__":
  main()
