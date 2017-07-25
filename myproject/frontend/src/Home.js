import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col, Table } from 'react-bootstrap';
import Head from './Components';
import {withGoogleMap, GoogleMap} from 'react-google-maps';


const MapsWrapper = withGoogleMap(props => (
	 <GoogleMap defaultZoom={7} defaultCenter={{ lat: 61.924, lng: 25.748 }}>
		
	</GoogleMap>
		
));

class Map extends Component{
	
	
	constructor() {
		super();
		this.state = {
			lat: undefined,
			lon: undefined,
			acc: undefined,
			imgUrl: undefined
		};
		
		
	}
	
	setGeoLocation() {
		if (navigator.geolocation){
			console.log("Broswer supports geo location");
			navigator.geolocation.getCurrentPosition(function(location) {
				this.setState({
					lat: location.coords.latitude.toFixed(3),
					lon: location.coords.longitude.toFixed(3),
					acc: (location.coords.accuracy/1000).toFixed(0)
				});
			}.bind(this));			
		 }		 
	}
	

	componentWillMount() {
		this.setGeoLocation();		
	}
	
	render() {
		return(
			<div>
			
				<Table>
					<thead>
						<tr><th>Metric</th><th>Value</th></tr>
					</thead>
					<tbody>					
						<tr><td>Latitude</td><td>{this.state.lat}</td></tr>
						<tr><td>Longitude</td><td>{this.state.lon}</td></tr>
						<tr><td>Accuracy</td><td>{this.state.acc} km</td></tr>
					</tbody>
				</Table>				
				<MapsWrapper containerElement={<div className="maps-container"/>} mapElement={<div className="maps-element" />} />
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
			<Map/>
		</div>
	);
  }
}

export default Home;