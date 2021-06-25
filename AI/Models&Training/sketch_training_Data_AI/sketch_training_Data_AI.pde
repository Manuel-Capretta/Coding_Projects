void setup() {
    size(64,64);
}

void draw(){
  
  for(int i = 0; i < 3; i++){
    background(255);
    pushMatrix();
    strokeWeight(4);
    float r = random(8, 24);
    float x = random(r, width-r);
    float y = random(r, height-r);
    stroke(random(100), random(100), random(100));
    translate(x,y);
    if(i == 0){
      circle(0, 0, r*2);
      saveFrame("learning_data/circle####.png");
    } else if(i == 1){
      rectMode(CENTER);
      rotate(random(-0.5, 0.5));
      square(0, 0, r*2);
      saveFrame("learning_data/square####.png");
    } else if(i == 2){
      rotate(random(-0.5, 0.5));
      triangle(0,random(-r+2,-r-2),random(r+2,r-2),random(r+2,r-2),random(-r+2,-r-2),random(r+0.2,r-0.2));
      saveFrame("learning_data/triangle####.png");
    }
    popMatrix();
  }
  
  if(frameCount == 430){
    exit();
  }
}
