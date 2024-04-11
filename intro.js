function msg() {
  // confirm("Are you good?");
  // alert("type here");
//   p=prompt("Ankara'nın plaka numarası nedir?", " ")
//   if(p=="yo")
//   {
//   alert("Doğru")
//   }
//   else
//   {
//   alert("Yanlış")
// }
try{
  var num = prompt("Enter a number (1-2):", "1");
  // You can throw exception of any type
  if (num == "1")
  throw "Some Error Message";
  else
  if (num == "2")
  throw 123;
  else
  throw new Error ("Invalid input");
  } catch( err ) {
  alert(typeof(errMsg) + "\n" + err);
  // instanceof operator checks if err is an Error object
  if (err instanceof Error)
  alert("Error Message: " + err.message);
  }
}

function sum() {
  var num1 = prompt("Enter number 1");
  var num2 = prompt("Enter number 2");
  var sum = parseInt(num1) + parseInt(num2);
  alert("The sum is: "+sum);
}
