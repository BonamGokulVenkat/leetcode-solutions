class Solution {
    public boolean isAnagram(String s, String t) {
        int slen=s.length();
        int tlen=t.length();
        if(slen!=tlen) return false;
        int[] map=new int[26];;
        for(char ch:s.toCharArray()){
            map[ch-'a']+=1;
        }
        for(char ch:t.toCharArray()){
            map[ch-'a']-=1;
        }
        for(int num:map){
            if(num!=0) return false;
        }
        return true;
    }
}