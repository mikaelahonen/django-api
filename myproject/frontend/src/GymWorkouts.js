import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col, Table, Form, FormControl, FormGroup, ControlLabel, InputGroup } from 'react-bootstrap';
import Head from './Components';
import * as Api from './Api';
import FontAwesome from  'react-fontawesome';

class WorkoutRow extends React.Component {
	
	constructor(props){
		super(props);
		this.handleClick = this.handleClick.bind(this);
	}
	
	handleClick() {
		console.log("Clicked item: ", this.props.workout.pk);
	}

	
	render() {
		return (
			<tr onClick={this.handleClick} >
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
		
		if(this.props.workouts == undefined){
			var rows = <FontAwesome name="circle-o-notch" size="3x" spin/>;
		} else {
			var rows = [];
			this.props.workouts.forEach(function(workout) {
			rows.push(<WorkoutRow workout={workout} key={workout.pk}/>);
			});
		}
		
		return (
			<Col md={8}>
				<h2>All workouts</h2>
				<Table hover>
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
	
	handleSubmit(){
		console.log("Submit");
		
	}
	
	render() {
		
	return (			
			<Col md={4}>
				<h2>Current workout</h2>
				<form onSubmit={this.handleSubmit}>
				
					<FormGroup>
						<ControlLabel>Id</ControlLabel>
						<FormControl id="id" type="text" disabled placeholder={1} />
					</FormGroup>
					
					<FormGroup>
						<ControlLabel>Workout</ControlLabel>
						<FormControl id="workout" type="text" placeholder="Full body" />
					</FormGroup>
					
					<FormGroup>
						<InputGroup>
							<ControlLabel>Start time</ControlLabel>
						</InputGroup>
						<InputGroup>
							<FormControl type="datetime-local"/>
							<InputGroup.Button><Button>Now</Button></InputGroup.Button>
						</InputGroup>
					</FormGroup>
					
					<FormGroup>
						<InputGroup>
							<ControlLabel>End time</ControlLabel>
						</InputGroup>
						<InputGroup>
							<FormControl type="datetime-local"/>
							<InputGroup.Button><Button>Now</Button></InputGroup.Button>
						</InputGroup>
					</FormGroup>
					
					<FormGroup>
						<ControlLabel>Location</ControlLabel>
						<FormControl type="text" placeholder="My gym" />
					</FormGroup>
					
					<Button type="submit">
						Submit
					</Button>
				</form>
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
		this.state = {
			data: undefined
		};
	}
	componentDidMount() {
		this.getData();
	}
	render() {
		
		return (			
		  <div>
			<Head head="Gym Workouts"/>
			<Row>
				<Single />			
				<WorkoutTable workouts={this.state.data}/>
			</Row>
		  </div>
		);
	}
}



 
export default GymWorkouts;