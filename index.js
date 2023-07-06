class Ankara {
    constructor(pattern) {
      this.pattern = pattern;
    }
  
    changeDesign(temperature, mood) {
      if (temperature > 24 || mood === "happy") {
        return `${this.pattern} is seamless`;
      } else if (temperature <= 24 || mood === "sad") {
        return `${this.pattern} is stripes`;
      } else {
        return `${this.pattern} is checked`;
      }
    }
  }
  
  const myAnkara = new Ankara("Vibrant Ankara");
  
  console.log(myAnkara.changeDesign(28, "happy")); 
  console.log(myAnkara.changeDesign(20, "sad")); 
  console.log(myAnkara.changeDesign(22, "excited")); 



// question 2

class Migration{
    constructor(riverlevels,weatherpatterns){
        this.riverlevels = riverlevels
        this.weatherpatterns = weatherpatterns
    }
    predict_migrations(){
        if(this.riverlevels ===  "low" && this.weatherpatterns === "dry"){
            return "migration happens"
        }else{
            return "migration does not happen"
        }
    }
}
const migration1 = new  Migration("high","wet")
console.log(migration1.predict_migrations());



// question 5

class Drum{
  constructor(material,size){
    this.material = material
    this.size = size
  }
  playSound(tone){
    return sound
  }
}
class Djembe extends Drum{
  playSound(tone){
    return `Djembe producer ${tone} when hit`
  }
}
class Talkingdrum extends Drum{
  playSound(tone){
    return `Talkingdrum produces ${tone} when hit`
  }
}