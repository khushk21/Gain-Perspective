async function gain_perspective(text) {
	let perspective = await fetch(`http://0.0.0.0:8000/endpoint?text=${text}`, {
		method: 'GET',
	}).catch((err) => {
		document.getElementById('messages').innerHTML = 'Internal Server Error';
		return;
	});
	console.log(perspective);
	return perspective;
}
let button = document.getElementById('button');
button.onclick = () => {
	const data = gain_perspective(document.getElementById('textarea').value);
	if (data == null) return;
	const articles = data['articles'];
	const toxicity = data['toxicity'];
	console.log(articles);
	console.log(toxicity);
	const div = document.getElementById('messages');
	let toxicityReport = `<div>Toxicity Report: ${toxicity}</div>`;
	div.innerHTML = toxicityReport;
};
