//COCO-SSD Variables
let video;
let detector;
let detections = [];

//PoseNet Variables
let poseNet;
let pose;
let skeleton;

function preload() {
  //Load COCO-SSD
  detector = ml5.objectDetector('cocossd');
}

function gotDetections(error, results) {
  if (error) {
    console.error(error);
  }
  detections = results;
  detector.detect(video, gotDetections);
}

function setup() {
  createCanvas(640, 480);
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
  image(video, 0, 0);

  for (let i = 0; i < detections.length; i++) {
    let object = detections[i];
    if (object.label == "person") {
      /*stroke(255, 0, 0);
      strokeWeight(4);
      noFill();
      rect(object.x, object.y, object.width, object.height);
      noStroke();
      fill(255);
      textSize(24);
      text(object.label, object.x + 10, object.y + 24);
      text(Number(object.confidence*100).toFixed(2), object.x + 10, object.y + 48);*/

      /*-----------------------------------------------------------------------------------------------*/
      //PoseNet
      if (pose) {
        let eyeR = pose.rightEye;
        let eyeL = pose.leftEye;
        let d = dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y);
        fill(255, 0, 0);
        //ellipse(pose.nose.x, pose.nose.y, d);
        fill(0, 0, 255);
        ellipse(pose.rightWrist.x, pose.rightWrist.y, 32);
        ellipse(pose.leftWrist.x, pose.leftWrist.y, 32);
    
        for (let i = 0; i < pose.keypoints.length; i++) {
          let x = pose.keypoints[i].position.x;
          let y = pose.keypoints[i].position.y;
          fill(0, 255, 0); 
          let conf = nf(100 * pose.score, 2, 2);                      //numberformat the confidence score 
          text(conf, x, y + 24);                                      //show detected parts confidence
          //text(pose.part, x, y - 24);                               //show detected parts name
          ellipse(x, y, 16, 16);
        }
    
        for (let i = 0; i < skeleton.length; i++) {
          let a = skeleton[i][0];
          let b = skeleton[i][1];
          strokeWeight(2);
          stroke(255);
          line(a.position.x, a.position.y, b.position.x, b.position.y);
        }
      }
      console.log(pose);
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