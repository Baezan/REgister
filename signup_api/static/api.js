// getapi.addEventListener('click',function getData()  { 
//     url = 'http://127.0.0.1:8000/api/getcourses';
//     fetch(url).then((response)=>{
//         return response.json();
//     }).then((data)=>{
//         console.log(data);
//         var j=1;
//         for(var i=0;i<data.length;i++){
//             document.getElementById(j).innerHTML+=
//             data[i].courseName+"<br/>"+"Course Fee = "+data[i].courseFee+"<br/>"+"Teacher = "+ data[i].courseTeacher+"</br>"
//             j++;
//         }

//     })
  
// });
function getData()  { 
        url = 'http://127.0.0.1:8000/api/getcourses';
        fetch(url).then((response)=>{
            return response.json();
        }).then((data)=>{
            console.log(data);
            var j=1;
            for(var i=0;i<data.length;i++){
                document.getElementById(j).innerHTML+=
                "Course Fee = "+data[i].courseFee+"<br/>"+"Teacher = "+ data[i].courseTeacher+"</br>"
                j++;
            }
    
        })
      
    };

window.onload=getData();

