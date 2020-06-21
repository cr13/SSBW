import React, { Component } from 'react';
import '../css/dark-mode.css';

class Menu extends Component {
  render() {
    return (
      
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div className="container">
            <a className="navbar-brand" href="/">Visitas Granada</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarResponsive">
                <ul className="navbar-nav ml-auto">
                    <li className="nav-item active">
                        <a className="nav-link" href="/">Inicio
                          <span className="sr-only">(current)</span>
                        </a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/">Añadir Visita</a>
                    </li>
                    <li>
                        <span className="nav-link" id="tipolectura" > <i className="fa fa-moon-o" aria-hidden="true"></i></span>
                    </li>

                    <li className="nav-item">
                        <a className="nav-link" href="/">Login</a>
                    </li> 
                </ul>
            </div>

            </div>
        </nav> 
    );
  }
}

export default Menu;
