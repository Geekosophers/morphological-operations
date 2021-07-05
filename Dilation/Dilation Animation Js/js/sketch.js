let kernelSquares = [];
let imageSquares = [];
let imageType = 'Binary';
let textList = ['',''];

function onchange_action(){
    var kernelValue = document.getElementsByName("mk-nk-value")[0];
    var m = document.getElementsByName("m-value")[0];
    var n = document.getElementsByName("n-value")[0];
    imageType = document.getElementsByName("image-type")[0].value;
    setup(kernelValue.value,m.value,n.value,imageType);
}

function setup(kernelValue,mValue,nValue,imageType) {
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
            for(let j = 2; j< mk+2; j++){
                let b = new Square(i*(length), j*(length), length, i*length+(length/3),j*length+(2*length/3),'0',height/40);
                kernelSquares.push(b);
            }
        }

        for (let i = 1; i < n+1; i++) {
            for(let j = mk+4; j< m+mk+4; j++){
                let char = imageType=='Binary' ? '0' : Math.floor(Math.random()*10).toString();
                let b = new Square(i*(length), j*(length), length, i*length+(length/3),j*length+(2*length/3),char,height/40);
                imageSquares.push(b);
            }
        }

        let kernelHeading = new Heading(length,length,'Kernel Matrix',height/40);
        textList[0] = kernelHeading;

        let imageHeading = new Heading(length,length*(mk+3),'Image Matrix',height/40);
        textList[1] = imageHeading;

    }
    else{

        for (let i = 1; i < nk+1; i++) {
            for(let j = 2; j< mk+2; j++){
                let b = new Square(i*(length), j*(length), length, i*length+(length/3),j*length+(2*length/3),'0',width/40);
                kernelSquares.push(b);
            }
        }
    
        for (let i = nk+2; i < nk+2+n; i++) {
            for(let j = 2; j< m+2; j++){
                let char = imageType=='Binary' ? '0' : Math.floor(Math.random()*10).toString();
                let b = new Square(i*(length), j*(length), length, i*length+(length/3),j*length+(2*length/3),char,width/40);
                imageSquares.push(b);
            }
        }

        let kernelHeading = new Heading(length,length,'Kernel Matrix',width/40);
        textList[0] = kernelHeading;

        let imageHeading = new Heading(length*(nk+2),length,'Image Matrix',width/40);
        textList[1] = imageHeading;

    }
}

function isSafari() {
    var is_safari = navigator.userAgent.toLowerCase().indexOf('safari/') > -1;
    return is_safari;
}

const isTouchDevice =  function() {
    const is_or_not =  ('ontouchstart' in window        // works on most browsers 
        || navigator.maxTouchPoints)                    // works on IE10/11 and Surface;       
        && !isSafari();

    console.log('is_or_not',is_or_not)
    return is_or_not ? true : false; // Fix to always return true or false
};

function mousePressed() {
    if( isTouchDevice() )
        return;

    mousePressX = mouseX;
    mousePressY = mouseY;
}

function mouseReleased(e) {
    if( isTouchDevice() )
        return;

    if(mousePressX == mouseX && mousePressY == mouseY)
        singleTap();

}

function mouseClicked() {
    if( !isTouchDevice() )
        return;

    singleTap();
}

function singleTap() {

    for (let i = 0; i < kernelSquares.length; i++) {
        kernelSquares[i].clicked(mouseX, mouseY);
    }
    if(imageType=='Binary'){
        for (let i = 0; i < imageSquares.length; i++) {
            imageSquares[i].clicked(mouseX, mouseY);
        }
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
    textList[0].show();
    textList[1].show();
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

class Heading {
    constructor(textx, texty, textValue, textSize) {
        this.textx = textx;
        this.texty = texty;
        this.textValue = textValue;
        this.textSize = textSize;
    }

    show() {
        strokeWeight(2);
        textSize(this.textSize);
        fill('white');
        text(this.textValue,this.textx,this.texty);
    }
}