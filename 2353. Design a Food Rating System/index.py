from typing import List
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        
        self.cuisine_heap = {}
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = (c, r)
            if c not in self.cuisine_heap:
                self.cuisine_heap[c] = []
            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]
        while heap:
            rating, food = heap[0]
            _, actual_rating = self.food_info[food]
            if -rating == actual_rating:
                return food
            heapq.heappop(heap)


if __name__ == "__main__":
    foods = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"]
    cuisines = ["korean","japanese","japanese","greek","japanese","korean"]
    ratings = [9,12,8,15,14,7]

    obj = FoodRatings(foods, cuisines, ratings)
    print(obj.highestRated("korean"))
    print(obj.highestRated("japanese"))
    
    obj.changeRating("sushi", 16)
    print(obj.highestRated("japanese")) 

    obj.changeRating("ramen", 16)
    print(obj.highestRated("japanese"))
