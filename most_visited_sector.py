from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # // Only first and last numbers(start and end of the give array) matters... why?
        # // The entire marathon has no track sector gap.
        # // Which means.. it doesn't matter how many times we rotate.. it will just cancel out...
        # // Cancel out means: if we visit 1,2,3,4 all 1 times.. do we get the max? no.. because all are the same..
        # // which means... if we visit [1,3,1,2], whatever is in between doesn't matter..
        # //
        # // And there can be only 2 cases:
        # // Case 1 : If start <= end
        # //     --->> In this case we return the range [start, end].
        # // Case 2 : If end < start
        # //     --->> In this case we return return the range [1, end] + range [start, n]
        # //
        # // What if we visited [1,1] -->> Invalid input because on the Constraints it says:
        # //                               rounds[i] != rounds[i + 1]
        l = []
        length = len(rounds)
        start = rounds[0]
        end = rounds[-1]

        if start <= end:
            while start <= end:
                l.append(start)
                start += 1
        else:
            x = 1

            while x <= end:
                l.append(x)
                x += 1
            
            while start <= n:
                l.append(start)
                start += 1
        return l
