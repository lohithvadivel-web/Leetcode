class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        # Multiply each digit
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                product = a * b
                position1 = i + j
                position2 = i + j + 1

                total = product + result[position2]

                result[position2] = total % 10
                result[position1] += total // 10

        # Convert result to string
        answer = ""
        for digit in result:
            if answer != "" or digit != 0:
                answer += str(digit)

        return answer
