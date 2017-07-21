import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col } from 'react-bootstrap';
import Head from './Components';

class GymHome extends Component {
  render() {
    return (
		<div>
			<Head head="GymHome"/>
			<Jumbotron>
				<h2>Gym App</h2>
				<p><i>Welcome!</i></p>
			</Jumbotron>
			<Row>
				<Col sm="4">
					<h3>Results</h3>
					<i className="fa fa-3x fa-area-chart"></i>
				</Col>
				<Col sm="4">
					<h3>Box 2</h3>
				</Col>
				<Col sm="4">
					<h3>Box 3</h3>
				</Col>
			</Row>
		</div>
	);
  }
}

export default GymHome;