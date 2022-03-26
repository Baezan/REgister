  // $('h1').click(function () {
  //       console.log('you clicked on h1', this);
  //        $('h1').hide();
       
  //   }); 
  var temp=localStorage.getItem('username');
  console.log(temp)
  document.getElementById('user').innerHTML=temp;
  addcourse.addEventListener('click',function getData(){
    console.log("Started getData")
    url = '/static/apiendpoint.json';
    fetch(url).then((response)=>{
        console.log("Inside first then")
        return response.json();
    }).then((data)=>{
        console.log("Inside second then")
        console.log(data);
    })
});

// $.get('/static/apiendpoint.json',function)