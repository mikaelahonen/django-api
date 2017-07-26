import React, {Component} from 'react';
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';

import GeoLocation from './GeoLocation';

export class MapContainer extends Component {
		
	state = {
		lat: 0,
		lon: 0
	}
	
	componentDidMount(){
		var geoSuccess = function(pos){
		console.log("Geolocation success in Google Maps Container");
			this.setState({
				lat: pos.coords.latitude,
				lon: pos.coords.longitude,
				acc: pos.coords.accuracy
			});
		}.bind(this);
		navigator.geolocation.getCurrentPosition(geoSuccess);
	}
	
	
	render() {
		console.log("Lat: ", this.state.lat)
		return (
				
				<div className="maps-container">
						<Map 
							className= 'maps'
							google={this.props.google} 
							centerAroundCurrentLocation = {true}
							zoom={8}>
							
							
							<Marker
								title = {'You are here'}
								name= {'Current location'}
							/>
							
						</Map>
	
			</div>

		);
	}
	
}



export default GoogleApiWrapper({
  apiKey: ('AIzaSyBT0n-dNVqFVv8PhNAAkBxGYLCP4n1QXZU')
})(MapContainer)