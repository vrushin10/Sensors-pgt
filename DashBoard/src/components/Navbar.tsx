import * as React from "react";

const MyNavbar: React.FC = () => {
  return (
    <nav className="bg-blue-500 p-4">
      <div className="container mx-auto flex items-center justify-between">
        <div className="text-2xl font-bold text-white">GIS system</div>
        <ul className="flex space-x-4">
          <li className="text-white">
            <a href="/">Home</a>
          </li>
          <li className="text-white">
            <a href="/about">About</a>
          </li>
          <li className="text-white">
            <a href="/contact">Contact</a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default MyNavbar;
