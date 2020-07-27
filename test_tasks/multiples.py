

class Multiples:

    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    def multiples(self, max_value):
        """
        1. For numbers between 0 and max_value check division on 3 or 5.
        2. Sum
        3. Return str result
        """
        res = 0
        for num in range(0, max_value):
            if not num % 3 or not num % 5:
                res += num
        return str(res)


