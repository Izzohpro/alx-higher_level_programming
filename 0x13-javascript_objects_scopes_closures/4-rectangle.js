#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      const izzoh = [];
      for (let k = 0; k < this.width; k++) izzoh.push('X');
      console.log(`${izzoh.join('')}`);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
}

module.exports = Rectangle;
