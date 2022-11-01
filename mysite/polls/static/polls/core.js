$(function(){
    // console.log("FUNCTIONAL");
    $('body').fadeIn();
    $('.fade-out').click(function(){
        // console.log($(this).attr('id'));
        url = $(this).attr('id');
        // $(this).toggleClass("fade-out");
        $(this).animate({
            left: "-40%",
            opacity:0
        }, function(){
            window.location = url;
        });
        
       
        
    });
});