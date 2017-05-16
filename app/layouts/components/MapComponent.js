import React, { Component } from 'react';
import { Map } from 'react-d3-map';
import { MarkerGroup } from 'react-d3-map';
import { fetchRecords } from '../../utils/Services.js';

class MapComponent extends Component {
	constructor(props) {
		super(props) 
		this.state = {
			data: null,
		}
		this.popupContent = this.popupContent.bind(this);
	}
	componentDidMount() {
		console.log('MOUNTINGGGG')
		fetchRecords()
		  .then((res) => {
				console.log(res.data, 'IS THE STUFF')
			})
	}
	popupContent(d) { 
		return d.properties.text; 
	}

	render() {
	let data = {
			"type": "Feature",
			"properties": {
				"text": "this is a Point!!!"
			},
			"geometry": {
					"type": "Point",
					"coordinates": [122, 23.5]
			}
	}		
  let width = 800;
  let height = 300;
  let scale = 1200 * 5;
  let scaleExtent = [1 << 12, 1 << 13];
  let center = [-5, 55.4];
	fetchRecords();			
	return (
		<div>
		  <h3>View Nurses Around You</h3>
			<Map
				width= {width}
				height= {height}
				scale= {scale}
				// scaleExtent= {scaleExtent}
				center= {center}
			>
			</Map>
		</div>			
	)
	}
}
export default MapComponent;

/*
	TODO: Add markers for each nurse
*/