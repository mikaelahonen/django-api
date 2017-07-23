import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col, Table, Form, FormControl, FormGroup, ControlLabel } from 'react-bootstrap';
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

			
			<Col md="4">
				<Form>
					<FormGroup>
						<ControlLabel>Id</ControlLabel>
						<FormControl type="text" disabled placeholder="1" />
					</FormGroup>
					<FormGroup>
						<ControlLabel>Workout</ControlLabel>
						<FormControl type="text" placeholder="Full body" />
					</FormGroup>
					<FormGroup>
						<Row>
							<Col sm={12}><ControlLabel>Start time</ControlLabel></Col>
							<Col sm={6}><FormControl type="date"/></Col>
							<Col sm={6}><FormControl type="time"/></Col>
						</Row>
					</FormGroup>
					<FormGroup>
						<Row>
							<Col sm={12}><ControlLabel>End time</ControlLabel></Col>
							<Col sm={6}><FormControl type="date"/></Col>
							<Col sm={6}><FormControl type="time"/></Col>
						</Row>
					</FormGroup>
					<FormGroup>
						<ControlLabel>Location</ControlLabel>
						<FormControl type="text" placeholder="My gym" />
					</FormGroup>
				</Form>
			</Col>

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
			<Head head="Gym Workouts"/>
			<Row>
				<Single />			
				{x}
			</Row>
		  </div>
		);
	}
}



 
export default GymWorkouts;