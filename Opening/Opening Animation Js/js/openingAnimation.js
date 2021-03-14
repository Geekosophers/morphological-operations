// for showing the frame rate, ram usage
(function(){var script=document.createElement('script');script.onload=function(){var stats=new Stats();document.body.appendChild(stats.dom);requestAnimationFrame(function loop(){stats.update();requestAnimationFrame(loop)});};script.src='//mrdoob.github.io/stats.js/build/stats.min.js';document.head.appendChild(script);})()

var kernelObj = [];
var kernelText = [];
var cubePaddedInputObj = [];
var cubePaddedErodedObj = [];
var playErosion = true;
var playDilation = false;
var playAnimationVar = true;

var drawImage = function(offsetX, offsetY){
    for(y=m+Math.floor(kernelArray.length/2)-1+offsetY;y>=Math.floor(kernelArray.length/2)+offsetY;y--){
        for(x=n+nk+Math.floor(kernelArray.length/2)+offsetX;x<2*n+nk+Math.floor(kernelArray.length/2)+offsetX;x++){
            drawCube(x,y,0,0x292929);
        }
    }
};

var drawPaddedImage = function(paddedArray,offsetX,offsetY,cubeObj){
    for(y=m+2*Math.floor(mk/2)-1+offsetY;y>=0+offsetY;y--){
        var cubeTempObj = [];
        for(x=0+offsetX;x<n+2*Math.floor(nk/2)+offsetX;x++){
            var colorOfCube = 0x292929;
            for(i=0;i<Math.floor(kernelArray.length/2);i++){
                if(x==i+offsetX || y==i+offsetY || x==paddedArray[0].length-(i+1)+offsetX || y==paddedArray.length-(i+1)+offsetY){
                    var colorOfCube = 0x696969;
                }
            }
            
            var cube = drawCube(x,y,0,colorOfCube);
            drawText(x-0.18,y-0.2,0.1,paddedArray[m+2*Math.floor(mk/2)-1-y-offsetY][x-offsetX],false,false);
            cubeTempObj.push(cube);
        }
        cubeObj.push(cubeTempObj);
    }
};

var drawKernel = function(basex,basey){
    for(y=m+1;y>=m-mk+2;y--){
        var kernelTempObj = [];
        for(x=0;x<nk;x++){
            if(kernelArray[m+1-y][x]=='1')
                var colorOfCube = 0xfbdd11;
            else
                colorOfCube = 0x292929;
            var cube = drawCube(x+basex,y+basey,3,colorOfCube);
            var content = drawText(x+basex-0.18,y+basey-0.2,3.1,kernelArray[m+1-y][x],true,x==(nk-1));
            kernelTempObj.push(cube);
        }
        kernelObj.push(kernelTempObj);
    }
};

var colorTheCubeToDefault = function(paddedArray, cubeObj){
    for(y=m+2*Math.floor(mk/2)-1;y>=0;y--){
        for(x=0;x<n+2*Math.floor(nk/2);x++){
            var colorOfCube = 0x292929;
            
            for(i=0;i<Math.floor(kernelArray.length/2);i++){
                if(x==i || y==i || x==paddedArray[0].length-(i+1) || y==paddedArray.length-(i+1)){
                    var colorOfCube = 0x696969;
                }
            }
            cubeObj[m+2*Math.floor(mk/2)-1-y][x].material.color.setHex( colorOfCube);
        }
    }
}

var getPaddedImage = function(paddedArray,inputImageArray){
    for(i=0;i<m+2*Math.floor(mk/2);i++){
        a: for(j=0;j<n+2*Math.floor(nk/2);j++){
            for(k=0;k<Math.floor(kernelArray.length/2);k++){
                if(i==k || j==k || i==paddedArray.length-(k+1) || j==paddedArray[0].length-(k+1)){
                    if(imageType=='Binary')
                        paddedArray[i][j]='1';
                    else
                        paddedArray[i][j]='255';
                    continue a;
                }
            }
            paddedArray[i][j]=inputImageArray[i-(Math.floor(kernelArray.length/2))][j-(Math.floor(kernelArray.length/2))];
        }
    }
}

var updatedPositionx=0;
var updatedPositiony=0;

