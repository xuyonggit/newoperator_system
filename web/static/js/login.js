$(function () {
    $('#button,#Retrievenow,#denglou').css('opacity', 0.7).hover(function () {
        $(this).stop().fadeTo(650, 1);
    }, function () {
        $(this).stop().fadeTo(650, 0.7);
    });
    
    if ($.cookie("codeusername") != null) {
        // $("#username").val($.cookie("codeusername"));
        // $("#password").val($.cookie("codeppsd"));
        $.ajax({
            type: "POST",
            url: '/user/checkis/',
            data: { typex: 1 },
            async: false,
            success: function (data) {///去更新cookies
                if (data == "NotLogin") {
                    ///沒有登錄
                    getLogStatx(2); //没有记录cookies 的登录状态
                } else {
                    window.location.href = "/page/index";
                }
            }
        });
    }
    $("#button").click(function () {
        var username = $("#username").val();
        var userpwd = $("#userpwd").val();
        if (username.length > 0 && userpwd.length > 0) {
            getLogStatx(1);
        }
    });

    //// 用户注册


    ////忘记密码
    $("#iforget").click(function () {
        $("#login_model").hide();
        $("#forget_model").show();

    });

    ///取回密码 
    $("#Retrievenow").click(function () {
        var usrmail = $("#usrmail").val();
        if (!Test_email(usrmail)) {
           // alert(msgggg.pssjs1);
            return false;
        }
        $("#sending").show();
        $.ajax({
            type: "POST",
            url: '/user/checkis/',
            data: { typex: 5, usermail: usrmail },
            dataType:"json",
            success: function (data) {//
                if (data.state == 0) {
                    swal("邮件已发送", data.info, "success");
                    $("#sending").hide();
                    $("#login_model").show();
                    $("#forget_model").hide();
                    $("#username").val("");
                    $("#userpwd").val("");
                } else {
                    swal("邮件发送失败", data.info, "error");
                    $("#usrmail").val("");
                }
            }
        });


    });
    //返回
    $("#denglou").click(function () {
        $("#usrmail").val("");
        $("#username").val("");
        $("#userpwd").val("");
        $("#login_model").show();
        $("#forget_model").hide();

    });


    //typexx 自动 还是手动
    function getLogStatx(typex) {
        var current = (location.href);
        var screenwidth = $(window).width();
        var screenheight = $(window).height();
        var username = $("#username").val();
        var userpwd = $("#userpwd").val();
        var issavecookies = "NO";
        if ($("#save_me")[0].checked == true) {
            issavecookies = "Yes";
        }
        else {
            issavecookies = "NO";issavecookies
        }
        var l_dot = screenwidth + "*" + screenheight;
        if (typex == "2") {
            if (username == null && userpwd == null) {
                ////保存了cook
                username = $.cookie('codeusername');
                userpwd = $.cookie('codeppsd');
                $.ajax({
                    type: "POST",
                    url: '/user/login/',
                    data: { username: username, userpwd: userpwd, issavecookies: issavecookies, l_dot: l_dot, typex: 2 },
                    dataType:"json",
                    success: function (data) {///去更新cookies
                        if (current.indexOf("index.aspx") > -1) {
                        } else {
                            if (data == "0" || data == "1") {
                                $.cookie('sessionId', data.sessionId, {path: '/'});
                                window.location.href = "/page/index";
                            } else {
                                ot5alert(data, "1");
                            }
                        }
                    }
                });


            }
        } else if (typex == "1") {
            ///// 手動 登錄
            $.ajax({
                type: "POST",
                url: '/user/login/',
                data: { username: username, userpwd: userpwd, issavecookies: issavecookies, l_dot: l_dot, typex: 1 },
                dataType:"json",
                success: function (data) {///去更新cookies
                    if (data.state == "0" || data.state == "1" && issavecookies == "Yes") {
                        $.cookie('sessionId', data.sessionId, {path: '/'});
                        $.cookie('codeusername', username);
                        $.cookie('codeppsd', userpwd);
                        window.location.href = "/page/index";
                    } else {
                        swal('登录失败', data.info, 'error');
                    }
                }
            });
        }
    }


});
//Email 规则以后重新整理所有网站关于js 验证
function Test_email(strEmail) { var myReg = /^[-a-z0-9\._]+@([-a-z0-9\-]+\.)+[a-z0-9]{2,3}$/i; if (myReg.test(strEmail)) return true; return false; }
