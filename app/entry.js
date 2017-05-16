import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';

import Index from './views/Index';
import NotFound from './views/NotFound';
import MapComponent from './layouts/components/MapComponent'
import Nurses from './layouts/components/Nurses'
// All of our CSS
require('../public/css/main.scss');

ReactDOM.render(
  <Router>
    <Switch>
      <Route path="/" exact component={Index} />
      <Route path="/map" exact component={MapComponent} />
      <Route path="/nurse-list" exact component={Nurses} />			
      <Route component={NotFound} status={404} />
    </Switch>
  </Router>,
  document.getElementById('root'),
);
