import React, { Component } from 'react';
import '../css/App.css';


class ListaVisitas extends Component {

  detalleItem(visita_id) {
    window.location.href="/visita/"+visita_id+"/";
  }

  renderItems = () => {
  let cardText={
      overflow: 'hidden',
      display: '-webkit-box',
      webKitLineClamp: '4',
      WebkitBoxOrient: 'vertical',
      };
    const newItems = this.props.listado;
    console.log(this.props.listado)
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
     
      return (
        <div className="row">
           {this.renderItems()}
        </div>
    
      );
    
  }
}

export default ListaVisitas;
