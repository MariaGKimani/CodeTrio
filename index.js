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
  
  // Example usage
  const myAnkara = new Ankara("Vibrant Ankara");
  
  console.log(myAnkara.changeDesign(28, "happy")); 
  console.log(myAnkara.changeDesign(20, "sad")); 
  console.log(myAnkara.changeDesign(22, "excited")); 
  