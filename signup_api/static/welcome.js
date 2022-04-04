$(document).ready(function () {
    $.getJSON("http://127.0.0.1:8000/api/course/", function (data) {
        var temp = '';
        i = 1;
        $.each(data, function (key, value) {
            temp += '<tr>';
            temp += '<th>' + i + '</th>';
            temp += '<th>' + value.courseName + '</th>';
            temp += '<th>' + value.courseFee + '</th>';
            temp += '<th>' + value.courseTeacher + '</th>';
            temp += '</tr>';
            i++;


        });
        $('#course').append(temp);
    });
    // var csrf_token = $('meta[name="csrf-token"]').attr('content');
   
    // $('#dja').click(function () {
    //     //  var id= $(this).attr('id');
    //     data = {
    //         "csrfmiddlewaretoken": "{{ csrf_token }}",
    //         "courseName":"Django",
    //         "courseFee":"10000",
    //         "courseTeacher":"Ahtisham Sir",
    //         "description":"added the course"

    //     };
    //     $.ajax({
    //         url:"http://127.0.0.1:8000/api/course/" ,
    //         cache: 'false',
    //         dataType: 'json',
    //         type: 'POST',
    //         data: data,
    //         success: function (data) {
    //             console.log(data);
    //         }
    //     });


    // });
});
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
 dja.addEventListener('click', function postData(){

        url ='http://127.0.0.1:8000/api/course/';
        data = '{"courseName":"Django","courseFee":"10000","courseTeacher":"Ahtisham Sir","description":"added the course"}'
        params = {
            method:"POST",
            headers: {
                'Content-Type': 'application/json;odata=verbose',
                'X-CSRFToken': csrftoken
              },
    
            body: data
        }
        fetch(url, params).then(response=> response.json())
        .then((data) => {
        
            console.log(data);
           
        })
        // $.post( url, function( data ) {
        //     console.log(data);
        //   });
    });
    
