let kernelSquares = [];
let imageSquares = [];

function onchange_action(){
    var kernelValue = document.getElementsByName("mk-nk-value")[0];
    var m = document.getElementsByName("m-value")[0];
    var n = document.getElementsByName("n-value")[0];
    setup(kernelValue.value,m.value,n.value);
}

function setup(kernelValue,mValue,nValue) {
    kernelSquares = [];
    imageSquares = [];
    let width = window.innerWidth;
    let height = window.innerHeight;
    createCanvas(width, height);
    let length = width/20;

    let m = parseInt(mValue);
    let n = parseInt(nValue);
    let mk = parseInt(kernelValue);
    let nk = parseInt(kernelValue);

    if(height>width){
        length = height/20;  
        
        for (let i = 1; i < nk+1; i++) {
            for(let j = 1; j< mk+1; j++){
                let b = new Square(i*(length), j*(length), length, i*length+(length/3),j*length+(2*length/3),'0',height/40);
                kernelSquares.push(b);
            }
        }

        for (let i = 1; i < n+1; i++) {
            for(let j = mk+2; j< m+mk+2; j++){
                let b = new Square(i*(length), j*(length), length, i*length+(length/3),j*length+(2*length/3),'0',height/40);
                imageSquares.push(b);
            }
        }
        
    }
    else{
        for (let i = 1; i < nk+1; i++) {
            for(let j = 1; j< mk+1; j++){
                let b = new Square(i*(length), j*(length), length, i*length+(length/3),j*length+(2*length/3),'0',width/40);
                kernelSquares.push(b);
            }
        }
    
        for (let i = nk+2; i < nk+2+n; i++) {
            for(let j = 1; j< m+1; j++){
                let b = new Square(i*(length), j*(length), length, i*length+(length/3),j*length+(2*length/3),'0',width/40);
                imageSquares.push(b);
            }
        }
    }
}

function mousePressed() {
    for (let i = 0; i < kernelSquares.length; i++) {
        kernelSquares[i].clicked(mouseX, mouseY);
    }
    for (let i = 0; i < imageSquares.length; i++) {
        imageSquares[i].clicked(mouseX, mouseY);
    }
}

function draw() {
    background('#4b5399');
    for (let i = 0; i < kernelSquares.length; i++) {
        kernelSquares[i].show();
    }
    for (let i = 0; i < imageSquares.length; i++) {
        imageSquares[i].show();
    }
}

class Square {
    constructor(x, y, length, textx, texty, textValue, textSize) {
        this.x = x;
        this.y = y;
        this.length = length;
        this.textx = textx;
        this.texty = texty;
        this.textValue = textValue;
        this.textSize = textSize;
        this.brightness = 0;
    }

    clicked(px, py) {
        if (px>this.x && px<this.x+this.length && py>this.y && py<this.y+this.length) {
            this.brightness = this.brightness!=255 ? 255 : 0;
            this.textValue = this.textValue=='0' ? '1' : '0';
        }
    }

    show() {
        stroke(0);
        strokeWeight(2);
        fill(this.brightness, 125);
        square(this.x,this.y,this.length);
        textSize(this.textSize);
        strokeWeight(1);
        fill(0);
        text(this.textValue,this.textx,this.texty);
    }
}