$(document).ready(function() {
    $(".popupBtn").click(function(event) { //팝업 Open 버튼 클릭 시 
        const thisId = this.getAttribute('id');
        console.log(thisId);
        $(`div.popupDiv.popUp-${thisId}`).css({
            "top": (($(window).height() - $(`div.popupDiv.popUp-${thisId}`).outerHeight()) / 2 + $(window).scrollTop()) + "px",
            "left": (($(window).width() - $(`div.popupDiv.popUp-${thisId}`).outerWidth()) / 2 + $(window).scrollLeft()) + "px",
        });
        $(`div.popupDiv.popUp-${thisId}`).fadeIn()
        $(".popupMask").fadeIn('fast');
        $("body").css("overflow", "hidden");
        $(`.popCloseBtn-${thisId}`).css("cursor", "pointer");
        $(`.popCloseBtn-${thisId}`).click(function(event) {
            $(".popupMask").fadeOut();
            $(`div.popupDiv.popUp-${thisId}`).fadeOut('fast');
            $("body").css("overflow", "auto");
        });
        $(".popupMask").click(function(event) {
            $(".popupMask").fadeOut();
            $(`div.popupDiv.popUp-${thisId}`).fadeOut('fast');
            $("body").css("overflow", "auto");
        });
    });

});