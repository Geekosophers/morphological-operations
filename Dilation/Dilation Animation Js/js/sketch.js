let squares = [];

function setup() {
    let width = window.innerWidth;
    let height = window.innerHeight;
    createCanvas(width, height);

    for (let i = 0; i < 5; i++) {
        for(let j = 0; j< 5; j++){
            let b = new Square(i*(width/10), j*(width/10), width/10);
            squares.push(b);
        }
    }
}

function mousePressed() {
    for (let i = 0; i < squares.length; i++) {
        squares[i].clicked(mouseX, mouseY);
    }
}

function draw() {
    background(255, 255, 255);
    for (let i = 0; i < squares.length; i++) {
        squares[i].show();
    }
}

class Square {
  constructor(x, y, length) {
    this.x = x;
    this.y = y;
    this.length = length
    this.brightness = 0;
  }

  clicked(px, py) {
    if (px>this.x && px<this.x+this.length && py>this.y && py<this.y+this.length) {
      this.brightness = 255;
    }
  }

  show() {
    stroke(0);
    strokeWeight(4);
    fill(this.brightness, 125);
    square(this.x,this.y,this.length);
  }
}