class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings.sort()
        covered_x = set()
        for _, group in groupby(buildings, lambda build: build[0]):
            for build in list(group)[1:-1]:
                covered_x.add(tuple(build))

        buildings.sort(key=lambda build: build[1])
        count = 0
        for _, group in groupby(buildings, lambda build: build[1]):
            for build in list(group)[1:-1]:
                if tuple(build) in covered_x:
                    count += 1
        return count
