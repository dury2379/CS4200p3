class Node(object):
    def __init__(self, state = []):
        self.state = state

    def heuristic(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                horizontal_sum = 0
                vertical_sum = 0
                for k in range(1, 4):
                    if self.state[i][j] == "-":
                        if j + k < len(self.state[i]):

    def evaluate_cell(self, row, column):
        if self.state[row][column] != "-":
            return 0
        horizontal_sum = 0
        vertical_sum = 0
        horizontal_streak = 0
        stop_left = False
        stop_right = False
        for k in range(1, 4):
            horizontal_sum, horizontal_streak, stop_left = self.evaluate_horizontal_neighbor(row, column-k, stop_left, horizontal_streak, horizontal_sum)

    def evaluate_horizontal_neighbor(self, row, column, stop_flag, streak, summation):
        if len(self.state[row]) > column >= 0 and not stop_flag:
            if self.state[row][column] == "X":
                summation += self.evaluate_streak(streak)
                streak += 1
                return summation, streak, stop_flag
            elif self.state[row][column] == "-":
                summation += self.evaluate_streak(streak) / 4
                stop_flag = True
                return summation, streak, stop_flag
            elif self.state[row][column] == "O":
                stop_flag = True
                return summation, streak, stop_flag

    def evaluate_streak(self, streak_number):
        if streak_number == 0:
            return 10
        if streak_number == 1:
            return 20
        if streak_number == 2:
            return 40
        return 150