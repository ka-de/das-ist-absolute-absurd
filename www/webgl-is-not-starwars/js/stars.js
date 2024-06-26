// stars.js

// Get canvas element by its ID
var field = document.getElementById("field");

// Make sure field canvas exists
var f = (typeof field.getContext === 'function') ? field.getContext("2d") : null;

// Config
var stars = {};
var starIndex = 0;
var numStars = 0;
var acceleration = 1;
var starsToDraw = (field.width * field.height) / 200;

function Star() {
    this.X = field.width / 2;
    this.Y = field.height / 2;

    this.SX = Math.random() * 10 - 5;
    this.SY = Math.random() * 10 - 5;

    var start = 0;

    if (field.width > field.height)
        start = field.width;
    else
        start = field.height;

    this.X += this.SX * start / 10;
    this.Y += this.SY * start / 10;

    this.W = 1;
    this.H = 1;

    this.age = 0;
    this.dies = 500;

    starIndex++;
    stars[starIndex] = this;

    this.ID = starIndex;
    this.C = "#ffffff";
}

Star.prototype.Draw = function () {
    if (!f) {
        console.log('Could not load canvas element');
        return;
    }
    this.X += this.SX;
    this.Y += this.SY

    this.SX += this.SX / (50 / acceleration);
    this.SY += this.SY / (50 / acceleration);

    this.age++;

    if (this.age == Math.floor(50 / acceleration) | this.age == Math.floor(150 / acceleration) | this.age == Math.floor(300 / acceleration)) {
        this.W++;
        this.H++;
    }

    if (this.X + this.W < 0 | this.X > field.width |
        this.Y + this.H < 0 | this.Y > field.height) {
        delete stars[this.ID];
        numStars--;
    }

    f.fillStyle = this.C;
    f.fillRect(this.X, this.Y, this.W, this.H);
}

field.width = window.innerWidth;
field.height = window.innerHeight;

function draw() {
    if (!f) {
        console.log('Could not load canvas element');
        return;
    }

    if (field.width != window.innerWidth)
        field.width = window.innerWidth;
    if (field.height != window.innerHeight)
        field.height = window.innerHeight;

    // The alpha value can be adjusted to create a stream effect
    f.fillStyle = "rgba(0, 0, 0, 0.6)";

    f.fillRect(0, 0, field.width, field.height);

    for (var i = numStars; i < starsToDraw; i++) {
        new Star();
        numStars++;
    }

    for (var star in stars) {
        stars[star].Draw();
    }
}

// Modify interval to adjust speed
if (f) setInterval(draw, 30);
