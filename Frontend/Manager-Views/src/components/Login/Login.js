import React, { useState } from "react";
import "./Login.css";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  return (
    <div className="login">
      <img
        src="https://th.bing.com/th/id/OIP.i-lH9uduHJkkhEk6I1wCLwHaB2?w=348&h=87&c=7&o=5&dpr=1.25&pid=1.7"
        alt="Logo"
      />
      <form>
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          type="email"
        />
        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          type="password"
        />
        <button type="submit">Sign In</button>
      </form>
    </div>
  );
};

export default Login;
