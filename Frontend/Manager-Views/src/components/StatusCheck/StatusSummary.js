import React from "react";
import "./StatusSummary.css";

const StatusSummary = (props) => {
  console.log(props.data.data);
  return (
    <>
      <div className="status">
        <div className="statusHeading">
          <h3>Status Summary</h3>
        </div>
        <table>
          <tr>
            <th>ID</th>
            <th>Order</th>
            <th>Status</th>
          </tr>
          {props.data.data.map((ele) => {
            return (
              <tr>
                <td>
                  <span className="statusId">{ele.id} </span>
                </td>
                <td>
                  <span className="statusName">{ele.text}</span>
                </td>
                <td>
                  <span className="statusCheck">{ele.status}</span>
                </td>
              </tr>
            );
          })}
        </table>
      </div>
    </>
  );
};

export default StatusSummary;
