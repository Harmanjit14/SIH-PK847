import React from "react";
import "./ListItem.css";

const List = (props) => {
  console.log(props.data.info);
  return (
    <>
      <div>
        {props.data.info.map((ele) => {
          return (
            <div className="div1">
              <div className="driverName">{ele.text}</div>
              <div className="driverLoad">
                {ele.header ? "" : <span className=""> {ele.load}</span>}
              </div>
            </div>
          );
        })}
      </div>
    </>
  );
};

export default List;
