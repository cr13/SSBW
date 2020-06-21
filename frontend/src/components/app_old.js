import React, { Component } from 'react';
import '../css/App.css';


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

  detalleItem(visita_id) {
    console.log('Se hizo click'+visita_id);
  }

  renderItems = () => {
  let cardText={
      overflow: 'hidden',
      display: '-webkit-box',
      webKitLineClamp: '4',
      WebkitBoxOrient: 'vertical',
      };
   const newItems = this.state.visitas;
    return newItems.map(item => (                 
          <div  key={item.id} className="col-lg-4 col-md-6 mb-4">
            <div className="card h-100">
                   
                  <img className="card-img-top" src={item.foto} width="200" height="180" />
              
              <div className="card-body">
                <h4 className="card-title">   
                  {item.nombre}
                </h4>
                <p style={cardText} className="card-text">
                  {item.descripcion}
                </p>
              </div>
              <div className="card-footer">
                <p>
                   <button type='button' className="w3-button w3-block w3-indigo"   data-toggle="tooltip" 
                    data-placement="top" title="Ver más"  onClick={() => this.detalleItem(item.id)}  > 
                    Detalle
                   </button>

                </p>
              
              </div>
            </div>
          </div>

              
           
      ));
  };

  render() {
     
    if (this.state.visitas.length > 0) {
      return (
        <div className="row">
           {this.renderItems()}
        </div>
    
      );
    } else {
      return <p className="text-center">No hay visitas disponible</p>
    }
  }
}

export default App;
