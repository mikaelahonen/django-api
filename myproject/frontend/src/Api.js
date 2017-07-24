export function getData(){
		var data = fetch('/gym/api/workouts')
		.then(response => response.json()
		)
		.then(json => {
			console.log("Api.getData() json: ", json);
			return json;
		});		
		return data;
}
