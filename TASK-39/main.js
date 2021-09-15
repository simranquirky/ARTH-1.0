
function display_out() {
		var xhr = new XMLHttpRequest();
		xhr.open("GET", "http:///cgi-bin/docker.py?x=" + document.getElementById("cmd").value, "true");
		xhr.send();
		xhr.onload= function()  {
			var a= xhr.responseText;
			var o= document.getElementById("box");
			//selects the html division --> "box"

			
			o.innerHTML=a;





		}

	}
