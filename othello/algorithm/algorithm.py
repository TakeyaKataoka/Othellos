import numpy as np

class Algorithm():
    def __init__(self, pattern) -> None:

        self.pattern = pattern

        self.base_scores = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 30, -10, 2,  1,  1, 2, -10, 30, 0],
            [0, -10, -20, -3, -3, -3, -3, -20, -10, 0],
            [0, 2, -3, 2, 0, 0, 2, -3, 2, 0],
            [0, 1, -3, 0, 0, 0, 0, -3, 1, 0],
            [0, 1, -3, 0, 0, 0, 0, -3, 1, 0],
            [0, 2, -3, 2, 0, 0, 2, -3, 2, 0],
            [0, -10, -20, -3, -3, -3, -3, -20, -10, 0],
            [0, 30, -10, 2,  1,  1, 2, -10, 30, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        ])

        if self.pattern == 'S':
            self.eval_scores = self.eval_hand()
        """
        [[70, -9, 37, 7, 7, 37, -9, 70], 
        [-9, -30, 28, -3, -3, 28, -30, -9], 
        [37, 28, 34, 7, 7, 34, 28, 37], 
        [7, -3, 7, -2, -2, 7, -3, 7], 
        [7, -3, 7, -2, -2, 7, -3, 7], 
        [37, 28, 34, 7, 7, 34, 28, 37], 
        [-9, -30, 28, -3, -3, 28, -30, -9], 
        [70, -9, 37, 7, 7, 37, -9, 70]]
        """


    def eval_hand(self):
        w = -2
        point = 0
        points =[]
        points_s = []

        for y in range(1, 9):
            for x in range(1, 9):
                if x == 0 or x == 9 or y == 0 or y == 9:
                    points.append(point)
                for v in [-1, 0, 1]:
                    for h in [-1, 0, 1]:
                        if v == 0 and h == 0:
                            point += self.base_scores[y + v,  x + h]
                        else:
                            point += w * self.base_scores[y + v,  x + h]
                points.append(point)
                point = 0
            points_s.append(points) 
            points =[]
        
        return points_s
