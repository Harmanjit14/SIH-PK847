import React from "react";
import { statusInfo } from "./CertiData";
import StatusSummary from "./StatusSummary";
import Header from "../Home/Header";
import "./StatusCheck.css";

const StatusCheck = () => {
  return (
    <div className="statusCheck">
      <Header />
      <StatusSummary data={statusInfo} />
    </div>
  );
};

export default StatusCheck;
