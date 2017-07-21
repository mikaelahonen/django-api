import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col } from 'react-bootstrap';

class Head extends Component {
  render() {
    return (
		<div>
			<h1>{this.props.head}</h1>
			<legend></legend>
		</div>
    );
  }
}


export default Head;
