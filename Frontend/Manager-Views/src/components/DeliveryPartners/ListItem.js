import React from "react";
import { partners } from "./Partners";
import "./ListItem.css";
import List from "./List";
const ListItem = () => {
  return <List data={partners} />;
};

export default ListItem;
