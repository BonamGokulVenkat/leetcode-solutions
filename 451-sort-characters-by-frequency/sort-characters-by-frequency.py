class Solution:
    def frequencySort(self, s: str) -> str:        
        freq = Counter(s)
        result = []
        
        for char, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            result.append(char * count)
        
        return ''.join(result)