export default function RoadmapTimeline({ roadmap }) {

  return (
    <div className="card">

      <h2>Roadmap</h2>

      {roadmap.phases.map((phase, i) => (
        <div key={i}>
          <h3>{phase.phase} - {phase.title}</h3>

          {phase.skills &&
            phase.skills.map((skill, j) => (
              <p key={j}>{skill.name}</p>
            ))}

        </div>
      ))}

    </div>
  );
}
