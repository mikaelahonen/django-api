import React, { Component } from 'react';
import { Navbar, MenuItem, Nav, NavDropdown, NavItem } from 'react-bootstrap';
import { Link } from 'react-router-dom'

class Menu extends Component {
  render() {
    return (
      <Navbar inverse collapseOnSelect>
		<Navbar.Header>
		  <Navbar.Brand>
			<a href="/">QS</a>
		  </Navbar.Brand>
		  <Navbar.Toggle />
		</Navbar.Header>
		<Navbar.Collapse>
		  <Nav>
			<NavItem eventKey={1}><Link to="/">Home</Link></NavItem>
			<NavItem eventKey={2}>Link</NavItem>
			<NavDropdown eventKey={3} title="Gym" id="basic-nav-dropdown">
			  <MenuItem header>Home</MenuItem>
			  <MenuItem eventKey={3.1}><Link to='/gym'>Gym</Link></MenuItem>
			  <MenuItem divider />
			  <MenuItem header>Templates</MenuItem>
			  <MenuItem eventKey={3.2}><Link to='/gym/workouts'>Workouts</Link></MenuItem>
			  <MenuItem divider />
			  <MenuItem header>Training</MenuItem>
			  <MenuItem eventKey={3.3}>Separated link</MenuItem>
			</NavDropdown>
		  </Nav>
		  <Nav pullRight>
			<NavItem eventKey={1} href="/">User</NavItem>
			<NavItem eventKey={2} href="/">Link Right</NavItem>
		  </Nav>
		</Navbar.Collapse>
	  </Navbar>
    );
  }
}

export default Menu;
