import sys


def count(config, nums):
    if config == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in config else 1

    result = 0

    if config[0] in ".?":
        result += count(config[1:], nums)

    if config[0] in "#?":
        if (
            nums[0] <= len(config)
            and "." not in config[: nums[0]]
            and (nums[0] == len(config) or config[nums[0]] != "#")
        ):
            result += count(config[nums[0] + 1 :], nums[1:])

    return result


def main():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        ans = 0
        for line in lines:
            config, nums = line.split()
            # we store nums in a tuple because it is impossible to mutate from our function
            nums = tuple(map(int, nums.split(",")))
            ans += count(config, nums)
        print(ans)


if __name__ == "__main__":
    main()
