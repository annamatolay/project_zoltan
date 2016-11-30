/**
 * Created by Matolay Pál
 */

$(document).ready(function () {
    var chapter = $("div").attr("id");

    $(function () {
        $("#text").load("/static/content/"+chapter+".html")
    })
});