var updateKernelPosition = function(){
    if(playErosion==true && playAnimationVar==true){
        if(imageType=='Binary'){
            var isUpdatedWithZero = false;
            colorTheCubeToDefault(paddedImageArray, cubePaddedInputObj);
            for(y=paddedImageArray.length-1;y>=paddedImageArray.length-1-mk+1;y--){
                for(x=0;x<nk;x++){
                    if(kernelArray[paddedImageArray.length-1-y][x]=='1'){
                        if(paddedImageArray[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x]=='0'){
                            cubePaddedInputObj[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0xfbdd11 );
                            isUpdatedWithZero = true;
                        }
                        else{
                            cubePaddedInputObj[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x4caf50 );
                        }
                    }
                    else{
                        cubePaddedInputObj[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x3a4f75 );
                    }
                    kernelObj[paddedImageArray.length-1-y][x].position.x=updatedPositionx+x;
                    kernelObj[paddedImageArray.length-1-y][x].position.y=y-updatedPositiony;
                    try{
                        kernelText[paddedImageArray.length-1-y][x].position.x=updatedPositionx+x-0.18;
                        kernelText[paddedImageArray.length-1-y][x].position.y=y-0.2-updatedPositiony;
                    }catch(err){
                        console.log('textHasNotInitialized');
                    }
                }
            }
            if(isUpdatedWithZero==true){
                erodedImageArray[updatedPositiony][updatedPositionx] = '0';
                drawText(updatedPositionx-0.18+n+nk+Math.floor(kernelArray.length/2),m+Math.floor(kernelArray.length/2)-1-updatedPositiony-0.2,0.1,'0',false,false);
            }
            else{
                erodedImageArray[updatedPositiony][updatedPositionx] = '1';
                drawText(updatedPositionx-0.18+n+nk+Math.floor(kernelArray.length/2),m+Math.floor(kernelArray.length/2)-1-updatedPositiony-0.2,0.1,'1',false,false);
            }
            updatedPositionx = (updatedPositionx+1)%(paddedImageArray[0].length-kernelArray[0].length+1);
            updatedPositiony = updatedPositionx==0 ? ((updatedPositiony+1)<(paddedImageArray.length-kernelArray.length+1) ? (updatedPositiony+1): 0): updatedPositiony;
        }
        else if(imageType=='Grayscale'){
            var minValue = 255;
            colorTheCubeToDefault(paddedImageArray, cubePaddedInputObj);
            for(y=paddedImageArray.length-1;y>=paddedImageArray.length-1-mk+1;y--){
                for(x=0;x<nk;x++){
                    if(kernelArray[paddedImageArray.length-1-y][x]=='1'){
                        var pixelValue = parseInt(paddedImageArray[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x]);
                        cubePaddedInputObj[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x4caf50 );
                        minValue = minValue>pixelValue ? pixelValue : minValue ;
                    }
                    else{
                        cubePaddedInputObj[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x3a4f75 );
                    }
                    kernelObj[paddedImageArray.length-1-y][x].position.x=updatedPositionx+x;
                    kernelObj[paddedImageArray.length-1-y][x].position.y=y-updatedPositiony;
                    try{
                        kernelText[paddedImageArray.length-1-y][x].position.x=updatedPositionx+x-0.18;
                        kernelText[paddedImageArray.length-1-y][x].position.y=y-0.2-updatedPositiony;
                    }catch(err){
                        console.log('textHasNotInitialized');
                    }
                }
            }
            minValue = minValue.toString();
            erodedImageArray[updatedPositiony][updatedPositionx] = minValue;
            drawText(updatedPositionx-0.18+n+nk+Math.floor(kernelArray.length/2),m+Math.floor(kernelArray.length/2)-1-updatedPositiony-0.2,0.1,minValue,false,false);
            updatedPositionx = (updatedPositionx+1)%(paddedImageArray[0].length-kernelArray[0].length+1);
            updatedPositiony = updatedPositionx==0 ? ((updatedPositiony+1)<(paddedImageArray.length-kernelArray.length+1) ? (updatedPositiony+1): 0): updatedPositiony;
        }
        if(updatedPositionx==0 && updatedPositiony==0){
            playErosion = false;
            getPaddedImage(paddedErodeArray,erodedImageArray);
            drawPaddedImage(paddedErodeArray,n+nk,0,cubePaddedErodedObj)
            drawImage(n+Math.floor(nk/2)+1,0);
            colorTheCubeToDefault(paddedImageArray, cubePaddedInputObj);
            drawText(updatedPositionx-0.18+n+nk,-1-0.2,0.1,'Eroded Image',false,false);
            // controls.target = new THREE.Vector3((n+nk), m/2, 0);
            playDilation = true;
        }
    }
    else if(playDilation==true && playAnimationVar==true){
        if(imageType=='Binary'){
            var isUpdatedWithOne = false;
            colorTheCubeToDefault(paddedErodeArray, cubePaddedErodedObj);
            for(y=paddedErodeArray.length-1;y>=paddedErodeArray.length-1-mk+1;y--){
                for(x=0;x<nk;x++){
                    if(kernelArray[paddedErodeArray.length-1-y][x]=='1'){
                        if(paddedErodeArray[paddedErodeArray.length-1-y+updatedPositiony][updatedPositionx+x]=='0')
                            cubePaddedErodedObj[paddedErodeArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0xfbdd11 );
                        else{
                            cubePaddedErodedObj[paddedErodeArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x4caf50 );
                            drawText(updatedPositionx-0.18+2*n+nk+Math.floor(kernelArray.length),m+Math.floor(kernelArray.length/2)-1-updatedPositiony-0.2,0.1,'1',false,false);
                            isUpdatedWithOne = true;
                        }
                    }
                    else{
                        cubePaddedErodedObj[paddedErodeArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x3a4f75 );
                    }
                    kernelObj[paddedErodeArray.length-1-y][x].position.x=updatedPositionx+x+n+nk;
                    kernelObj[paddedErodeArray.length-1-y][x].position.y=y-updatedPositiony;
                    try{
                        kernelText[paddedErodeArray.length-1-y][x].position.x=updatedPositionx+x-0.18+n+nk;
                        kernelText[paddedErodeArray.length-1-y][x].position.y=y-0.2-updatedPositiony;
                    }catch(err){
                        console.log('textHasNotInitialized');
                    }
                }
            }
            if(isUpdatedWithOne==false)
                drawText(updatedPositionx-0.18+2*n+nk+Math.floor(kernelArray.length),m+Math.floor(kernelArray.length/2)-1-updatedPositiony-0.2,0.1,'0',false,false);
            updatedPositionx = (updatedPositionx+1)%(paddedErodeArray[0].length-kernelArray[0].length+1);
            updatedPositiony = updatedPositionx==0 ? ((updatedPositiony+1)<(paddedErodeArray.length-kernelArray.length+1) ? (updatedPositiony+1): 0): updatedPositiony;
        }
        else if(imageType=='Grayscale'){
            var maxValue = '0';
            colorTheCubeToDefault(paddedErodeArray, cubePaddedErodedObj);
            for(y=paddedErodeArray.length-1;y>=paddedErodeArray.length-1-mk+1;y--){
                for(x=0;x<nk;x++){
                    if(kernelArray[paddedErodeArray.length-1-y][x]=='1'){
                        var pixelValue = paddedErodeArray[paddedErodeArray.length-1-y+updatedPositiony][updatedPositionx+x];
                        cubePaddedErodedObj[paddedErodeArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x4caf50 );
                        maxValue = maxValue<pixelValue ? pixelValue : maxValue;
                    }
                    else{
                        cubePaddedErodedObj[paddedErodeArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x3a4f75 );
                    }
                    kernelObj[paddedErodeArray.length-1-y][x].position.x=updatedPositionx+x+n+nk;
                    kernelObj[paddedErodeArray.length-1-y][x].position.y=y-updatedPositiony;
                    try{
                        kernelText[paddedErodeArray.length-1-y][x].position.x=updatedPositionx+x-0.18+n+nk;
                        kernelText[paddedErodeArray.length-1-y][x].position.y=y-0.2-updatedPositiony;
                    }catch(err){
                        console.log('textHasNotInitialized');
                    }
                }
            }
            drawText(updatedPositionx-0.18+2*n+nk+Math.floor(kernelArray.length),m+Math.floor(kernelArray.length/2)-1-updatedPositiony-0.2,0.1,maxValue,false,false);
            updatedPositionx = (updatedPositionx+1)%(paddedErodeArray[0].length-kernelArray[0].length+1);
            updatedPositiony = updatedPositionx==0 ? ((updatedPositiony+1)<(paddedErodeArray.length-kernelArray.length+1) ? (updatedPositiony+1): 0): updatedPositiony;
        }
        if(updatedPositionx==0 && updatedPositiony==0){
            playDilation = false;
            drawText(updatedPositionx-0.18+2*n+nk+Math.floor(nk),-1-0.2+Math.floor(nk/2),0.1,'Result Image',false,false);
        }
    }
};


