function userChoice(choice) {


  // const reqForm   = document.getElementById("requestForm");
  // const offReqDiv = document.getElementById("OffReq");
  // console.log('choice=', choice, 'reqForm?', !!reqForm, 'offReqDiv?', !!offReqDiv);



  // console.log('Hi1', choice)
  if (choice=='offer'){
    document.getElementById("offerForm").style.display = "block";
    document.getElementById("OffReq").style.display = "none";

  }
  else if(choice=='request'){
    // console.log('Hi3', choice)
    document.getElementById("OffReq").style.display = "none";
    document.getElementById("requestForm").style.display = "block";
  }
  else{
    print ("Something went wrong, please try again.")
  }
} 

// function myFunction(){
//   console.log('Im working')

// }