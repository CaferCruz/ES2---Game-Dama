function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function handler() {
	
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
	var fromid = document.getElementById(data).parentNode.id;
	var parid = ev.target.parentNode.id;
	var ready;
	//ev.target.innerHTML = "";
    //ev.target.appendChild(document.getElementById(data));
	//alert(data);
	var message = new XMLHttpRequest();
	message.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          ready = true;
        }
    };
	var tring = "handler.py?";
	var ssid = getElementById(sid).value;
	tring += "from=";
	tring += fromid;
	tring += "&to=";
	tring += parid;
	tring += "&this="
	tring += data;
	tring += "&id=";
	tring += ssid;
	message.open("GET", tring, true);
	message.send();
}