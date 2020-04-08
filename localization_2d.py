# Helper function to print 2D lists
def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')


# Sense function
def sense(p, colors, measurement, sensor_right):
    q = []
    for i, row in enumerate(colors):
        r = []
        for j, item in enumerate(row):
            hit = (item == measurement)
            r.append(p[i][j] * (hit * sensor_right + (1 - hit) * (1 - sensor_right)))
        q.append(r)
    norm = sum(sum(q, []))
    q = [[item / norm for item in col] for col in q]
    return q


# Move function
def move(p, motion, p_move):
    q = []
    for i, row in enumerate(p):
        r = []
        for j, item in enumerate(row):
            s = (1 - p_move) * item
            s = s + p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[0])]
            r.append(s)
        q.append(r)
    return q


# Localization function
def localize(colors, measurements, motions, sensor_right, p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    for i in range(len(measurements)):
        p = move(p, motions[i], p_move)
        p = sense(p, colors, measurements[i], sensor_right)

    return p


if __name__ == "__main__":
    #################### TEST CASES ##############################
    # Case 1:
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'G'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0, 0]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    print("Probability distribution for case 1:")
    show(p)
    print("\n")

    # Case 2:
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0, 0]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    print("Probability distribution for case 2:")
    show(p)
    print("\n")

    # Case 3:
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0, 0]]
    sensor_right = 0.8
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    print("Probability distribution for case 3:")
    show(p)
    print("\n")

    # Case 4:
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 0], [0, 1]]
    sensor_right = 0.8
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    print("Probability distribution for case 4:")
    show(p)
    print("\n")

    # Case 5:
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 0], [0, 1]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors, measurements, motions, sensor_right, p_move)
    print("Probability distribution for case 5:")
    show(p)
    print("\n")

    # Case 6:
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 0], [0, 1]]
    sensor_right = 0.8
    p_move = 0.5
    p = localize(colors, measurements, motions, sensor_right, p_move)
    print("Probability distribution for case 6:")
    show(p)
    print("\n")

    # Case 7:
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 0], [0, 1]]
    sensor_right = 1.0
    p_move = 0.5
    p = localize(colors, measurements, motions, sensor_right, p_move)
    print("Probability distribution for case 7:")
    show(p)
    print("\n")

    # Case 8:
    colors = [['R', 'G', 'G', 'R', 'R'],
              ['R', 'R', 'G', 'R', 'R'],
              ['R', 'R', 'G', 'G', 'R'],
              ['R', 'R', 'R', 'R', 'R']]
    measurements = ['G', 'G', 'G', 'G', 'G']
    motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
    sensor_right = 0.7
    p_move = 0.8
    p = localize(colors, measurements, motions, sensor_right, p_move)
    print("Probability distribution for case 8:")
    show(p)
    print("\n")
