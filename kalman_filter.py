from matrix import *


# Kalman Filter implementation
def kalman_filter(x, P, measurements, H, R, I, F, u):
    for n in range(len(measurements)):
        # measurement update
        Z = matrix([measurements[n]])
        y = Z.transpose() - (H * x)
        S = H * P * H.transpose() + R
        K = (P * H.transpose()) * S.inverse()
        x = x + K * y
        P = (I - K * H) * P

        # prediction
        x = F * x + u
        P = F * P * F.transpose()

    return x, P
