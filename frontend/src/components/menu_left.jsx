import React, { Component } from 'react';


class Menuleft extends Component {

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


  renderItems = () => {

    const newItems = this.state.visitas;
    return newItems.map(item => (
        <a href={"/visita/"+item.id+"/"} className="list-group-item">{item.nombre}</a>                 
           
      ));
  };

  render() {
    return (
        <div>
            <h1 className="my-4">Visitas</h1>
            <div className="list-group">
               {this.renderItems()}

            </div>
        </div>
    );
  }
}

export default Menuleft;
