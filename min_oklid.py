import math

# Define the points
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Define a function to calculate Euclidean distance
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Calculate the distances between each pair of points
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Find the minimum distance
min_distance = min(distances)
print("Minimum Euclidean Distance:", min_distance)
