import React from 'react';
//Put into a tagble
const Nurse = ({nurse}) => {
	const { salary, city, experience, department, education } = nurse;
	return (
		<div className="nurse-list-item">
		<p><strong>Location:</strong>{city} <strong>YOE:</strong>{ experience } <strong>Department:</strong>{ department} <strong>Education:</strong> { education } <strong>Hourly Salary:</strong> {salary}</p>
		</div>
	)
}

export default Nurse;
