class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size()-1;
        int max_contain = 0;
        while (left < right) {
            int area = (right - left) * min(heights[left], heights[right]);
            max_contain = max(max_contain, area);

            if (heights[left] <= heights[right]) {
                left++;
            }
            else if (heights[left] > heights[right]) {
                right--;
            }
        }
        return max_contain;
    }
};
