
function needAttention(){
    console.log(document.getElementById('needattention').value);
    if (document.getElementById('needattention').value == 0){
        document.getElementById('needattention').value = 1;
        alert("Head Nurse is Being Contacted");
    }
    else {
        document.getElementById('needattention').value = 0;
        alert("Head Nurse is no longer coming");
    }
}

function contactFamily(){
    if (document.getElementById('familycall').value == 0){
        document.getElementById('familycall').value = 1;
        alert("Your Family is Being Contacted");
    }
    else {
        document.getElementById('familycall').value = 0;
        alert("Your Family is no longer being contacted");
    }
}

function livestream_video(){
    var test = document.getElementsByClassName('livestream');
    test.innerHTML = '<iframe width="560" height="315" src="https://www.youtube.com/embed/2IrEJougork" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
}   



