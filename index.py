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


# Question 3
# class Movie:
#       def __init__(self,title,schedule):
#             self.title = title
#             self.schedule = schedule
#             self.budget = {}
#             self.cast_members =[]
#       def calculate_budget():
#             if self.schedule == "premiere":
      
database =[]
class Baobab:
      def __init__(self,season,power,fruit):
            self.season = season
            self.power = power
            self.fruit = fruit

fruit1 = Baobab("wet","invisible","kiwi")
fruit2 = Baobab("dry","fly","sweetmelon")
database.extend(fruit1,fruit2)

# class Season:
#       def __init__(self,seasons):
#             self.seasons = seasons

#       def predict_fruit(self):
#             for i in database:
#                   if {self.seasons}==i.season:
#                         print(f"{i.fruit} is produced during {self.seasons}")
# s = Season("dry")
# s.predict_fruit()
      
class Drum:
     def __init__(self,sizes,material):
          self.sizes = sizes
          self.materials = material
     def make_sound(self,sound):
           return f"{sound}"
           
class Djembe extends Drum{
      
}
      
