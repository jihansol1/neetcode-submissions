class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # group (position, speed) of cars and sort in increasing order
        
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []
        for p,s in cars:
            # calculate the arrival time
            arrival_time = (target-p) / s
            # if stack is empty, create a fleet
            if not stack:
                stack.append(arrival_time)
            # stack not empty, fleet exists
            else:
                # fleet that started ahead is slower -> join fleet ahead
                if stack[-1] >= arrival_time:
                    continue
                # fleet that started ahead is faster -> create new fleet
                else:
                    stack.append(arrival_time)

        return len(stack)



        