from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # res starts as the total number of students (those unable to eat)
        res = len(students)
        # Creating a Counter for student preferences: {0: count, 1: count}
        cnt = Counter(students)
        
        # Traversing through the sandwiches stack from top to bottom
        for s in sandwiches:
            # Check if there are students remaining who want this type of sandwich (s)
            if cnt[s] > 0:
                # A student takes the sandwich.
                cnt[s] -= 1
                # Decrement the number of students *unable* to eat.
                res -= 1
            else: 
                # No student is willing to eat the current sandwich (s). The process stops.
                return res
                
        # If the loop finishes, all students ate.
        return res
        