class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        Count total collisions on the road.
        
        Key insight: 
        - Cars moving left at the beginning (left edge) escape without collision
        - Cars moving right at the end (right edge) escape without collision
        - All other moving cars (L or R) will eventually collide
        
        Time: O(n), Space: O(1)
        """
        s = directions
        n = len(s)
        
        # Strip leading 'L's - these cars move off the left edge
        left = 0
        while left < n and s[left] == 'L':
            left += 1
        
        # Strip trailing 'R's - these cars move off the right edge
        right = n - 1
        while right >= 0 and s[right] == 'R':
            right -= 1
        
        # Count all remaining 'L' and 'R' - each will cause 1 collision
        collisions = 0
        for i in range(left, right + 1):
            if s[i] in ['L', 'R']:
                collisions += 1
        
        return collisions