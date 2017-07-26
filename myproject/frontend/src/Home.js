import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col, Table } from 'react-bootstrap';
import Head from './Components';
import GoogleMapsContainer from './GoogleMapsContainer';
import GeoLocation from './GeoLocation';
import {getPosition} from './functions';



class Position extends Component{	

	state = {
		lat: 1,
		lon: 2,
		acc: 3
	}	
	

	componentDidMount() {
		
				
	}
	
	render() {
		return(
			<div>
			
				<Table>
					<thead>
						<tr><th>Metric</th><th>Value</th></tr>
					</thead>
					<tbody>					
						<tr><td>Latitude</td><td><GeoLocation coord="lon" /></td></tr>
						<tr><td>Longitude</td><td><GeoLocation coord="lat" /></td></tr>
						<tr><td>Accuracy</td><td><GeoLocation coord="acc" /></td></tr>
					</tbody>
				</Table>				
			</div>
		);		
	}
	
}

class Home extends Component {
	
	render() {
		return (
			<div>
				<Head head="Home"/>
				<Jumbotron>
					<h2>Quantiefied Self App</h2>
					<p><i>Welcome!</i></p>
					<Button bsStyle='primary' bsSize='large'>Home button</Button>
				</Jumbotron>
				<h2>Location</h2>
				<Position/>
				<GoogleMapsContainer/>
			</div>
		);
	}
}

export default Home;