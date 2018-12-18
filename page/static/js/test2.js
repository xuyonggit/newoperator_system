var imgPosX = 0;var imgWidth = 256;function dealSelectFiles(){
                                                            var selectFiles = document.getElementById("selectFiles").files;
                                                            for(var file of selectFiles){console.log(file.webkitRelativePath);
                                                                var reader = new FileReader();reader.readAsDataURL(file);
                                                                reader.onloadend = function(){
                                                                    var img = new Image();
                                                                    img.src = this.result;img.onload = function(){
                                                                        var myCanvas = document.getElementById("myCanvas");
                                                                        var cxt = myCanvas.getContext('2d');
                                                                        cxt.drawImage(img, imgPosX, 0);imgPosX += imgWidth;}}}}
                                                                        
function addUser() {
    var param = $("#urlform").serializeArray();
    $("#conf").attr("onclick", "addUser()");
    $.ajax({
        url: "/page/names/",
        method: "post",
        data: param,
        dataType: "json",
        success: function (data) {
            if (data.state == 0) {
                swal("成功", data.info, "success")
            } else {
                swal("失败", data.info, "error")
            }
        },
        error: function () {
            swal("失败！", "保存失败，请联系管理员", "error")
        }
    })
}