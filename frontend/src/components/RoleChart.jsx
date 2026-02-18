import React from "react";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";

import { Bar } from "react-chartjs-2";


// ENTERPRISE FIX — register scales
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);


export default function RoleChart({ roleScores }) {

  if (!roleScores) return null;


  const labels = Object.keys(roleScores);
  const values = Object.values(roleScores);


  const data = {

    labels,

    datasets: [
      {
        label: "Role Match %",
        data: values,
        backgroundColor: "#6366f1",
        borderRadius: 6,
      },
    ],
  };


  const options = {

    responsive: true,

    plugins: {
      legend: {
        display: false,
      },
    },

    scales: {
      y: {
        beginAtZero: true,
        max: 100,
      },
    },
  };


  return (

    <div className="bg-card p-6 rounded-xl shadow">

      <h2 className="text-lg font-semibold mb-4">
        Role Match Analysis
      </h2>

      <Bar data={data} options={options} />

    </div>

  );
}
