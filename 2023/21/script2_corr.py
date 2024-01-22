import sys
from collections import deque

# Solution based on quadratic relation between nb of steps and nb of reachable spots
def main_func():
    with open(sys.argv[1], "r") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))

        start_pos = next(
            (row, col)
            for row, row_content in enumerate(lines)
            for col, char in enumerate(row_content)
            if char == "S"
        )

        def f(nb_expansions, size, original_nb_steps):
            ans = set()
            seen = {start_pos}
            q = deque(
                [
                    (
                        start_pos[0],
                        start_pos[1],
                        original_nb_steps + 2 * size * nb_expansions,
                    )
                ]
            )
            while q:
                row, col, r_steps = q.popleft()
                if r_steps % 2 == 0:
                    ans.add((row, col))
                if r_steps == 0:
                    continue
                for new_row, new_col in [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ]:
                    if lines[new_row % size][new_col % size] == "#" or (
                        (new_row, new_col) in seen
                    ):
                        continue
                    seen.add((new_row, new_col))
                    q.append((new_row, new_col, r_steps - 1))
            return len(ans)

        total_steps = 26501365
        size = len(lines)
        original_nb_steps = total_steps % (2 * size)
        nb_expansions = 0
        res = []
        while True:
            res.append(f(nb_expansions, size, original_nb_steps))
            nb_expansions += 1

            if len(res) >= 4:
                fd = [res[1] - res[0], res[2] - res[1], res[3] - res[2]]
                sd = [fd[1] - fd[0], fd[2] - fd[1]]
                if sd[0] == sd[1]:
                    break
                else:
                    res.pop(0)
        print(res)
        print(nb_expansions)

        offset = nb_expansions - 4
        alpha, beta, gamma, _ = res
        c = alpha
        a = (gamma + alpha - 2 * beta) / 2
        b = beta - alpha - a

        def g(x):
            return a * x**2 + b * x + c

        print(g(0), g(1), g(2), g(3))
        print(g(total_steps // (2 * size) - offset))


if __name__ == "__main__":
    main_func()
