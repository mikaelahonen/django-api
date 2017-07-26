import React, {Component} from 'react';
import ReactDOM from 'react-dom';

export class Map extends Component{
	
	
	componentDidUpdate(prevProps, prevState) {
		if (prevProps.google !== this.props.google) {
			this.loadMap();
		}		
	}
	
	componentDidMount() {		
		this.loadMap();
	}
	
	loadMap(){
		if (this.props && this.props.google) {
			// google is available
			const {google} = this.props;
			const maps = google.maps;
			
			const mapRef ) this.refs.map;
			const node = ReactDOM.findDOMNode(maprRef);
			
			let zoom = 14;
			let lat = 67;
			let lng = 24;
			const center = new maps.LatLng(lat, lng);
			const mapConfig = Object.assign({}, {
				center: center,
				zoom, zoom
			}
			this.map = new maps.Map(node, mapConfig);
		}
	}
	
	render(){
		return(
			<div className="maps-element" ref='map'>
				Loading map...
			</div>
		)
	}
	
}

