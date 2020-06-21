import React, { Component } from 'react';

class visita extends React.Component {
 
    constructor(props) {
        super(props)
        this.state = { visita: {} }
    } 
    
    
    componentWillMount() {
        fetch('http://localhost:8000/api/apivisitas/' + this.props.match.params.id + '/')
          .then((response) => {
            return response.json()
          })
          .then((data) => {
              console.log(data);
            this.setState({ visita: data })
        })
      }

    updateLike(value){

        fetch('http://localhost:8000/api/likes/' + this.state.visita.id, {
        method: 'PUT',
        body: JSON.stringify({
            "id": this.state.visita.id,
            "likes": this.state.visita.likes + value 
        }),
        headers: {
            'Content-Type': 'application/json'
        }
        }).then(function (response) {
            console.log(response)
          });

        this.setState({
              visita: {
                ['likes']: this.state.visita.likes + value 
              }
            })   
        this.componentWillMount();
        this.render();
        
    }

    render() {
    
    return (  
        
        <div className="row">
    
            <div className="ftco-section ftco-no-pt ftco-no-pb">
                <div className="container">
                    <div className="row d-flex no-gutters">
                        <div className="col-md-6 d-flex">
    
                            <div className="img d-flex align-items-center justify-content-center py-md-0">
                                
                                <img className="card-img-top"  src={this.state.visita.foto} width="200" height="400" />
                                
                            </div>
                        </div>

                        <div className="col-md-6 pl-md-5 pt-md-5">
                            <div className="row justify-content-start py-5">
                                <div className="col-md-12 heading-section ftco-animate"> 
                                    <div className="d-flex flex-row bd-highlight mb-3">
                                       <div className="p-2 bd-highlight"><span className="subheading" id="likestotal">{this.state.visita.likes} </span><span className="subheading"> likes</span></div>                                      
                                        <a class="btn ButtonIncrementLikes" data-id-visit="this.props.id" onClick={this.updateLike.bind(this, 1)}><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>
                                        <a class="btn ButtonDecrementLikes" data-id-visit="this.props.id" onClick={this.updateLike.bind(this, -1)}><i class="fa fa-thumbs-o-down" aria-hidden="true"></i></a>                                          
                                    </div>
                                    
                                    <h2 className="mb-4" id="nombre" >  {this.state.visita.nombre}</h2>
                                    <p id="descripcion">{this.state.visita.descripcion}</p>
                                </div>
                            </div>
                            <div className="row justify-content-start py-5">
                              

                                <div className="col-sm-6">
                                    <button id="editar" type='button' className="w3-button w3-block w3-indigo"   data-toggle="tooltip" data-placement="top" title="Ver más" > 
                                    <i className="fa fa-pencil-square-o" aria-hidden="true"></i> Editar
                                </button>

                                 </div>
                              
                                 <div className="col-sm-6">
                                   <button id="borrar" type='button' className="w3-button w3-block w3-indigo"   data-toggle="tooltip" data-placement="top" title="Ver más" > 
                                    <i className="fa fa-trash" aria-hidden="true"></i> Eliminar
                                </button>
                                 </div>
                              
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )      
    }   
}
   
  export default visita;