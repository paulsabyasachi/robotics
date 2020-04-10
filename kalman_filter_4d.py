from kalman_filter import *

if __name__ == "__main__":
    print('### 4-dimensional example ###')

    # Test case 1
    measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
    initial_xy = [5., 10.]

    # # Test case 2
    # measurements = [[1., 4.], [6., 0.], [11., -4.], [16., -8.]]
    # initial_xy = [1., 4.]
    #
    # # Test case 3
    # measurements = [[1., 17.], [1., 15.], [1., 13.], [1., 11.]]
    # initial_xy = [1., 17.]

    dt = 0.1
    # initial state (location and velocity)
    x = matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]])
    # external motion
    u = matrix([[0.], [0.], [0.], [0.]])
    # initial uncertainty: 0 for positions x and y, 1000 for the two velocities
    P = matrix([[0., 0., 0., 0.],
                [0., 0., 0., 0.],
                [0., 0., 1000., 0.],
                [0., 0., 0., 1000.]])
    # state transition matrix
    F = matrix([[1., 0., dt, 0.],
                [0., 1., 0., dt],
                [0., 0., 1., 0.],
                [0., 0., 0., 1.]])
    # measurement function: reflecting the fact that we observe x and y but not the two velocities
    H = matrix([[1., 0., 0., 0.],
                [0., 1., 0., 0.]])
    # measurement uncertainty: use 2x2 matrix with 0.1 as main diagonal
    R = matrix([[0.1, 0.], [0., 0.1]])
    # 4d identity matrix
    I = matrix([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])

    x, P = kalman_filter(x, P, measurements, H, R, I, F, u)
    print("Predicted state x:")
    x.show()
    print("Predicted uncertainty covariance P:")
    P.show()
