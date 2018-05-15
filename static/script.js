$(document).on("click", ".dropdown-menu li", function(){
  $.ajax({
    type: "GET",
    url: "/language/" + $(this).text(),
    success: function(data) {
      alert(data);
    },
  });
});

var clicked = false;
$(document).on("click", "#start", function(){
  alert("clicked");
  if (!clicked) {
    clicked = true
    evtSrc.close();
    evtSrc = new EventSource("/chatData/False");
  }
  else {
    evtSrc.close();
    evtSrc = new EventSource("/chatData/True");
    clicked = false
  }
  // $.ajax({
  //   type: "GET",
  //   url: "/language/" + $(this).text(),
  //   success: function(data) {
  //     alert(data);
  //   },
  // });
});

var evtSrc = new EventSource("/chatData/True");

evtSrc.onmessage = function(e) {
  var previousText = $(".chatText").html();
  $(".chatText").html(previousText + "<br>" + e.data);
}
