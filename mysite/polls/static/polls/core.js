$(function(){
    // console.log("FUNCTIONAL");
    $('.fade-out').click(function(){
        // console.log($(this).attr('id'));
        url = $(this).attr('id');
        // $(this).toggleClass("fade-out");
        $(this).animate({
            "left": "-40%",
            opacity:0
        }, function(){
            window.location = url;
        });
    });
    $('.fade-down').click(function(){
        // console.log($(this).attr('id'));
        url = $(this).attr('id');
        // $(this).toggleClass("fade-out");
        $(this).animate({
            "top": "+=50px",
            opacity:0
        }, function(){
            // window.location = url;
        });
    });
});