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
function openuser() {
    $.ajax({
        url: "/user/get_userinfo/",
        method: "post",
        dataType: "json",
        success: function (data) {
            $("#usernamels").val(data.username);
            $("#email_addressls").val(data.email_address);
            $("#positionls").val(data.position);
            $("#agels").val(data.age);
            if ( data.sex == 1 ) {
                $("#sexls").val("男");
            }else if ( data.sex == 2 ) {
                $("#sexls").val("女");
            }else {
                $("#sexls").val("保密");
            }

        }

    })
}
function makeUser() {
    var param_2 = $("#makefrom").serializeArray();
    $.ajax({
        url: "/user/update_userinfo/",
        method: "post",
        data: param_2,
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

