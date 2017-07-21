import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col, Table, FormControl } from 'react-bootstrap';
import Head from './Components';


class WorkoutRow extends React.Component {
  render() {
    return (
      <tr>
        <td>{this.props.workout.pk}</td>
		<td>{this.props.workout.fields.name}</td>
        <td>{this.props.workout.fields.start_time}</td>
		<td>{this.props.workout.fields.end_time}</td>
		<td>{this.props.workout.fields.location}</td>
      </tr>
    );
  }
}

class WorkoutTable extends React.Component {
  render() {
    var rows = [];
	this.props.workouts.forEach(function(workout) {
		rows.push(<WorkoutRow workout={workout} key={workout.pk} />);
	});
    return (
		<Col md="8">
			<Table>
				<thead>
					<tr>
						<th>Id</th>
						<th>Workout</th>
						<th>Start</th>
						<th>End</th>
						<th>Location</th>
					</tr>
				</thead>
				<tbody>{rows}</tbody>
			</Table>
		</Col>
    );
  }
}

class Single extends React.Component {
  render() {
    return (
		<div>
			<Head head="Gym Workouts"/>
			<Col md="4">
				<form>
					<FormControl type="text" placeholder="Search..." />
				</form>
			</Col>
		</div>
    );
  }
}

class GymWorkouts extends React.Component {
	getData() {
		var data = fetch('/gym/api/workouts')
		.then(response => response.json())
		.then(json => {
			console.log(json);
			this.setState({data: json});			
		});
		console.log("Data: ", data);
	}
	constructor() {
		super()
		this.state = {data: undefined};
	}
	componentDidMount() {
		this.getData();
	}
	render() {
		var x = undefined;
		if(this.state.data == undefined){
			var x = <p>Waiting...</p>
		}else{
		var x = <WorkoutTable workouts={this.state.data} />
		}
		return (		
		  <div>
			<Single />			
				{x}
		  </div>
		);
	}
}



 
export default GymWorkouts;