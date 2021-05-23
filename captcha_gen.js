for(let i=0;i<100;i++){
    var svgCaptcha = require('svg-captcha');
    var fs = require('fs');
    class options{
        constructor(size,noise,color,background){
            this.size = size;
            this.noise = noise;
            this.color = color;
            this.background = background;
        }
    }
    const op = new options(1,0,false,"#ffffff");
    var captcha = svgCaptcha.create(op);
    fs.writeFile('svg/'+captcha.text+'.svg', captcha.data, function (err) {
        if (err) return console.log(err);
    });
}
console.log('All Files Written To Disk');

// console.log(captcha);