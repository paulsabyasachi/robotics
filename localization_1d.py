# Sense function
def sense(p, world, measurement, pHit, pMiss):
    q = []
    for i in range(len(p)):
        hit = (measurement == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


# Move function
def move(p, motion, pExact, pOvershoot, pUndershoot):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - motion) % len(p)]
        s = s + pOvershoot * p[(i - motion - 1) % len(p)]
        s = s + pUndershoot * p[(i - motion + 1) % len(p)]
        q.append(s)
    return q


# Localization function
def localize(p, world, measurements, pHit, pMiss, motions, pExact, pOvershoot, pUndershoot):
    for k in range(len(measurements)):
        p = sense(p, world, measurements[k], pHit, pMiss)
        p = move(p, motions[k], pExact, pOvershoot, pUndershoot)
    return p


if __name__ == "__main__":
    p = [0.2, 0.2, 0.2, 0.2, 0.2]
    world = ['green', 'red', 'red', 'green', 'green']
    measurements = ['red', 'red']
    motions = [1, 1]
    pHit = 0.6
    pMiss = 0.2
    pExact = 0.8
    pOvershoot = 0.1
    pUndershoot = 0.1
    print("World: ", world)
    print("Measurements: ", measurements)
    print("Motions: ", motions)
    p = localize(p, world, measurements, pHit, pMiss, motions, pExact, pOvershoot, pUndershoot)
    print("Probabilities after executing localization:")
    print(p)
    print("Robot now most likely in position:")
    print(p.index(max(p)))
