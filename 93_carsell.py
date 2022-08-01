# Your class should be named `CarSell`.
# Your method should be named `getPromisingCustomers`
# Your method should return the indices of customers who are willing to pay greater than or equal to 90% of the car value
class CarSell:
    def __init__(self,lis):
        self.list=lis
    def getPromisingCustomers(self):
        ind=[]
        for i in range(len(self.list)):
            if self.list[i]>=0.9*1000000:
                ind.append(i)
        return ind


if __name__ == "__main__":
    num_customers = int(input())
    customer_proposals = []
    for i in range(num_customers):
        customer_proposals.append(int(input()))

    car_sell = CarSell(customer_proposals)
    for j in car_sell.getPromisingCustomers():
        print(j)