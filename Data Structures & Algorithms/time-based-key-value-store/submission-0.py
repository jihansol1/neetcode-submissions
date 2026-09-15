class TimeMap:

    def __init__(self):
        # use hashmap to store key:[(val1,timestamp1), (val2, timestamp2), (val3, timestamp3), ...]
        self.m = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # stores the key:val at the given timestamp
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        # return a value such that set was called previously, with timestampp_prev <= timesteamp
        # If there are multiple such values, return the value associated with largest timestamp_prev
        # if there are no values return ""

        # binary search to retrieve the timestamps

        res, values = "", self.m.get(key, [])
        l, r = 0, len(values) - 1
        # find key in map and go to its list and find val associated with timestamp
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res


        

        
