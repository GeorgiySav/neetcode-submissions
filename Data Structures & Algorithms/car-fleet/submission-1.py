class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        
        fleets = 0
        fleet_steps = -float('inf')

        for p, s in ps:
            steps = (target - p) / s
            if steps > fleet_steps: # new fleet
                fleets += 1
                fleet_steps = steps
        
        return fleets