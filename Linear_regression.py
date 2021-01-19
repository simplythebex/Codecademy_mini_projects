# find y value for x on a line 
def get_y(m, b, x):
  return (m*x) + b

# calculates error between a point and the line
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[-1]
    y = get_y(m, b, x_point)
    diff = y - y_point
    return abs(diff)
    
# totals the error from all points and the line 
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error
  
# finds values for m (between -10 and 10) ad for b (between -20 and 20)
possible_ms = [m*0.1 for m in range(-100, 101)]
possible_bs = [b * 0.1 for b in range(-200, 201)]
  
# finds the smallest error using a set of data stored in datapoints
smallest_error = (float("inf"))
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error
print(best_m, best_b, smallest_error)

# get_y can now be used to predict an unknown y value for x on a line, using best_m as m and best_b as b in the get_y function.
 
