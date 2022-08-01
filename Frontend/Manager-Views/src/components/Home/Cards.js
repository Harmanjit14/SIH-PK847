import React from "react";
import { Typography } from "@material-ui/core";
import Button from "@material-ui/core/Button";
import cert from "../../assets/1.png";

import "./Cards.css";

function Card({ Cardtitle, Cardbody }) {
  return (
    <div className="card">
      <div>
        <img className="card-image" src={cert} href="Alt" />
      </div>
      <div className="card-title">
        <Typography variant="h5" align="left">
          {Cardtitle}
        </Typography>
      </div>
      <div className="card-body">
        <Typography variant="p" align="center">
          {Cardbody}
        </Typography>
      </div>
      <div className="card-buttons">
        <div className="card-button1">
          <Button
            variant="contained"
            color="primary"
            target="_blank"
            rel="noopener"
          >
            Assign
          </Button>
        </div>
        <div className="card-button2">
          <Button
            variant="contained"
            color="success"
            target="_blank"
            rel="noopener"
          >
            Status
          </Button>
        </div>
      </div>
    </div>
  );
}

export default Card;
