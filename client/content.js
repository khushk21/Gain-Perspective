async function gain_perspective(text) {
	let data = await fetch(`http://0.0.0.0:8000/endpoint?text=${text}`, {
		method: 'GET',
	}).catch((err) => {
		document.getElementById('toxicity').innerHTML = err;
		return;
	});
	data = await data.json();
	document.getElementById('toxicity').innerHTML =
		'Toxicity Rating: ' +
		'<b>' +
		data['toxicity'].join(', ') +
		'</b><br/><br/>News Articles: ';
	if (data['articles'].length == 0)
		document.getElementById('toxicity').innerHTML += 'No Articles Found! :(';
	for (var i = 0; i < data['articles'].length; i++) {
		document.getElementById('toxicity').innerHTML +=
			'<br/><br/><div><b>' +
			data['articles'][i]['title'] +
			' (<a href=' +
			data['articles'][i]['url'] +
			'>here</a>)</b></div><br/> <div><img src=' +
			data['articles'][i]['urlToImage'] +
			'></img><div>' +
			data['articles'][i]['description'] +
			'</div></div>';
		if (i == 4) break;
	}
}

let button = document.getElementById('GPbutton');
button.onclick = () => {
	document.getElementById('toxicity').innerHTML = 'Gaining Perspective...';
	gain_perspective(document.getElementById('GPtextarea').value);
};
