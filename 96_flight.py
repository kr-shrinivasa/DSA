### Define the required class here...

class Flight:
    def __init__(self, upTime, downTime):
        self.upTime = upTime
        self.downTime = downTime

    def calculateFlight(self):
        n=self.upTime.split(":")
        m=self.downTime.split(":")
        hr=(int(m[0])-int(n[0]))*60
        min=int(m[1])-int(n[1])
        return hr+min


        # Your Code goes here



### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    t1 = input()
    t2 = input()

    f1 = Flight(t1, t2)
    print(f1.calculateFlight())