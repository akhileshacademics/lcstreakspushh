class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        n, m = len(matrix), len(matrix[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        result = []

        while top <= bottom and left <= right:

            # top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
