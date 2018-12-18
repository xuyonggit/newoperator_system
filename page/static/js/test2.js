var imgPosX = 0;
var imgWidth = 256;
function dealSelectFiles(){
    var selectFiles = document.getElementById("selectFiles").files;
    for(var file of selectFiles){
        // console.log(file.webkitRelativePath);
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function(){
            var img = new Image();
            img.src = this.result;img.onload = function(){
                var myCanvas = document.getElementById("myCanvas");
                var cxt = myCanvas.getContext('2d');
                cxt.drawImage(img, imgPosX, 0);
                imgPosX += imgWidth;
            }
        }
    }
}
