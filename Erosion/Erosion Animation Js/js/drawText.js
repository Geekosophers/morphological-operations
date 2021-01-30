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

        const shapes = font.generateShapes( message, 0.4 );

        const geometry = new THREE.ShapeBufferGeometry( shapes );

        geometry.computeBoundingBox();

        // const xMid = - 0.5 * ( geometry.boundingBox.max.x - geometry.boundingBox.min.x );

        // geometry.translate( xMid, 0, 0 );


        const text = new THREE.Mesh( geometry, matLite );
        text.position.x = xpos;
        text.position.y = ypos;
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