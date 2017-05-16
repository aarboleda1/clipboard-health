import React from 'react';
import { Link } from 'react-router-dom';
import Main from '../layouts/Main';
import Nurses from '../layouts/components/Nurses';
import NavInstance from '../layouts/components/Nav';
import ScatterPlot from '../layouts/components/ScatterPlot';

const Index = () => (
  <Main>
    <div className="col-sm-12" id="index">
      <h1>Nurse Dashboard</h1>
    </div>
		<ScatterPlot />
		<Link to={`/map`}>
			View Nurse Map
		</Link>	
		<Link to={`/nurse-list`}>
			View Nurse List
		</Link>					
  </Main>
);

export default Index;
/*
	Todo: Creat a Nav bar with styling for proper routing
*/