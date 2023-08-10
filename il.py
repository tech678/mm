import numpy as np
import matplotlib.pyplot as plt

def func(random_x,random_y,polygon_vertices):
  cnt = 0
  for i,j in zip(random_x, random_y):
    point_x = i
    point_y = j
    intersections = 0
    # Loop through each edge of the polygon
    for i in range(len(polygon_vertices)):
        x1, y1 = polygon_vertices[i]
        x2, y2 = polygon_vertices[(i + 1) % len(polygon_vertices)]  # Next vertex

        # Check for intersection
        if (y1 > point_y) != (y2 > point_y):
            if point_x < (x2 - x1) * (point_y - y1) / (y2 - y1) + x1:
                intersections += 1

    # Determine if the point is inside the polygon
    is_inside = intersections % 2 == 1
    if(is_inside):
      cnt+=1
  return cnt

def plot_polygon(vertices, random_x, random_y):
    vertices.append(vertices[0])
    x_values = [vertex[0] for vertex in vertices]
    y_values = [vertex[1] for vertex in vertices]
    plt.plot(x_values, y_values, marker='o')
    #plt.scatter(random_x, random_y, marker='o', color='green')
    for i,j in zip(random_x,random_y):
      plt.plot(i, j, marker='o', color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of Irregular Lamina')
    plt.axis('equal')
    plt.show()
    
total = 100
start = 1
end = 8
polygon_vertices = [(2,4),(3,2),(3,3),(5,2),(7,4),(3,5)]
random_x = np.random.uniform(start, end, total)
random_x = [i for i in random_x]
random_y = np.random.uniform(start, end, total)
random_y = [i for i in random_y]
print(random_x)
print(random_y)
count = func(random_x,random_y,polygon_vertices)
print("Number of points insize irregular lamina:",count)
plot_polygon(polygon_vertices, random_x, random_y)
area = (count/total)*35
print("Area of irregular lamina:",area)
