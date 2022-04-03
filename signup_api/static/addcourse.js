// dja.addEventListener('click', function postData(){
//     url ='http://127.0.0.1:8000/api/course/';
//     data = '{"courseId":"1",courseName":"Django","courseFee":"10000","courseTeacher":"Ahtisham Sir","description":"added the course"}'
//     params = {
//         method:'post',
//         body: data
//     }
//     fetch(url, params).then(response=> response.json())
//     .then((data) => {
    
//         console.log(data);
       
//     })
// });
// dja.addEventListener('click',function getData(){
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