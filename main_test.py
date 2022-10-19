
import main


def test_main():
    numbers = [5, 4, 3, 2, 1]

    others = numbers
    for i in range(len(numbers)-1):
        findmin(others)
        firstval, *others = others
        numbers[i] = firstval

    print(numbers)
    assert numbers[0] == 1
    assert numbers[1] == 2
    assert numbers[2] == 3
    assert numbers[3] == 4
    assert numbers[4] == 5
# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"
