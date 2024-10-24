import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "hello"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input = "pineapple"
        result = hw1.vowel_count(input)
        expected = 4
        self.assertEqual(expected, result)


    # Part 2
    def test_short_lists_1(self):
        input = [[1,0],[1,2],[1,202,100],[30]]
        result = hw1.short_lists(input)
        expected = [[1,0],[1,2]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        input = [[1], [1, 2,3], [1, 202, 100], [30,10]]
        result = hw1.short_lists(input)
        expected = [[30, 10]]
        self.assertEqual(expected, result)


    # Part 3
    def test_ascending_pairs_1(self):
        input = [[2,1],[3,4,5]]
        result = hw1.ascending_pairs(input)
        expected = [[1,2],[3,4,5]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input = [[3, -1], [4, 22, 3],[1,9,2],[0,0]]
        result = hw1.ascending_pairs(input)
        expected = [[-1, 3], [4, 22, 3],[1,9,2],[0,0]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        input = (data.Price(5,99))
        input2 = (data.Price(2,5))
        result = hw1.add_prices(input, input2)
        expected = (8, 4)
        self.assertEqual(expected,result)

    def test_add_prices_2(self):
        input = (data.Price(1, 879))
        input2 = (data.Price(6, 2315))
        result = hw1.add_prices(input, input2)
        expected = (38, 94)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_angle_1(self):
        input = (data.Rectangle(data.Point(-1,3),data.Point(1,2)))
        result = hw1.rectangle_angle(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_rectangle_angle_2(self):
        input = (data.Rectangle(data.Point(-9, 13), data.Point(-11, 21)))
        result = hw1.rectangle_angle(input)
        expected = 16
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        book_list = \
        [data.Book(["bob", "joe", "rick"], "fire"),
         data.Book(["bob","rick"],"water"),
         data.Book(["joe"],"ice"),
         data.Book(["bob"],"dirt")]
        input = ("bob")
        input2 = (book_list)
        result = hw1.books_by_author(input,input2)
        expected = ['fire','water','dirt']
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        book_list = \
            [data.Book(["bob", "joe", "rick"], "fire"),
             data.Book(["bob", "rick"], "water"),
             data.Book(["joe"], "ice"),
             data.Book(["bob"], "dirt")]
        input = ("rick")
        input2 = (book_list)
        result = hw1.books_by_author(input, input2)
        expected = ['fire','water']
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        input = (data.Rectangle(data.Point(-1,1),data.Point(0,0)))
        result = hw1.circle_bound(input)
        expected = (0.71, (-0.5, 0.5))
        self.assertEqual(expected,result)

    def test_circle_bound_2(self):
        input = (data.Rectangle(data.Point(-8, 7), data.Point(3, -12)))
        result = hw1.circle_bound(input)
        expected = ((10.98), (-2.5, -2.5))
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average_1(self):
        employee_list = \
            [data.Employee("bob",10),
            (data.Employee("rick",12)),
            (data.Employee("joe",9)),
            (data.Employee("rob",14)),
            (data.Employee("fred",7))]
        input = (employee_list)
        result = hw1.below_pay_average(input)
        expected = ["bob","joe","fred"]
        self.assertEqual(expected,result)

    def test_below_pay_average_2(self):
        employee_list = \
            [data.Employee("bob", 19),
             (data.Employee("rick", 23)),
             (data.Employee("joe", 22)),
             (data.Employee("rob", 21)),
             (data.Employee("fred", 20))]
        input = (employee_list)
        result = hw1.below_pay_average(input)
        expected = ['bob', 'fred']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
