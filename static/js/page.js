/**
 * Created by Matolay Pál
 */

$(document).ready(function () {
   $("a.page").click(function () {
       var href_val = $(this).attr("href").split("/");
       var page = href_val[1];
       alert(page);
   });
});