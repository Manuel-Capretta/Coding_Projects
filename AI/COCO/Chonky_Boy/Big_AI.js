//COCO-SSD Variables
let video;
let detector;
let detections = [];

//PoseNet Variables
let poseNet;
let pose;
let skeleton;

//other variables
let counter;
let shift = 500;
let refreshRate = 2; //refresh every […] pictures 

function preload() {
  //Load COCO-SSD
  detector = ml5.objectDetector('cocossd');

  //set counter
  counter = 1;
}

function gotDetections(error, results) {
  if (error) {
    console.error(error);
  }
  detections = results;
  detector.detect(video, gotDetections);
}

function setup() {
  createCanvas(1140, 480);
  video = createCapture(VIDEO);
  video.size(640, 480);
  video.hide();
  detector.detect(video, gotDetections);

  //Load PoseNet
  poseNet = ml5.poseNet(video, modelLoaded);
  poseNet.on('pose', gotPoses);
}

function gotPoses(poses) {
  //console.log(poses);
  if (poses.length > 0) {
    pose = poses[0].pose;
    skeleton = poses[0].skeleton;
  }
}

function modelLoaded() {
  console.log('poseNet ready');
}

function draw() {
  counter++;
  image(video, 0, 0);
  let img; 
  img = loadImage('s_big.png');
 

  for (let i = 0; i < detections.length; i++) {
    let object = detections[i];
    if (object.label == "person") {

      //Show box around detected person
      /*stroke(255, 0, 0);
      strokeWeight(4);
      noFill();
      rect(object.x, object.y, object.width, object.height);*/
      

/*-----------------------------------------------------------------------------------------------*/
      //PoseNet
      if (pose) {
        //Just let the console print out some informations…
        for (let i = 0; i < skeleton.length; i++) {
          for (let j = 0; j < skeleton.length; j++) {
            console.log(skeleton[i][j+1]);                              //Print out informations about detexted part
          }                                                             //if parts should be detected specifically, use: pose.rightWrist (EX.)
        }                                                               //for their position just write pose.rightWrist.x (EX.) or .y)                                                      


        //Ellipse
        for (let i = 0; i < pose.keypoints.length; i++) {
          let x = pose.keypoints[i].position.x;
          let y = pose.keypoints[i].position.y;
          fill(255, 0, 0); 
          let conf = nf(100 * pose.score, 2, 2);                      //numberformat the confidence score 
          text(conf, x, y + 24);                                      //show detected parts confidence
          //text(pose.part, x, y - 24);                               //show detected parts name
          
          ellipse(x, y, 10, 10);                                      //Show a little circle at detected location

          //2nd ellipse
          fill(0, 255, 0);
          ellipse(x+500, y, 10, 10);

          //2nd ellipse delete test
          fill(0, 0, 0);
          if(counter%refreshRate == 0){ //refresh rate                    
            rect(640, 0, shift, 480);
          }
        }
    
    
        for (let i = 0; i < skeleton.length; i++) {
          let a = skeleton[i][0];
          let b = skeleton[i][1];
          strokeWeight(2);
          stroke(255);
          line(a.position.x, a.position.y, b.position.x, b.position.y); //line between detected parts (the ones that weren't shifted)
          line(a.position.x+shift, a.position.y+shift, b.position.x+shift, b.position.y+shift); //line between detected parts (the ones that were shifted)
        }
      }
/*-----------------------------------------------------------------------------------------------*/
    } else {
      stroke(0, 255, 0);
      strokeWeight(4);
      noFill();
      rect(object.x, object.y, object.width, object.height);
      noStroke();
      fill(255);
      textSize(24);
      text(object.label, object.x + 10, object.y + 24);
      text(Number(object.confidence*100).toFixed(2), object.x + 10, object.y + 48);
    }
  }
}