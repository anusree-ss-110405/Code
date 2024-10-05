class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;

        vector<int> s1Count(26, 0), s2Count(26, 0);

        // Count frequencies of characters in s1 and the first window in s2
        for (int i = 0; i < s1.length(); ++i) {
            s1Count[s1[i] - 'a']++;
            s2Count[s2[i] - 'a']++;
        }

        int matches = 0;
        for (int i = 0; i < 26; ++i) {
            if (s1Count[i] == s2Count[i]) matches++;
        }

        // Sliding window
        for (int i = 0; i < s2.length() - s1.length(); ++i) {
            if (matches == 26) return true;

            // Slide the window: add new character on the right
            int r = s2[i + s1.length()] - 'a';
            int l = s2[i] - 'a';

            s2Count[r]++;
            if (s1Count[r] == s2Count[r]) {
                matches++;
            } else if (s1Count[r] + 1 == s2Count[r]) {
                matches--;
            }

            // Remove the leftmost character from the window
            s2Count[l]--;
            if (s1Count[l] == s2Count[l]) {
                matches++;
            } else if (s1Count[l] - 1 == s2Count[l]) {
                matches--;
            }
        }

        return matches == 26;
    }
};
