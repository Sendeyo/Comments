$(document).ready(function () {
  console.log("js is ready sir");

  var text = "text"

  $(".btn-me").click(function(params) {
    $.ajax({
      url : "",
      type : "get",
      data : {
        text : text
      },
      success : function(response){
        $(".home-something").text(response.text)
      }
    })
  })


  $.ajax({
    url : "",
    type : "get",
    data : {
      text : "comments",
      id : "1387991968282905"
    },
    success : function(response){
      var comments = response.comments[0].data
      // console.log(comments)
      comments.forEach(element => {
        console.log(element.id)
        
      });
      // $(".home-something").text(response.comments)
    }
  })



}); 