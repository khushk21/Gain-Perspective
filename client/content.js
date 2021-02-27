async function gain_perspective(text) {
	let data = await fetch(`http://0.0.0.0:8000/endpoint?text=${text}`, {
		method: 'GET',
	}).catch((err) => {
		document.getElementById('messages').innerHTML = err;
	});
	data = await data.json();
	document.getElementById('messages').innerHTML = data['toxicity'];
}

let button = document.getElementById('GPbutton');
button.onclick = () => {
	document.getElementById('messages').innerHTML = 'Gaining Perspective...';
	gain_perspective(document.getElementById('GPtextarea').value);
};
