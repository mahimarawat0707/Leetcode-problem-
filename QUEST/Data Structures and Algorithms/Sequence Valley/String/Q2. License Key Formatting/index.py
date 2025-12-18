class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        # Eliminate all dashes
        S = S.replace('-', '')
        
        head = len(S) % K
        
        grouping = []
        
        # Special handle for first group
        if head:
            grouping.append( S[:head] )
        
        # General case:
        for index in range(head, len(S), K ):
            grouping.append( S[ index : index+K ] )
        
        
        # Link each group togetger and separated by dash '-'
        return '-'.join( grouping ).upper()