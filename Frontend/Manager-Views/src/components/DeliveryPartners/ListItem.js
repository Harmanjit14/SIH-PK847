import React from "react";
import { partners } from "./Partners";
import "./ListItem.css";

const ListItem = () => {
  return {
    ...partners.info((driver) => {
      return (
        <li>
          <div className="driverName">{driver.text}</div>
          <div className="driverLoad">
            {driver.header ? "" : <span className=""> {driver.load}</span>}
          </div>
        </li>
      );
    }),
  };
};

export default ListItem;
