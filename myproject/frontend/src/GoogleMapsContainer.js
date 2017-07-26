import React, {Component} from 'react';
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';

import GeoLocation from './GeoLocation';

export class MapContainer extends Component {
		
	state = {
		lat: 0,
		lon: 0
	}
	
	render() {
		return (
				<div className="maps-container">

						<Map 
							className= 'maps'
							google={this.props.google} 
							centerAroundCurrentLocation = {true}
							zoom={8}>
							
							<Marker name={'Current'} />
							
						</Map>
	
			</div>

		);
	}
	
}



export default GoogleApiWrapper({
  apiKey: ('AIzaSyBT0n-dNVqFVv8PhNAAkBxGYLCP4n1QXZU')
})(MapContainer)