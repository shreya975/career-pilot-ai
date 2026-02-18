import React, { useState } from "react";
import {
  flexibleAnalysis
} from "../api/api";

import ProfileCard from "./ProfileCard";
import SkillsAnalysis from "./SkillsAnalysis";
import RoadmapTimeline from "./RoadmapTimeline";
import ProjectsList from "./ProjectsList";
import RoleChart from "./RoleChart";

export default function Dashboard() {

  const [mode, setMode] = useState("");
  const [file, setFile] = useState(null);
  const [skills, setSkills] = useState("");
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);


  const handleAnalyze = async () => {

    const formData = new FormData();

    if (mode === "resume" && file)
      formData.append("file", file);

    if (mode === "skills" && skills)
      formData.append("skills", skills);

    if (role)
      formData.append("target_role", role);

    setLoading(true);

    try {

      const data = await flexibleAnalysis(formData);

      setResult(data);

    } catch {
      alert("Backend not running");
    }

    setLoading(false);

  };


  return (

    <div className="min-h-screen flex">

      {/* SIDEBAR */}

      <div className="w-64 bg-slate-900 p-6">

        <h1 className="text-2xl font-bold text-primary">
          Career Copilot AI
        </h1>

        <p className="text-slate-400 mt-2">
          Career Intelligence Dashboard
        </p>

      </div>


      {/* MAIN CONTENT */}

      <div className="flex-1 p-10">

        {/* INPUT CARD */}

        <div className="bg-card p-6 rounded-xl shadow-lg">

          <h2 className="text-xl font-semibold mb-4">
            Analyze Your Career Profile
          </h2>


          <select
            className="w-full p-3 bg-slate-800 rounded-lg mb-4"
            value={mode}
            onChange={(e) => setMode(e.target.value)}
          >

            <option value="">Select Input Method</option>
            <option value="resume">Upload Resume</option>
            <option value="skills">Enter Skills</option>
            <option value="role">Select Role Only</option>

          </select>


          {mode === "resume" && (

            <input
              type="file"
              className="w-full mb-4"
              onChange={(e) => setFile(e.target.files[0])}
            />

          )}


          {mode === "skills" && (

            <input
              type="text"
              placeholder="python, react, docker"
              className="w-full p-3 bg-slate-800 rounded-lg mb-4"
              onChange={(e) => setSkills(e.target.value)}
            />

          )}


          {mode && (

            <select
              className="w-full p-3 bg-slate-800 rounded-lg mb-4"
              value={role}
              onChange={(e) => setRole(e.target.value)}
            >

              <option value="">Auto Detect Role</option>
              <option>Backend Developer</option>
              <option>Frontend Developer</option>
              <option>Full Stack Developer</option>

            </select>

          )}


          <button
            onClick={handleAnalyze}
            className="w-full bg-primary hover:bg-indigo-600 p-3 rounded-lg font-semibold"
          >

            {loading ? "Analyzing..." : "Analyze"}

          </button>

        </div>


        {/* RESULTS */}

        {result && (

          <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">

            <ProfileCard profile={result.profile}/>

            <SkillsAnalysis skills={result.skills}/>

            <RoadmapTimeline roadmap={result.roadmap}/>

            <ProjectsList roadmap={result.roadmap}/>

            <RoleChart roleScores={result.role_scores}/>

          </div>

        )}

      </div>

    </div>

  );
}
