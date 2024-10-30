import React from "react";
import axios from 'axios';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";


class Contact extends React.Component {
  state = { details: [] };
  server = 'http://localhost:8000';

  componentDidMount() {
    axios.get(`${this.server}/prod/`)
      .then(res => {
        this.setState({
          details: res.data
        });
      })
      .catch(err => console.error(err));
  }

  render() {
    const sliderSettings = {
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,  // Exibe um slide por vez
      slidesToScroll: 1,
    };

    return (
      <div id="produtos" className="product">
        <div className="element-contact" id="element-contact">
          <img className="imgsorvete3" src="/img/sorvete.svg" alt="Sorvete 3" />
          <img className="imgsorvete4" src="/img/sorvete.svg" alt="Sorvete 3" />
          <img className="imgacai6" src="./img/acai.svg" alt="Açaí 6" />
          <img className="imgacai7" src="/img/acai.svg" alt="Açaí 7" />
          <img className="imgacai8" src="/img/acai.svg" alt="Açaí 8" />
          <img className="imgacai9" src="/img/acai.svg" alt="Açaí 9" />
          <img className="imgacai10" src="/img/acai.svg" alt="Açaí 10" />
        </div>
        
        <div className="product-carousel">
          <Slider {...sliderSettings}>
            {this.state.details.map((data, id) => (
              <div key={id} className="product-card1">
                <div className="product-content">
                  
                  <div className="product-text1">
                    <p id="nome-product" key={id} className="product-description">{data.nome}</p>
                    <p id="descricao-product" key={id} className="product-description">{data.descricao}</p>
                    <p id="preco-product" key={id} className="product-description">R$ {data.preco}</p>
                  </div>
                  <img id="img-product" className="product-image" src={data.imagem} alt={data.nome} />



                </div>
              </div>
            ))}
          </Slider>
        </div>
      </div>
    );
  }
}

export default Contact;
