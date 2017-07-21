import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col, Table, FormControl } from 'react-bootstrap';
import Head from './Components';


class WorkoutRow extends React.Component {
  render() {
    return (
      <tr>
        <td>{this.props.workout.fields.name}</td>
        <td>{this.props.workout.fields.location}</td>
      </tr>
    );
  }
}

class WorkoutTable extends React.Component {
  render() {
    var rows = [];
	this.props.workouts.forEach(function(workout) {
		rows.push(<WorkoutRow workout={workout} key={workout.fields.name} />);
	});
    return (
		<Col md="8">
			<Table>
				<thead>
					<tr>
					<th>Name</th>
					<th>Price</th>
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
  render() {
    return (
      <div>
        <Single />
        <WorkoutTable workouts={WORKOUTS} />
      </div>
    );
  }
}


var WORKOUTS = [
  {"model": "gym.workout", "pk": 2, "fields": {"name": "Chest + Bicep", "start_time": null, "end_time": null, "location": "Gym X"}}, 
  {"model": "gym.workout", "pk": 3, "fields": {"name": "Back + Triceps", "start_time": null, "end_time": null, "location": "Gym X"}}
];
 
export default GymWorkouts;