var scene = new THREE.Scene();
scene.background = new THREE.Color( 0x4b5399 );
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight);
document.body.appendChild( renderer.domElement);

window.addEventListener('resize', function(){
    var width = window.innerWidth;
    var height = window.innerHeight;
    renderer.setSize( width, height);
    camera.aspect = width/height;
    camera.updateProjectionMatrix();
});

var m = imageArray.length;
var n = imageArray[0].length;

var mk = kernelArray.length;
var nk = kernelArray[0].length;

var erodedImageArray = new Array(m).fill(0).map(() => new Array(n).fill(0));

var paddedImageArray = new Array(m+2*Math.floor(mk/2)).fill(0).map(() => new Array(n+2*Math.floor(nk/2)).fill(0));
var paddedErodeArray = new Array(m+2*Math.floor(mk/2)).fill(0).map(() => new Array(n+2*Math.floor(nk/2)).fill(0));

getPaddedImage(paddedImageArray,imageArray)

var controls = new THREE.OrbitControls(camera, renderer.domElement);

controls.target = new THREE.Vector3((n+nk), m/2, 0);

drawImage(0,0);
drawPaddedImage(paddedImageArray,0,0,cubePaddedInputObj);

drawKernel(-100,0);
camera.position.set((n+nk),-m/2,10);

// animation logic
var update = function(){
    controls.update();
};

// draw scene
var render = function(){
    renderer.render(scene, camera);
};

// run animation loop {update, render, repeat}
var animationLoop = function(){
    requestAnimationFrame( animationLoop );
    update();
    render();
};

var nextStep = function(){
    playAnimationVar = true;
    updateKernelPosition(); 
    playAnimationVar = false;
    document.getElementById("play-button").innerHTML = "Play";
}

var playAnimation = function(){
    playAnimationVar = !playAnimationVar;
    document.getElementById("play-button").innerHTML = playAnimationVar==true ? "Pause" : "Play";
}

setInterval(updateKernelPosition, 1000);
animationLoop();