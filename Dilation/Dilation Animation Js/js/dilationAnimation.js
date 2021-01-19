// for showing the frame rate, ram usage
(function(){var script=document.createElement('script');script.onload=function(){var stats=new Stats();document.body.appendChild(stats.dom);requestAnimationFrame(function loop(){stats.update();requestAnimationFrame(loop)});};script.src='//mrdoob.github.io/stats.js/build/stats.min.js';document.head.appendChild(script);})()

var kernelObj = [];
var kernelText = [];
var cubeObj = [];

var drawImage = function(){
    for(y=m+Math.floor(kernelArray.length/2)-1;y>=Math.floor(kernelArray.length/2);y--){
        for(x=n+nk;x<2*n+nk;x++){
            var cube = drawCube(x,y,0,0x292929);
        }
    }
};

var drawPaddedImage = function(){
    for(y=m+2*Math.floor(mk/2)-1;y>=0;y--){
        var cubeTempObj = [];
        for(x=0;x<n+2*Math.floor(nk/2);x++){
            var colorOfCube = 0x292929;
            for(i=0;i<Math.floor(kernelArray.length/2);i++){
                if(x==i || y==i || x==paddedImageArray[0].length-(i+1) || y==paddedImageArray.length-(i+1)){
                    var colorOfCube = 0x696969;
                }
            }
            
            var cube = drawCube(x,y,0,colorOfCube);
            drawText(x-0.18,y-0.2,0.1,paddedImageArray[m+2*Math.floor(mk/2)-1-y][x],false,false);
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

var colorTheCubeToDefault = function(){
    for(y=m+2*Math.floor(mk/2)-1;y>=0;y--){
        for(x=0;x<n+2*Math.floor(nk/2);x++){
            var colorOfCube = 0x292929;
            
            for(i=0;i<Math.floor(kernelArray.length/2);i++){
                if(x==i || y==i || x==paddedImageArray[0].length-(i+1) || y==paddedImageArray.length-(i+1)){
                    var colorOfCube = 0x696969;
                }
            }
            cubeObj[m+2*Math.floor(mk/2)-1-y][x].material.color.setHex( colorOfCube);
        }
    }
}

var updatedPositionx=0;
var updatedPositiony=0;

var updateKernelPosition = function(){
    var isUpdatedWithOne = false;
    colorTheCubeToDefault();
    for(y=paddedImageArray.length-1;y>=paddedImageArray.length-1-mk+1;y--){
        for(x=0;x<nk;x++){
            if(kernelArray[paddedImageArray.length-1-y][x]=='1'){
                if(paddedImageArray[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x]=='0')
                    cubeObj[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0xfbdd11 );
                else{
                    cubeObj[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x4caf50 );
                    drawText(updatedPositionx-0.18+n+nk,m+Math.floor(kernelArray.length/2)-1-updatedPositiony-0.2,0.1,'1',false,false);
                    isUpdatedWithOne = true;
                }
            }
            else{
                cubeObj[paddedImageArray.length-1-y+updatedPositiony][updatedPositionx+x].material.color.setHex( 0x3a4f75 );
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
    if(isUpdatedWithOne==false)
        drawText(updatedPositionx-0.18+n+nk,m+Math.floor(kernelArray.length/2)-1-updatedPositiony-0.2,0.1,'0',false,false);
    updatedPositionx = (updatedPositionx+1)%(paddedImageArray[0].length-kernelArray[0].length+1);
    updatedPositiony = updatedPositionx==0 ? ((updatedPositiony+1)<(paddedImageArray.length-kernelArray.length+1) ? (updatedPositiony+1): 0): updatedPositiony;
};


var scene = new THREE.Scene();
scene.background = new THREE.Color( 0xFFFFFF );
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

var paddedImageArray = new Array(m+2*Math.floor(mk/2)).fill(0).map(() => new Array(n+2*Math.floor(nk/2)).fill(0));

for(i=0;i<m+2*Math.floor(mk/2);i++){
    a: for(j=0;j<n+2*Math.floor(nk/2);j++){
        for(k=0;k<Math.floor(kernelArray.length/2);k++){
            if(i==k || j==k || i==paddedImageArray.length-(k+1) || j==paddedImageArray[0].length-(k+1)){
                paddedImageArray[i][j]='0';
                continue a;
            }
        }
        paddedImageArray[i][j]=imageArray[i-(Math.floor(kernelArray.length/2))][j-(Math.floor(kernelArray.length/2))];
    }
}

var controls = new THREE.OrbitControls(camera, renderer.domElement);

drawImage();
drawPaddedImage();

drawKernel(-100,0);
camera.position.z = 10;

// animation logic
var update = function(){
    
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
setInterval(updateKernelPosition, 1000);
animationLoop();