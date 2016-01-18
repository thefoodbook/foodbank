$(document).ready(function(){
  var counter = 0;
  $(".buddy").on("swiperight", right);  
  $(".buddy").on("swipeleft", left);
   
    /*$(".buddy").on("click", function(){
      var arr = [1,2,3,4,5,6]
      console.log(arr[1]);
      right();
    });*/
  $(".buddy").on("click", right)
  
  function right() {
    counter++;
      if(counter == 3 || counter ==5 ||counter ==8){
        return left.apply(this);
      }

      $(this).addClass('rotate-left').delay(700).fadeOut(1);
      $(this).find('.status').remove();
      console.log(this);
      $(this).append('<div class="status like">Like!</div>');      
      if ( $(this).is(':last-child') ) {
        $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
       } else {
          $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
       }
  }
  
  function left() {
    $(this).addClass('rotate-right').delay(700).fadeOut(1);
    $(this).find('.status').remove();
    $(this).append('<div class="status dislike">Dislike!</div>');

    if ( $(this).is(':last-child') ) {
     $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
      
     } else {
        $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
    } 
  }


});