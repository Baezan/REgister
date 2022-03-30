// course.addEventListener('click',function getData(){
//     console.log("Started getData")
//     url = 'http://127.0.0.1:8000/api/course/';
//     fetch(url).then((response)=>{
//         console.log("Inside first then")
//         return response.json();
//     }).then((data)=>{
//         console.log("Inside second then")
//         console.log(data);
//     })
// });
$(document).ready(function () {
    $.getJSON("http://127.0.0.1:8000/api/course/", function (data) {
        var temp = '';
        $.each(data, function (key, value) {
            temp += '<tr>';
            temp += '<th>' + value.courseName + '</th>';
            temp += '<th>' + value.courseFee + '</th>';
            temp += '<th>' + value.courseTeacher + '</th>';
            temp += '</tr>';


        });
        $('#course').append(temp);
    });

});
