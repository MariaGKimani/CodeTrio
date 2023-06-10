# You are a fashion designer known for your unique and 
# vibrant Ankara designs recently you’ve discovered that some of your fabric
# patterns change their designs based on the temperature and mood of the wearer 
# you want to create a software application that can predict the changes in the fabric design 
# given the mood and temperature data.
# Think about the classes you will need to model the changing Ankara and how to predict the changes.

class Ankara:
    def __init__(self,pattern):
        self.pattern = pattern
    def change_temperature(self,temperature,mood):
            temp = 24
            moodswings = range(6)
            if temperature >= 24 or  moodswings == 1:
                    return f"{self.pattern} is seamless"
            elif temperature >= 24 or moodswings == 5:
             return f"{self.pattern} is stripes"
            else:
                 return f"{self.pattern} is checked"


ankara1 = Ankara("pattern")
print(ankara1.change_temperature(25,2))

# The Great Migration Forecast: Every year, millions of
# wildebeest, zebras and other animals participate in 
# the Great Migration across the Serengeti-Mara ecosystem.
# As a conservationist you want to develop a software system
# that models this migration, predicting the movement of the 
# herds based on weather patterns, river levels, and 
# predator locations. Consider what classes you’ll need 
# to represent the animals, the environment, and the various factors that influence migration.

