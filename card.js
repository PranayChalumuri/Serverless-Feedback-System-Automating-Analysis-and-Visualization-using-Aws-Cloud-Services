import React from "react";

export const Card = ({ children }) => {
  return <div className="shadow-lg p-4 rounded-md">{children}</div>;
};

export const CardContent = ({ children }) => {
  return <div className="p-4">{children}</div>;
};
