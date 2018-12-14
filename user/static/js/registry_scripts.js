
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("/static/pic/registry_bg1.jpg");
    
    /*
	    Modals
	*/
	$('.launch-modal').on('click', function(e){
		e.preventDefault();
		$( '#' + $(this).data('modal-id') ).modal();
		var check = 0;
	});
    
    /*
        Form validation
    */
    $('.registration-form input[type="text"], .registration-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    var username = "";
    var passwd = "";
    var code = "";
    var email = "";
    var position = "";
    $('.registration-form').on('submit', function(e) {
    	// $(this).find('input[type="text"], textarea').each(function(){
    	// 	if( $(this).val() == "" ) {
    	// 		e.preventDefault();
    	// 		if ($(this).attr("name") != "form-position") {
         //            $(this).addClass('input-error');
         //        }
    	// 	}
    	// 	else {
    	// 		$(this).removeClass('input-error');
    	// 	}
    	// });
        e.preventDefault();
        $(this).find('input[name="form-username"], textarea').each(function () {
            if( $(this).val() == "" ) {
                $(this).addClass('input-error');
            }
            else{
                username = $(this).val();
                $(this).removeClass('input-error');
            }
        });
        $(this).find('input[name="form-password"], textarea').each(function () {
            if( $(this).val() == "" ) {
                $(this).addClass('input-error');
            }
            else{
                passwd = $(this).val();
                $(this).removeClass('input-error');
            }
        });
        $(this).find('input[name="form-code"], textarea').each(function () {
            if( $(this).val() == "" ) {
                $(this).addClass('input-error');
            }
            else{
                code = $(this).val();
                $(this).removeClass('input-error');
            }
        });
        $(this).find('input[name="form-email"], textarea').each(function () {
            if( $(this).val() == "" ) {
                $(this).addClass('input-error');
            }
            else{
                email = $(this).val();
                $(this).removeClass('input-error');
            }
        });
        if( username != "" && passwd != "" && code != "" && email != "" ) {
            createUser();
        }
        // createUser(username, passwd, code, email, position)
    	// if (check )
        // console.log(1);
    });
    $("#form-username").click(function() {
        $(this).blur(function () {
            if($(this).val() == "") {
                $(this).addClass("input-error");
            }
        })
    });
    function createUser() {
        var formData = $('#registration-form').serialize();
        $.ajax({
            type: 'POST',
            url: '/user/create_user/',
            cache: false,
            data: formData,
            dataType:'json',
        }).success(function (data) {
            if( data.state == 0 ){
                swal("成功", data.info, "success");
            } else {
                swal("失败", data.info, "error");
            }
        })
    }
});
