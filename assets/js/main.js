$(document).ready(function(){
// grab an element
  var myElement = document.querySelector("#header-headroom");
  // construct an instance of Headroom, passing the element
  var headroom  = new Headroom(myElement);
  // initialise
  headroom.init();

  // https://github.com/ghiculescu/jekyll-table-of-contents
  // ...I miss middleman...
  $('#table-of-contents .toc').toc();
})

