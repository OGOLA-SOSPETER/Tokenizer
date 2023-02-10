#A fuel economy tool.
#Accept input of petrol pumped, milage of car, date etc.
# to calc kms per litre. graph that shit up and you'll be looking at an A!
import time
import datetime
import matplotlib.pyplot as plt

class Odometer:

    petrol_pumped = 0
    date_today = 20230209
    milage = 0
    fuel_economy = 0
    FuelStation = ''

    def getdata(self):
        self.petrol_pumped = float(input('Enter the petrol pumped: '))
        self.milage = float(input('Enter the mileage covered: '))
        self.date_today = time.asctime( time.localtime(time.time()) )
        self.FuelStation = input('Enter the fueling station:')

    def GetFuelEconomy(self):

        self.fuel_economy = self.petrol_pumped / self.milage



    def DisplayFuelEconomy(self):
        p = '\t'*10
        pp = '\t'*12
        result = {'date': self.date_today, "fuel economy": self.fuel_economy}
        print('\n')
        print(p + '_'*70)
        print('\t'*16 + self.FuelStation.upper())
        print(pp + 'Petrol Pumped: ' + '\t'*5, self.petrol_pumped)
        print(pp + 'Mileage: ' + '\t'*6, self.milage)
        print('\t'*13, '-'*40)
        print(pp + 'Fuel Economy: ' + '\t' * 5, self.milage)
        print('\t'*13, '-'*40)

        print(p + 'Date:' + '\t'*2 , self.date_today)

        print(pp + '_'*70)

#To visualize the fuel economy data,
# you can use a library like matplotlib to plot a line graph.



    def fuel_economy_calculator():
        # accept inputs
        litres_pumped = float(input("Enter the amount of petrol pumped in litres: "))
        odometer_reading = float(input("Enter the current odometer reading in km: "))
        date = input("Enter the date (YYYY-MM-DD): ")

        # calculate fuel economy
        fuel_economy = odometer_reading / litres_pumped

        # store the result in a dictionary along with date
        result = {"date": date, "fuel_economy": fuel_economy}

        # return the result
        return result

    # call the function and print the result
    result = fuel_economy_calculator()
    print("On", result["date"], "you got", result["fuel_economy"], "km/l")


    def plot_fuel_economy(results):
        dates = [result["date"] for result in results]
        fuel_economies = [result["fuel_economy"] for result in results]

        # plot the data
        plt.plot(dates, fuel_economies)

        # add labels and title
        plt.xlabel("Date")
        plt.ylabel("Fuel Economy (km/l)")
        plt.title("Fuel Economy over Time")

        # show the plot
        plt.show()

    # create a list to store multiple results
    results = []

    # call the fuel economy calculator multiple times and store the results in the list
    for i in range(2):
        result = fuel_economy_calculator()
        results.append(result)

    # plot the results
    plot_fuel_economy(results)


Odom1 = Odometer()
#Odom1.getdata()
#Odom1.GetFuelEconomy()
#Odom1.DisplayFuelEconomy()
Odom1.plot_fuel_economy()
