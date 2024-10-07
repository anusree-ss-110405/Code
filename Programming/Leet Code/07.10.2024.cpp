class Solution {
public:
    int minLength(string s) {
        stack<int> l;
        for(char c:s){
            if(!l.empty() && ((c=='B' && l.top()=='A')||(c=='D' && l.top()=='C')))
                l.pop();
            else
                l.push(c);
        }
        return l.size();
    }
};