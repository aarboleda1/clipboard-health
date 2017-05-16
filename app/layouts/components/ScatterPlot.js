import React, {Component} from 'react';
import LineChart from 'react-d3-components/lib/LineChart';
import { fetchRecords } from '../../utils/Services.js';

let defaultData = [
    {
    label: 'Years Worked',
    values: [{x: 0, y: 2}, {x: 1.3, y: 5}, {x: 3, y: 6}, {x: 3.5, y: 6.5}, {x: 4, y: 6}, {x: 4.5, y: 6}, {x: 5, y: 7}, {x: 5.5, y: 8}]
    },
];
class ScatterPlot extends Component {
	constructor(props) {
		super(props)
		this.state = {
			nurses: defaultData
		}

	}
	componentDidMount() {
		fetchRecords()
			.then((res) => {
				let data = res.data.records.map((record) => {
					const experience = !record.experience ? 5 : record.experience;
					const salary = salary > 200 ? 30 : record.salary;
					return { x: experience, y: salary }
				})
				this.setState({
					nurses: [
						{
							label: 'Years Worked',
							values: data
						}
					]
				})
			})		
	}
	render() {
		return (
			<div id="line-chart-wrapper">
			<LineChart
				data={this.state.nurses}
				width={400}
				height={400}
        xAxis={{innerTickSize: 6, label: "Years Worked"}}
        yAxis={{label: "Hourly Salary"}}				
				margin={{top: 10, bottom: 50, left: 100, right: 10}}
			/>			
			</div>
		) 
	}
}
export default ScatterPlot

/*
	TODO: fix scatterPlot and normalize data
*/