# Importing libary for plotting
import matplotlib.pyplot as plt

# function to open,read and plot file data
def plot_data(file_path):
    with open("C:\Users\Ronnie Mushayi\Desktop\coordinates\coordinate_file.csv" , 'r') as file_obj:
        data = file_obj.readlines()

    # Extract x and y coordinates from the data
    x_coords = []
    y_coords = []
    for line in data[1:]:  # Skip the header line
        line = line.strip().split(',')
        x_coords.append(float(line[0]))
        y_coords.append(float(line[1]))

    # Create the scatter plot
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot')
    plt.grid(True)

    # Show the plot
    plt.show()

# Example usage
file_path = "C:\Users\Ronnie Mushayi\Desktop\coordinates\coordinate_file.csv"
plot_data(file_path)

# Fuction to translate and replot

def plot_data(file_path, dx, dy, color):
    # Open the file and read the data
    with open(file_path, 'r') as file_obj:
        data = file_obj.readlines()

    # Extract x and y coordinates from the data
    x_coords = []
    y_coords = []
    for line in data[1:]:
        line = line.strip().split(',')
        x = float(line[0]) + dx  # Translate x-coordinate
        y = float(line[1]) + dy  # Translate y-coordinate
        x_coords.append(x)
        y_coords.append(y)

    # Create the scatter plot with the translated points
    plt.scatter(x_coords, y_coords, color=color)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Translated Scatter Plot')
    plt.grid(True)

    # Show the plot
    plt.show()

# Example usage
file_path = "C:\Users\Ronnie Mushayi\Desktop\coordinates\coordinate_file.csv"
dx = 2.0  # Translation in x-direction
dy = 3.0  # Translation in y-direction
color = 'blue'  # Color for the translated points

plot_data(file_path, dx, dy, color)
