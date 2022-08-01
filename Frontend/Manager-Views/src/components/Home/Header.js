import React from "react";
import { NavLink } from "react-router-dom";
import "./Header.css";

const Header = () => {
  return (
    <div className="header">
      <div className="req">
        <NavLink
          to="/"
          style={{ textDecoration: "none" }}
          activeClassName="current"
          exact
        >
          <h4>Requests</h4>
        </NavLink>
      </div>
      <div className="deli">
        <NavLink
          to="/deliveryPartners"
          style={{ textDecoration: "none" }}
          activeClassName="current"
          exact
        >
          <h4>Delivery Partners</h4>
        </NavLink>
      </div>
      <div className="stats">
        <NavLink
          to="/statusCheck"
          style={{ textDecoration: "none" }}
          activeClassName="current"
          exact
        >
          <h4>Status Summary</h4>
        </NavLink>
      </div>
    </div>
  );
};

export default Header;
