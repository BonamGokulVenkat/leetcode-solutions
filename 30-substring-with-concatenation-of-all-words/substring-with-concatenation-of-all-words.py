class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len=len(words[0])
        word_count=len(words)
        total_len=word_len*word_count
        freq_w=defaultdict(int)
        if total_len>len(s):
            return []
        for w in words:
            freq_w[w]+=1
        
        ans=[]
        for i in range(word_len):
            left=i
            right=i
            freq_s=defaultdict(int)
            count=0
            while right+word_len<=len(s):
                word=s[right:right+word_len]
                right+=word_len

                if word not in words:
                    freq_s.clear()
                    count=0
                    left=right
                    continue
                freq_s[word]+=1
                count+=1
                while freq_s[word]>freq_w[word]:
                    left_w=s[left:left+word_len]
                    freq_s[left_w]-=1
                    count-=1
                    left+=word_len
                if count==word_count:
                    ans.append(left)
                    left_w=s[left:left+word_len]
                    freq_s[left_w]-=1
                    count-=1
                    left+=word_len
        return ans

                