import "./App.css";
import Login from "./components/Login/Login";
import ListItem from "./components/DeliveryPartners/ListItem";
import Home from "./components/Home/Home";
import StatusCheck from "./components/StatusCheck/StatusCheck";
//import "bootstrap/dist/css/bootstrap.min.css";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/login" element={<Login />} />
      </Routes>
      <Routes>
        <Route path="/deliveryPartners" element={<ListItem />} />
      </Routes>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
      <Routes>
        <Route path="/statusCheck" element={<StatusCheck />} />
      </Routes>
    </div>
  );
}

export default App;
