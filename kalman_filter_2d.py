from kalman_filter import *

if __name__ == "__main__":
    print('### 2-dimensional example ###')
    measurements = [[1], [2], [3]]

    x = matrix([[0.], [0.]])  # initial state (location and velocity)
    P = matrix([[1000., 0.], [0., 1000.]])  # initial uncertainty
    u = matrix([[0.], [0.]])  # external motion
    F = matrix([[1., 1.], [0, 1.]])  # next state function
    H = matrix([[1., 0.]])  # measurement function
    R = matrix([[1.]])  # measurement uncertainty
    I = matrix([[1., 0.], [0., 1.]])  # identity matrix

    x, P = kalman_filter(x, P, measurements, H, R, I, F, u)
    print("Predicted state x:")
    x.show()
    print("Predicted uncertainty covariance P:")
    P.show()
