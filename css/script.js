function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function handler() {
	var ssid = document.getElementById('sid').value;
	var save = prompt("Enter save file number", ssid);
	var req = new XMLHttpRequest();
	req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          ready = true;
		  if(this.responseText != "0") {
			  document.getElementById("main").innerHTML = this.responseText;
		  }
        }
    };
	//document.getElementById('sid').value;
	var tring = "handler.py?from=00&to=00&this=000&id=" + save;
	message.open("GET", tring, true);
	message.send();
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
	var fromid = document.getElementById(data).parentNode.id;
	var parid = ev.target.id;
	var ready;
	//ev.target.innerHTML = "";
    //ev.target.appendChild(document.getElementById(data));
	//alert(data);
	var message = new XMLHttpRequest();
	message.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          ready = true;
		  if(this.responseText != "0") {
			  document.getElementById("main").innerHTML = this.responseText;
		  }
        }
    };
	var tring = "../Model/handler.py?";
	var ssid = document.getElementById('sid').value;
	tring += "from=";
	tring += fromid;
	tring += "&to=";
	tring += parid;
	tring += "&this="
	tring += data;
	tring += "&id=";
	tring += ssid;
	message.open("GET", tring, true);
	//message.open("GET", "output3.html", true);
	message.send();
}
