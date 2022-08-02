import React from "react";
import "./List.css";

const List = (props) => {
  console.log(props.data.info);
  return (
    <>
      <div className="list">
        <div className="listHeading">
          <h3>Delivery Partners</h3>
        </div>
        <table>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Assigned Jobs</th>
          </tr>
          {props.data.info.map((ele) => {
            return (
              <tr>
                <td>
                  <span className="driverId">{ele.id} </span>
                </td>
                <td>
                  <span className="driverName">{ele.text}</span>
                </td>
                <td>
                  <span className="driverLoad">{ele.load}</span>
                </td>
              </tr>
            );
          })}
        </table>
      </div>
    </>
  );
};

export default List;
