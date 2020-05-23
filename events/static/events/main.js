
$(window).bind("load", function() {
    // code here


$(document).ready(function () {
    'use strict';



	setTimeout(function () {
		$('#loader').fadeToggle();
	}, 4000);



});

$(document).ready(function(){
    $('.checkbtn').click(function(){
        $('#active').toggleClass('active')
    });
    
    $(window).scroll(function(){
        if ($(document).scrollTop()>300){
            $('nav').addClass('navbg')
        }
        else{
          
                $('nav').removeClass('navbg')
        }

    });

    var typed = new Typed('#typed', {
        strings: [
            "Welcome to University Events Manager"
        ],
        typeSpeed: 80,
        backSpeed: 50,
        loop: false,
        startDelay: 3000,
        onComplete: function() {
            $(".typed-cursor").hide();
        }
    
    });
    
    
    
    var typed2 = new Typed('#typed2', {
        strings: [
            "Easiest way to handle Events",
            "Quick Registration of Events"
        ],
        typeSpeed: 80,
        backSpeed: 30,
        loop: true,
        onComplete: function() {
            $(".typed-cursor").hide();
        }
    
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor =>{
        anchor.addEventListener('click', function(e){
            e.preventDefault();
    
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    
    
    

});


// filter galary
$(document).ready(function(){
(function(){

    'use strict';


    var $projects = $('.projects');

    $projects.isotope({
        itemSelector: '.item',
        layoutMode: 'fitRows'
    });

    $('ul.filters > li').on('click', function(e){

        e.preventDefault();

        var filter = $(this).attr('data-filter');

        $('ul.filters > li').removeClass('active');
        $(this).addClass('active');

        $projects.isotope({filter: filter});

    });

    $('.card').mouseenter(function(){

        $(this).find('.card-overlay').css({'top': '-100%'});
        $(this).find('.card-hover').css({'top':'0'});

    }).mouseleave(function(){

        $(this).find('.card-overlay').css({'top': '0'});
        $(this).find('.card-hover').css({'top':'100%'});

    });

})(jQuery);


});




$(document).ready(function () {
    $("#0").attr({ "src": "static/assets/it.jpg "});
    $("#1").attr({ "src": "static/assets/cse.jpg " });
    $("#2").attr({ "src": "static/assets/mech.jpg " });
    $("#3").attr({ "src": "static/assets/ece.jpg "});
    $("#4").attr({ "src": "static/assets/eee.jpg " });
    $("#5").attr({ "src": "static/assets/civil.jpg " });
});




// form


function validate()
{
  var phoneNumber = document.getElementById('reg').value;
  var phoneRGEX = /^[1][^1-5][0-9]{10} $/;
  var phoneResult = phoneRGEX.test(phoneNumber);
  if(phoneResult==false){
  alert("enter a valid reg no");
  return false;
  }
  else{
      return true;
  }
  

}
});
