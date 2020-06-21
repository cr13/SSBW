import React, { Component } from 'react';
import '../css/App.css';
import ListaVisitas from './lista_visitas';
import Visita from './visita' 

import { BrowserRouter as Router, Switch } from 'react-router-dom'


class App extends Component {
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
     
    if (this.state.visitas.length > 0) {
      return (
        
            <Router>
              <Switch>
                <Route path="/" exact>
                  <ListaVisitas listado={this.state.visitas} />
                </Route>
                 <Route path="/visita/:id" exact component={Visita} >
                </Route>
              
              </Switch>
            </Router>
    
      );
    } else {
      return <p className="text-center">No hay visitas disponible</p>
    }
  }
}

export default App;
