let shapeClassifier;
let canvas;
let resultsDiv;
let inputImage;
let clearButton;
let video;

function setup() {
  canvas = createCanvas(400, 400);
  video = createCapture(VIDEO);
  video.size(64, 64);
  let options = {
    inputs: [64, 64, 4],
    task: 'imageClassification'
  };
  shapeClassifier = ml5.neuralNetwork(options);
  const modelDetails = {
    /*model: 'model_cam/model1.json',
    metadata: 'model_cam/model_meta1.json',
    weights: 'model_cam/model.weights1.bin'*/
    model: 'models/1MioModel/model.json',
    metadata: 'models/1MioModel/model_meta.json',
    weights: 'models/1MioModel/model.weights.bin'
  };
  background(255);
  resultsDiv = createDiv('loading model');
  inputImage = createGraphics(64, 64);
  shapeClassifier.load(modelDetails, modelLoaded);
}

function modelLoaded() {
  console.log('model ready!');
  classifyImage();
}

function classifyImage() {
  shapeClassifier.classify(
    {
      image: video
    },
    gotResults
  );
}

function gotResults(err, results) {
  if (err) {
    console.error(err);
    return;
  }
  let label = results[0].label;
  let confidence = nf(100 * results[0].confidence, 2, 0);
  resultsDiv.html(`${label} ${confidence}%`);
  classifyImage();
}

function draw() {
  image(video, 0, 0, width, height);
}