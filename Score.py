def add_score(points):
    try:
        new_points = points
        with open('scores.txt', 'r') as score:
            user_points = score.read()
        with open('scores.txt', 'w') as sc:
            new_points = int(user_points) + int(points)
            sc.write(str(new_points))

    except IOError:
        with open('scores.txt', 'w') as score:
            score.write(str(new_points))
    print(new_points)
