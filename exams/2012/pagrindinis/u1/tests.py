import u1


def test(path):
    (path / 'U1.txt').write(
        '8',
        '9 5 7 -5 13 -4 11',
        '7 5 -3 12 -5 17 -3',
        '25 7 12 -3 5 -5 7 -5 3',
        '14 5 12 -3 10 -7 8',
        '5 1 -40',
        '33 5 15 -5 9 -3 8',
        '11 5 -12 8 -5 12 -3',
        '13 5 3 -4 25 -5 3',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '9 13 14 25 33',
        '33 32',
        '5 40',
    ]


def test_equal_case(path):
    (path / 'U1.txt').write(
        '2',
        '1 2 8 -8',
        '2 2 8 -9',
    )
    u1.main(path)
    assert (path / 'U1rez.txt').read() == [
        '1 2',
        '1 8',
        '2 9'
    ]
