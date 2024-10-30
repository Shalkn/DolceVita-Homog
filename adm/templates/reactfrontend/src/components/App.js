import React from "react";
import Header from "./Header";
import ProductCard from "./ProductCard";
import Footer from "./Footer";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";


export default class App extends React.Component {
    render(){
        return(
            <div className="main">
                <Header />
                <ProductCard />
                <Footer />
            </div>
        );
    }
}