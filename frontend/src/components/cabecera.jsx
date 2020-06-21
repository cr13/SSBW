import React, { Component } from 'react';


class Cabecera extends Component {
  constructor(props) {
    super(props)
    this.state = { visitas: [] }
  }

  componentWillMount() {
    fetch('http://localhost:8000/api/apivisitas/')
      .then((response) => {
        return response.json()
      })
      .then((visitas) => {
        this.setState({ visitas: visitas })
    })
  }
  render() {
    return (
        <div className="container text-center">
        <h1>Visita en Granada</h1>
        <p className="lead">
              Se dispone de {this.state.visitas.length} visitas
        </p>
      </div>
      
    );
  }
}

export default Cabecera;
