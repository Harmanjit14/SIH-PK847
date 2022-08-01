import React from "react";
import { partners } from "./Partners";
import List from "./List";
import "./ListItem.css";
import Header from "../Home/Header";
const ListItem = () => {
  return (
    <div className="listItem">
      <Header />
      <List data={partners} />
    </div>
  );
};

export default ListItem;
