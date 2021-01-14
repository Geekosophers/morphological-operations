const texture = new THREE.TextureLoader().load( 'assets/frame.PNG' );
// create the shape
var geometry = new THREE.BoxGeometry( 0.9, 0.9, 0.1);

const material = new THREE.MeshBasicMaterial( { map: texture } );
var drawCube = function(xpos,ypos,zpos){
    // material, color and image texture
    // var material = new THREE.MeshBasicMaterial( { color: 0xe14e87, wireframe: false } );
    var cube = new THREE.Mesh( geometry, material);
    cube.position.set(xpos,ypos,zpos);
    scene.add(cube);
};

// grey cube color = 0x292929
// padding cube color = 0x696969

var drawCube = function(xpos,ypos,zpos,colorOfCube){
    // material, color and image texture
    var material = new THREE.MeshBasicMaterial( { color: colorOfCube, wireframe: false } );
    var cube = new THREE.Mesh( geometry, material);
    cube.position.set(xpos,ypos,zpos);
    scene.add(cube);
    return cube;
};