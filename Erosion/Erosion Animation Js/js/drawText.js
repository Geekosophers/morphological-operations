var kernelTextTemp = []

var drawText = function(xpos,ypos,zpos,textName,isKernel,pushToArray){
    const loader = new THREE.FontLoader();
    
    
    const text = '';
    
    loader.load( 'fonts/helvetiker_regular.typeface.json', function ( font ) {

        const color = 0xFFFFFF;

        const matDark = new THREE.LineBasicMaterial( {
            color: color,
            side: THREE.DoubleSide
        } );

        const matLite = new THREE.MeshBasicMaterial( {
            color: color,
            transparent: true,
            opacity: 1,
            side: THREE.DoubleSide
        } );

        const message = textName;
        let shapes = ''
        let xoffset = 0;
        let yoffset = 0;

        if(message==='255'){
            shapes = font.generateShapes( message, 0.3 );
            xoffset = 0.15;
            yoffset = 0.1;
        }
        else
        shapes = font.generateShapes( message, 0.4 );

        const geometry = new THREE.ShapeBufferGeometry( shapes );
        geometry.computeBoundingBox();

        const text = new THREE.Mesh( geometry, matLite );
        
        
        text.position.x = xpos-xoffset;
        text.position.y = ypos+yoffset;
        text.position.z = zpos;
        scene.add( text );
        
        if(isKernel==true)
            kernelTextTemp.push(text);
        
        if(isKernel && pushToArray){
            kernelText.push(kernelTextTemp)
            kernelTextTemp = []
        }
            
        
    } ); //end load function
    // console.log(text);
};