from random import choice, choices


class Sudoko:
    def __init__(self, level):
        self.level = level
        self.grid = self.initiate()

    def initiate(self):
        grid = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
                [8, 4, 2, 9, 7, 3, 5, 6, 1],
                [9, 6, 1, 2, 8, 5, 3, 7, 4],
                [2, 8, 6, 3, 4, 9, 1, 5, 7],
                [4, 1, 3, 8, 5, 7, 9, 2, 6],
                [5, 7, 9, 1, 2, 6, 4, 3, 8],
                [1, 5, 7, 4, 9, 2, 6, 8, 3],
                [6, 9, 4, 7, 3, 8, 2, 1, 5],
                [3, 2, 8, 5, 6, 1, 7, 4, 9]]

        for _time in range(2):
            for i in range(3):
                [c1, c2] = choices([3 * i + 0, 3 * i + 1, 3 * i + 2], k=2)
                tmp = []
                for r in range(9):
                    tmp.append(grid[r][c1])
                    grid[r][c1] = grid[r][c2]
                for r in range(9):
                    grid[r][c2] = tmp[r]

        for _time in range(2):
            for i in range(3):
                [r1, r2] = choices([3 * i + 0, 3 * i + 1, 3 * i + 2], k=2)
                tmp = grid[r1]
                grid[r1] = grid[r2]
                grid[r2] = tmp

        for _time in range(2):
            [b1, b2] = choices([0, 1, 2], k=2)
            tmp1, tmp2, tmp3 = grid[b1 * 3], grid[b1 * 3 + 1], grid[b1 * 3 + 2]
            grid[b1 * 3] = grid[b2 * 3]
            grid[b1 * 3 + 1] = grid[b2 * 3 + 1]
            grid[b1 * 3 + 2] = grid[b2 * 3 + 2]
            grid[b2 * 3], grid[b2 * 3 + 1], grid[b2 * 3 + 2] = tmp1, tmp2, tmp3

        return grid

    def check(self):
        for r in range(9):
            if r % 3 == 0:
                box = [[False for i in range(10)],
                       [False for i in range(10)],
                       [False for i in range(10)]]
            row = [False for i in range(10)]
            for c in range(9):
                if row[self.grid[r][c]]:
                    print(f"{self.grid[r][c]} appear again in row {r + 1}")
                    return False
                row[self.grid[r][c]] = True
                box_idx = c // 3
                if box[box_idx][self.grid[r][c]]:
                    b = box_idx + r // 3 * 3
                    print(f"{self.grid[r][c]} appear again in box {b + 1}")
                    return False
                box[box_idx][self.grid[r][c]] = True

        for c in range(9):
            col = [False for i in range(10)]
            for r in range(9):
                if col[self.grid[r][c]]:
                    print(f"{self.grid[r][c]} appear again in col {c + 1}")
                    return False
                col[self.grid[r][c]] = True
        print("Valid")
        return True

    def reset(self):
        self.grid = self.initiate()

    def __check_row(self, r):
        row = [False for i in range(9)]
        for c in range(9):
            if row[self.grid[r][c]]:
                return False
            row[self.grid[r][c]] = True
        return True

    def __check_column(self, c):
        col = [False for i in range(9)]
        for r in range(9):
            if col[self.grid[r][c]]:
                return False
            col[self.grid[r][c]] = True
        return True

    def __check_box(self, r, c):
        box = [False for i in range(9)]
        r, c = r // 3 * 3, c // 3 * 3
        for i in range(2):
            for j in range(2):
                if box[self.grid[r + i][c + j]]:
                    return False
                box[self.grid[r + i][c + j]] = True
        return True

    def __backtrack(self, r, c):
        if r == 8 and c == 8:
            return self.__check_row(r) and self.__check_column and self.__check_box(r, c)
        for v in range(9):
            self.grid[r][c] = v
            if self.__check_row(r) and self.__check_column(c) and self.__check_box(r, c):
                rr, cc = r, c
                while self.grid[rr][cc] != -1:
                    cc += 1
                    if cc == 9:
                        cc,  rr = 0, rr + 1
                    if rr == 9:
                        break
                if rr < 9 and cc < 9 and self.grid[rr][cc] == -1 and self.__backtrack(rr, cc) == False:
                    self.grid[r][c] = -1
                    return False
            self.grid[r][c] = -1
        return True

    def __solvable(self) -> bool:
        is_solvable = True
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] != -1:
                    continue
                self.__backtrack(r, c)
        return is_solvable

    def __str__(self):
        print("\t┌───┬───┬───┬───┬───┬───┬───┬───┬───┐")
        middle = "\t├───┼───┼───┼───┼───┼───┼───┼───┼───┤"
        border = "│"
        for r in range(9):
            s = "\t" + border
            for c in range(9):
                s += " " + str(self.grid[r][c]) + " " + border
            print(s)
            if r < 8:
                print(middle)
        print("\t└───┴───┴───┴───┴───┴───┴───┴───┴───┘")


s = Sudoko(1)
s.__str__()
