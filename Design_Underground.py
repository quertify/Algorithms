"""
An underground railway system is keeping track of customer travel times between different stations. 
They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that happened directly, \
meaning a check in at startStation followed by a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. 
If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.
Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],
[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);mer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
"""
#  customer = {id:[{starttime,startlocation,endtime,endlocation}]}

class UnderGroundSystem:
    def __init__(self)-> None:
        self.customer = {} # id:("station",time) 
        self.station_dist = {}
        # self.station_dist = {("start_end"): [end-start]}
        pass
    def checkIn(self, id: int , stationName:str , t:int )-> None:
        """
        if customer not exists, add id to customer 
        else append startTime, startLocation to the list of dictionary
        """
        if id not in self.customer:
            self.customer[id]=[{"starttime":t,"startlocation": stationName}]
        else:
            self.customer[id].append({"starttime":t,"startlocation": stationName})
        pass
    def checkOut(self, id: int , stationName:str , t:int) -> None:
        """
        append endTime and endLocation to the list of dictionary
        station_dict update startlocation_endlocation and append the difference of end and start to the list
        """
        resp = self.customer[id][-1]
        resp["endtime"] = t
        resp["endlocation"] = stationName
        stations = f"{resp["startlocation"]}_{stationName}"
        if stations not in self.station_dist:
            self.station_dist[stations]= [t- resp["starttime"]]
        else:
            self.station_dist[stations].append(t-resp["starttime"])
        pass
    def getAverageTime(self, start:str, end:str)-> float:
        """
        calculate the sum/count of given start and end from station_dic
        """
        stations =  f"{start}_{end}"
        dist = self.station_dist[stations]
        count = len(dist)
        sum_of_distance = sum(dist)
        return sum_of_distance/count

undergroundSystem = UnderGroundSystem()
print(undergroundSystem.checkIn(45, "Leyton", 3))
print(undergroundSystem.checkIn(32, "Paradise", 8))
print(undergroundSystem.checkIn(27, "Leyton", 10))
print(undergroundSystem.checkOut(45, "Waterloo", 15))
print(undergroundSystem.checkOut(27, "Waterloo", 20))
print(undergroundSystem.checkOut(32, "Cambridge", 22))
print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
print(undergroundSystem.checkIn(10, "Leyton", 24))
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
print(undergroundSystem.checkOut(10, "Waterloo", 38))
print(undergroundSystem.getAverageTime("Leyton", "Waterloo")) 