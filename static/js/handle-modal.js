$(document).ready(function() {
    $(".popupBtn").click(function(event) { //팝업 Open 버튼 클릭 시 
        const thisId = this.getAttribute('id');
        console.log(thisId);
        $(`div.popupDiv.popUp-${thisId}`).css({
            "top": (($(window).height() - $(`div.popupDiv.popUp-${thisId}`).outerHeight()) / 2 + $(window).scrollTop()) + "px",
            "left": (($(window).width() - $(`div.popupDiv.popUp-${thisId}`).outerWidth()) / 2 + $(window).scrollLeft()) + "px",
            "display": "block"
        });
        $(".popupMask").css("display", "block");
        $("body").css("overflow", "hidden");
        $(`.popCloseBtn-${thisId}`).css("cursor", "pointer");
        $(`.popCloseBtn-${thisId}`).click(function(event) {
            $(".popupMask").css("display", "none");
            $(`div.popupDiv.popUp-${thisId}`).css("display", "none");
            $("body").css("overflow", "auto");
        });
    });

});