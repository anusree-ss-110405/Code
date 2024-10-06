class Solution {
    public boolean areSentencesSimilar(String s1, String s2) {
        String shorter = s1.length() > s2.length() ? s2:s1;
        String longer = shorter.equals(s1) ? s2:s1;
        String[] shortwords = shorter.split(" ");
        String[] longwords = longer.split(" ");
        int diffs = 0;
        int i=0,j=0;
        for(; i < shortwords.length && j < longwords.length; ){
            if(shortwords[i].equals(longwords[j])){
                i++;
                j++;
            }
            else{
                diffs++;
                if(diffs > 1){
                    break;
                }
                while(j< longwords.length && !longwords[j].equals(shortwords[i])){
                    j++;
                }
            }
        }
        if((diffs == 1 && i == shortwords.length && j == longwords.length) || (diffs == 0 && i == shortwords.length)){
            return true;
        }
        i = shortwords.length - 1;
        j = longwords.length - 1;
        diffs=0;
        for(;i>=0 && j>=0;){
            if(shortwords[i].equals(longwords[j])){
                i--;
                j--;
            }else{
                diffs++;
                if(diffs > 1){
                    return false;
                }
                while(j>=0 && !longwords[j].equals(shortwords[i])){
                    j--;
                }
            }
        }
        return (diffs == 1 && i==-1 && j==-1) || (diffs == 0 && i == -1);
    }
}