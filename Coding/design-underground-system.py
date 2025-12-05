# bloomberg, amazon
# design question
# Design Underground System

# time is o(1) for each operation
# approach: 
# only trick is to identify how to use the hashmap, 2 hashmaps are needed here
# no need to remove the id after checkout, but in real world this needs to be done as data will grow
# store id with station name and start time, at checkout: find id from checkinmap and 
# create a route tuple: with total time and count of trips


class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # id -> station, time
        self.totalMap = {} # (startstation, endStation) -> [total, count]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # one station at a time
        self.checkInMap[id] = [stationName, t]
        return


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, time = self.checkInMap[id]
        route = (start_station, stationName)
        total_time = t - time
        if route not in self.totalMap:
            self.totalMap[route] = [0, 0]
        self.totalMap[route][0] += total_time
        self.totalMap[route][1] += 1
        return
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = self.totalMap[(startStation, endStation)][0]
        trip_count = self.totalMap[(startStation, endStation)][1]
        return total / trip_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)