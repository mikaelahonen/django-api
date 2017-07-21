import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col } from 'react-bootstrap';
//React Router
import {Switch, Route} from 'react-router-dom'
//Gym components
import GymHome from './GymHome'
import GymWorkouts from './GymWorkouts'

class Gym extends Component {
  render() {
    return (
		<Switch>
			<Route exact path='/gym' component={GymHome}/>
			<Route path='/gym/workouts' component={GymWorkouts}/>
		</Switch>
	);
  }
}

export default Gym;