import React, { Component } from 'react';
import { fetchRecords } from '../../utils/Services.js';
// import { browserHistory } from 'react-router'


import Nurse from './Nurse';
class Nurses extends Component {
	constructor(props) {
		super(props)
		this.state = {
			nurses: [1, 2, 3]
		}
	}
	componentDidMount() {
		fetchRecords()
			.then((res) => {
				this.setState({
					nurses: res.data.records
				})
			})
	}
	render() {
		return (
			<div>
				<h1>Nurse List and information</h1>
				<ul>
					{this.state.nurses.map((nurse, index) => {
						return <Nurse nurse={nurse} key={index} />
					})}
				</ul>
			</div>
		)
	}
}

export default Nurses

/*
TODO: implement browser history to move back
*/