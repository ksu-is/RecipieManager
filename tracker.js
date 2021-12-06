var count = 0;




function myFunction() {
  
  /*count += document.getElementById("numCals");
  var display = document.getElementById("container");
  var paragraph = document.createElement("p");
  var node = document.createTextNode("Your calorie count is " + count + ".");
 
  paragraph.appendChild(node);
  display.appendChild(paragraph);*/
  count = count + document.getElementById("numCals")
  document.getElementById("demo").innerHTML = count;
}


function displayBelow()

{

  var x = document.getElementById("mySelect");

  var i = x.selectedIndex;

  document.getElementById("label1").innerHTML = "Food Selected  = " + x.options[i].text;

 

  var x = document.getElementById("mySelect");

  document.getElementById("container").innerHTML = "Calories  = " + x.value;

 

}
