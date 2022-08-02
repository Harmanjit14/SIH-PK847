import React from "react";
import Header from "./Header";
import Card from "./Cards";
import Footer from "./Footer";
import "./Home.css";

const Home = () => {
  return (
    <div className="home">
      <Header />
      <div className="certi-sec">
        <div className="certiHeading">
          <h2>Pending Requests</h2>
        </div>
        <div className="certi-section-1">
          <div className="certi-section-1a">
            <Card
              Cardtitle="Certi Check"
              Cardbody=" it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letrase"
            />
          </div>
          <div className="certi-section-1b">
            <Card
              Cardtitle="Certi Check"
              Cardbody=" it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letrase"
            />
          </div>
          <div className="certi-section-1c">
            <Card
              Cardtitle="Certi Check"
              Cardbody=" it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letrase"
            />
          </div>
        </div>
        <div className="certi-section-2">
          <div className="certi-section-2a">
            <Card
              Cardtitle="Certi Check"
              Cardbody=" it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letrase"
            />
          </div>
          <div className="certi-section-2b">
            <Card
              Cardtitle="Certi Check"
              Cardbody=" it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letrase"
            />
          </div>
          <div className="certi-section-2c">
            <Card
              Cardtitle="Certi Check"
              Cardbody=" it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letrase"
            />
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Home;
