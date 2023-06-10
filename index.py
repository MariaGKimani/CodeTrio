# QUESTION 1

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

# Question2
class Migration:
     def __init__(self,weather_patterns,river_levels):           
                self.weather_patterns = weather_patterns
                self.river_levels = river_levels
     def predict_migrations(self):
           if self.river_levels =="low" and self.weather_patterns =="dry":
                 return f" migration happens"
           else:
                 return f"migration does not happen"
           
Migration1 =Migration("dry","low")
print(Migration1.predict_migrations())