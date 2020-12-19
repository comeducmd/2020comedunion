$(document).ready(function(){
    $("#popOpenBtn1").click(function(event){  //팝업 Open 버튼 클릭 시 

         $("#popup_div1").css({
            "top": (($(window).height()-$("#popup_div1").outerHeight())/2+$(window).scrollTop())+"px",
            "left": (($(window).width()-$("#popup_div1").outerWidth())/2+$(window).scrollLeft())+"px"
         }); 
        
        $("#popup_mask").css("display","block");
        $("#popup_div1").css("display","block");
        $("body").css("overflow","hidden");
    });
    
    $("#popCloseBtn1").click(function(event){
        $("#popup_mask").css("display","none");
        $("#popup_div1").css("display","none");
        $("body").css("overflow","auto");
    });        
}); 