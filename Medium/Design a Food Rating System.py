class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.cuisine_heaps = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = cuisine, rating
            if cuisine not in self.cuisine_heaps:
                self.cuisine_heaps[cuisine] = []
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foods[food]
        self.foods[food] = cuisine, newRating
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            rating, food = heap[0]
            if self.foods[food][1] == -rating:
                return food
            heapq.heappop(heap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
