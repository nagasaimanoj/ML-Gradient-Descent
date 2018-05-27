from numpy import genfromtxt, mean


class GradientDescent():

    def __init__(self):
        self.initial_b = 0
        self.initial_m = 0

    def _step_gradient(self, b, m, learningRate):
        N = len(self.x_list)

        predected_y = m * self.x_list + b
        y_difference = self.y_list - predected_y

        b_gradient = sum(2 / N * y_difference)
        m_gradient = sum(2 / N * self.x_list * y_difference)

        b += learningRate * b_gradient
        m += learningRate * m_gradient

        return b, m

    def train_model(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list

        b = self.initial_b
        m = self.initial_m

        num_iterations = len(self.x_list) * 100
        learning_rate = 1 / num_iterations

        for _ in range(num_iterations):
            b, m = self._step_gradient(b, m, learning_rate)

        self.b, self.m = b, m

    def predect(self, *x):
        return x * self.m + self.b

    @property
    def variable_set(self):
        predected_y = self.x_list * self.m + self.b
        avg_error = mean((self.y_list - predected_y) ** 2)

        return self.b, self.m, avg_error


if __name__ == '__main__':
    data_set = genfromtxt("data.csv", delimiter=",")
    x = data_set[:, 0]
    y = data_set[:, 1]

    gradient_descent = GradientDescent()
    gradient_descent.train_model(x, y)

    b, m, error = gradient_descent.variable_set

    print("intercept =", b)
    print("slope =", m)
    print("error =", error)