function setTime(){
  var d = new Date()
  var hours = d.getHours() //get hours in 24 hr format
  var minutes = d.getMinutes()//get minutes
  var part = "NA"
  if(hours > 11){ //get AM or PM
    part = "PM"
  }
  else{
    part = "AM"
  }
  hours = hours % 12 //convert to 12 hour format
  if(hours < 10){
    hours = "0" + hours
  }
  if(hours == "00") {
    hours = 12
  }
  if(minutes < 10){
    minutes = "0" + minutes
  }
  $('.time-hours')[0].innerText = hours
  $('.time-minutes')[0].innerText = minutes
  $('.part')[0].innerText = part
}
// set date
function setDate(){
  var d = new Date()
  var day = d.getDay()
  var daylist = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
  var months = ['January','February','March','April','May','June','July','August','September','October','November','December']
  $('.day')[0].innerHTML = daylist[day] + ", "
  $('.month')[0].innerHTML = months[d.getMonth()] + " "
  $('.date')[0].innerHTML = d.getDate()
}

setTime()
setDate()
setInterval(setTime, 60000)
